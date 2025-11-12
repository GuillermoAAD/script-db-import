# Configuración para importar datos de infracciones

COLUMN_MAP = {
    'id_c_infracciones': 'id',
    # 'estacionometros': 'xxxxxxx' #! Sin equivalente
    # 'veces_salario_minimo': 'xxxxxxx' #! Sin equivalente
    'articulos': 'fraction',
    # //! Estos son los que tiene la tabla pim_ticket_types
    # 'name' #! Sin equivalente
}

TABLE_NAME = "pim_tickets"

CSV_DIR_PATH = "csv/infracciones"

