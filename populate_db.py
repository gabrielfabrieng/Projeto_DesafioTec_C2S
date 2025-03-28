# populate_db.py
"""
Populate the database with fake vehicle records.
"""

import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from data_model import engine, Vehicle, Base

fake = Faker('pt_BR')

# Sample data lists
BRANDS = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen']
MODELS = ['Corolla', 'Civic', 'Focus', 'Onix', 'Golf']
FUEL_TYPES = ['Gasolina', 'Diesel', 'Flex', 'Elétrico']
TRANSMISSIONS = ['Manual', 'Automática']

def generate_vehicle() -> Vehicle:
    """
    Generate and return a fake Vehicle instance.
    """
    return Vehicle(
        brand=random.choice(BRANDS),
        model=random.choice(MODELS),
        year=random.randint(2000, 2023),
        engine=f"{random.randint(1, 4)}.0L",
        fuel_type=random.choice(FUEL_TYPES),
        color=fake.color_name(),
        mileage=random.randint(0, 200000),
        doors=random.choice([2, 3, 4, 5]),
        transmission=random.choice(TRANSMISSIONS),
        price=round(random.uniform(20000, 150000), 2)
    )

def populate_database(n: int = 100) -> None:
    """
    Insert 'n' fake vehicle records into the database.
    
    Args:
        n: Number of records to insert.
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    vehicles = [generate_vehicle() for _ in range(n)]
    session.bulk_save_objects(vehicles)
    session.commit()
    session.close()
    print(f"{n} records inserted successfully!")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    populate_database(100)
