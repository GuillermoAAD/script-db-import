"""
Script principal para importar CSVs a PostgreSQL
"""
from dotenv import dotenv_values
import importlib
from csv_importer import import_csv_to_db

config = dotenv_values(".env")

# Importar configuración dinámica
config_module_name = config.get('CONFIG_FILE')
config_module = importlib.import_module(config_module_name)
COLUMN_MAP = config_module.COLUMN_MAP
TABLE_NAME = config_module.TABLE_NAME
CSV_DIR_PATH = config_module.CSV_DIR_PATH
TRANSFORM_FUNC = getattr(config_module, 'TRANSFORM_FUNC', None)  # Opcional
COLUMNS_NOT_NULLABLE = getattr(config_module, 'COLUMNS_NOT_NULLABLE', None)  # Opcional


if __name__ == "__main__":
    # Importar todos los CSVs del directorio
    import_csv_to_db(
        csv_dir_path=CSV_DIR_PATH,        
        table_name=TABLE_NAME,
        column_map=COLUMN_MAP,
        transform_func=TRANSFORM_FUNC,
        columns_not_nullable=COLUMNS_NOT_NULLABLE,
    )

