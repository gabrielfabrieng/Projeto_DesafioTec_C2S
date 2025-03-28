# terminal_agent.py
"""
Terminal-based virtual agent for searching vehicles.
"""

from typing import Dict, Any
from mcp_client import send_request

def collect_filters() -> Dict[str, Any]:
    """
    Collects search filters from the user via terminal input.
    
    Returns:
        A dictionary with the filter criteria.
    """
    print("Olá, sou o agente virtual. Como posso ajudar?")
    print("Estou aqui para encontrar o veículo ideal para você!")
    
    filters: Dict[str, Any] = {}
    brand = input("Digite a marca desejada (ou deixe em branco para ignorar): ").strip()
    if brand:
        filters["brand"] = brand

    model = input("Digite o modelo desejado (ou deixe em branco para ignorar): ").strip()
    if model:
        filters["model"] = model

    ano_min = input("Digite o ano mínimo (ou deixe em branco): ").strip()
    if ano_min.isdigit():
        filters["year_min"] = int(ano_min)

    ano_max = input("Digite o ano máximo (ou deixe em branco): ").strip()
    if ano_max.isdigit():
        filters["year_max"] = int(ano_max)

    fuel_type = input("Digite o tipo de combustível (ou deixe em branco): ").strip()
    if fuel_type:
        filters["fuel_type"] = fuel_type

    price_min = input("Digite o preço mínimo (ou deixe em branco): ").strip()
    try:
        if price_min:
            filters["price_min"] = float(price_min)
    except ValueError:
        pass

    price_max = input("Digite o preço máximo (ou deixe em branco): ").strip()
    try:
        if price_max:
            filters["price_max"] = float(price_max)
    except ValueError:
        pass

    return filters

def display_vehicles(vehicles: Any) -> None:
    """
    Displays the vehicle search results in a friendly format.
    
    Args:
        vehicles: List of vehicle dictionaries.
    """
    if not vehicles:
        print("Nenhum veículo encontrado com os critérios informados.")
        return

    print("\nVeículos encontrados:")
    for v in vehicles:
        print(f"- {v['brand']} {v['model']} ({v['year']}), "
              f"Cor: {v['color']}, Quilometragem: {v['mileage']} km, Preço: R$ {v['price']:.2f}")

def main() -> None:
    """
    Main function to run the terminal agent.
    """
    filters = collect_filters()
    print("\nBuscando veículos...")
    vehicles = send_request(filters)
    display_vehicles(vehicles)

if __name__ == '__main__':
    main()
