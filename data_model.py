from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    engine = Column(String, nullable=False)
    fuel_type = Column(String, nullable=False)
    color = Column(String, nullable=False)
    mileage = Column(Integer, nullable=False)
    doors = Column(Integer, nullable=False)
    transmission = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    def to_dict(self):
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

# Cria o engine e o banco de dados SQLite
engine = create_engine('sqlite:///vehicles.db', echo=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("DatabAse created with sucess!")
