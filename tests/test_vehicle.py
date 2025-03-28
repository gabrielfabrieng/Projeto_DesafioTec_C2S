# tests/test_vehicle.py
import pytest
from data_model import Vehicle

def test_vehicle_to_dict():
    vehicle = Vehicle(
        brand="Toyota",
        model="Corolla",
        year=2015,
        engine="2.0L",
        fuel_type="Gasolina",
        color="Branco",
        mileage=50000,
        doors=4,
        transmission="Automática",
        price=50000.0
    )
    vehicle_dict = vehicle.to_dict()
    assert vehicle_dict["brand"] == "Toyota"
    assert vehicle_dict["model"] == "Corolla"
    assert vehicle_dict["year"] == 2015
