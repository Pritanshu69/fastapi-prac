from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:prit1924@localhost:5432/fastapiprit"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autoflush=False, autocommit = False, bind=engine)