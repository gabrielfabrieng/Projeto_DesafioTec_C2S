# data_model.py
"""
Module defining the data model for vehicles using SQLAlchemy.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from config import settings

Base = declarative_base()

class Vehicle(Base):
    """
    Represents a vehicle record.
    """
    __tablename__ = 'vehicles'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    brand: str = Column(String, nullable=False)
    model: str = Column(String, nullable=False)
    year: int = Column(Integer, nullable=False)
    engine: str = Column(String, nullable=False)
    fuel_type: str = Column(String, nullable=False)
    color: str = Column(String, nullable=False)
    mileage: int = Column(Integer, nullable=False)
    doors: int = Column(Integer, nullable=False)
    transmission: str = Column(String, nullable=False)
    price: float = Column(Float, nullable=False)

    def to_dict(self) -> dict:
        """
        Convert the Vehicle instance to a dictionary.
        """
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "engine": self.engine,
            "fuel_type": self.fuel_type,
            "color": self.color,
            "mileage": self.mileage,
            "doors": self.doors,
            "transmission": self.transmission,
            "price": self.price
        }

# Create the engine using the DATABASE_URL from configuration.
engine = create_engine(settings.DATABASE_URL, echo=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("Database created successfully!")
