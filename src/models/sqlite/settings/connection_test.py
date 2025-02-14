from sqlalchemy.engine import Engine
from .connection import db_connection_handler

def test_connect():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect()
    db_engine = db_connection_handler.get_engine()
    
    assert db_engine is not None
    assert isinstance(db_engine, Engine)
