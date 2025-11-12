"""
Módulo para gestionar la conexión a PostgreSQL
"""
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

config = dotenv_values(".env")


def connect_postgres():
    """
    Establece conexión con PostgreSQL usando las credenciales del .env
    
    Returns:
        engine: Motor de SQLAlchemy o None si hay error
    """
    db_url = (
        f"postgresql+psycopg2://{config.get('DB_USERNAME', 'user')}:"
        f"{config.get('DB_PASSWORD', 'password')}@"
        f"{config.get('DB_HOST', 'localhost')}:"
        f"{config.get('DB_PORT', '5432')}/"
        f"{config.get('DB_DATABASE', 'database')}"
    )

    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            print("✅ Conexión a PostgreSQL correcta")
        return engine
    except SQLAlchemyError as e:
        print("❌ Error al conectar a la base de datos:")
        print(e)
        return None
