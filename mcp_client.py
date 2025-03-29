# mcp_client.py
import json
import socket
from typing import Any, Dict, Union
from config import settings

def receive_all(sock: socket.socket) -> bytes:
    """Recebe todos os dados enviados pelo servidor, até EOF."""
    buffer = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        buffer += data
    return buffer

def send_request(filters: Dict[str, Union[str, int, float]], 
                 host: str = settings.MCP_HOST, 
                 port: int = settings.MCP_PORT) -> Any:
    """
    Envia os filtros para o servidor MCP e retorna os veículos encontrados.
    """
    try:
        data = json.dumps(filters).encode('utf-8')
        with socket.create_connection((host, port), timeout=5) as sock:
            sock.sendall(data + b'\n')
            response = receive_all(sock)

        print("Resposta bruta recebida do servidor:", response[:300], "...[truncado]")
        results = json.loads(response.decode('utf-8'))
        return results

    except ConnectionRefusedError:
        return {"error": "Conexão recusada pelo servidor. Verifique se o servidor está rodando."}
    except socket.timeout:
        return {"error": "Tempo de resposta do servidor esgotado."}
    except json.JSONDecodeError:
        return {"error": "Resposta inválida do servidor. Não é um JSON válido."}
    except Exception as e:
        return {"error": f"Erro inesperado: {str(e)}"}

if __name__ == '__main__':
    sample_filters = {
        "brand": "Toyota",
        "year_min": 2010,
        "fuel_type": "Gasolina"
    }
    vehicles = send_request(sample_filters)
    print("\nResultado final:")
    print(json.dumps(vehicles, indent=4, ensure_ascii=False))
