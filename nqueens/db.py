from queens import size, solucion_individual, solutions
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://postgres:Holacode@localhost:5432/soluciones"

db = create_engine(db_string)
base = declarative_base()

class NQueens(base):
    __tablename__ = 'reynas'

    numero_de_reynas = Column(Integer, primary_key=True)
    lista = Column(ARRAY(Integer))
    total_de_soluciones = Column(Integer)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Create
eight_queens = NQueens(numero_de_reynas=size, lista=solucion_individual, total_de_soluciones=solutions)
session.add(eight_queens)
session.commit()
