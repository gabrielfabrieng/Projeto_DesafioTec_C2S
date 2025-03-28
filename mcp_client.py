# mcp_client.py
"""
MCP client that sends filter criteria to the server and returns vehicle records.
"""

import json
import socket
from typing import Any, Dict, Union
from config import settings

def send_request(filters: Dict[str, Union[str, int, float]], 
                 host: str = settings.MCP_HOST, 
                 port: int = settings.MCP_PORT) -> Any:
    """
    Sends a JSON request with filter criteria to the MCP server and returns the response.
    
    Args:
        filters: Dictionary with filter criteria.
        host: Server host.
        port: Server port.
    
    Returns:
        Parsed JSON response from the server.
    """
    data = json.dumps(filters).encode('utf-8')
    with socket.create_connection((host, port)) as sock:
        sock.sendall(data + b'\n')
        response = sock.recv(4096)
    try:
        results = json.loads(response.decode('utf-8'))
    except json.JSONDecodeError:
        results = {"error": "Invalid response from server."}
    return results

if __name__ == '__main__':
    sample_filters = {
        "brand": "Toyota",
        "year_min": 2010,
        "fuel_type": "Gasolina"
    }
    vehicles = send_request(sample_filters)
    print(json.dumps(vehicles, indent=4, ensure_ascii=False))
