# mcp_server.py
"""
MCP server that handles client requests for vehicle data.
"""

import json
import socketserver
import logging
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from data_model import engine, Vehicle
from config import settings

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

Session = sessionmaker(bind=engine)

class MCPRequestHandler(socketserver.StreamRequestHandler):
    """
    Handles incoming MCP requests.
    """
    def handle(self) -> None:
        """
        Read the JSON request, apply filters, and send back the vehicle records.
        """
        try:
            data = self.rfile.readline().strip()
            request = json.loads(data.decode('utf-8'))
            logging.info("Received request: %s", request)
        except json.JSONDecodeError:
            error_msg = {"error": "Invalid JSON"}
            self.wfile.write(json.dumps(error_msg).encode('utf-8') + b'\n')
            return

        filters = []
        if "brand" in request:
            filters.append(Vehicle.brand.ilike(f"%{request['brand']}%"))
        if "model" in request:
            filters.append(Vehicle.model.ilike(f"%{request['model']}%"))
        if "year_min" in request:
            filters.append(Vehicle.year >= request["year_min"])
        if "year_max" in request:
            filters.append(Vehicle.year <= request["year_max"])
        if "fuel_type" in request:
            filters.append(Vehicle.fuel_type.ilike(f"%{request['fuel_type']}%"))
        if "price_min" in request:
            filters.append(Vehicle.price >= request["price_min"])
        if "price_max" in request:
            filters.append(Vehicle.price <= request["price_max"])

        session = Session()
        query = session.query(Vehicle)
        if filters:
            query = query.filter(and_(*filters))
        vehicles = query.all()
        results = [v.to_dict() for v in vehicles]
        session.close()

        response = json.dumps(results, ensure_ascii=False)
        self.wfile.write(response.encode('utf-8') + b'\n')
        logging.info("Response sent with %d records", len(results))

if __name__ == '__main__':
    host = settings.MCP_HOST
    port = settings.MCP_PORT
    logging.info("Starting MCP server at %s:%d", host, port)
    with socketserver.ThreadingTCPServer((host, port), MCPRequestHandler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            logging.info("Server is shutting down...")
