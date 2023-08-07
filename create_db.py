from database import Base, engine
from models_sql import Item


print("Creating database.........")
Base.metadata.create_all(engine)