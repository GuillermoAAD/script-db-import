# Configuración para importar datos de c_infracciones

COLUMN_MAP = {
    # 'id_c_infracciones': 'id',
    # 'cve_infraccion': 'code',
    # 'descripcion': 'description',
    # 'importe_infraccion': 'amount',
    # 'vigencia': 'status',
    # 'capturo': 'created_by',
    # 'fecha': 'created_at',
    # # 'estacionometros': 'xxxxxxx' #! Sin equivalente
    # 'axovig': 'year',
    # # 'veces_salario_minimo': 'xxxxxxx' #! Sin equivalente
    # 'articulos': 'fraction',
    # //! Estos son los que tiene la tabla pim_ticket_types
    'id': 'id_c_infracciones',
    'code': 'cve_infraccion',
    'name': None, #! Sin equivalente
    'fraction': 'articulos',
    'year': 'axovig',
    'description': 'descripcion',
    'legal_basis': None, #! Sin equivalente
    'amount': 'importe_infraccion',
    # 'is_discount_applicable': None, #! Sin equivalente
    'status': 'vigencia',
    'created_by': 'capturo',
    # 'updated_by': 'xxxxx'
    'created_at': 'fecha',
}

# Columnas que no pueden ser NULL (se reemplazarán con '-' si están vacías)
COLUMNS_NOT_NULLABLE = [
    'code',
    'name'
    # 'amount',
]

TABLE_NAME = "pim_ticket_types"

CSV_DIR_PATH = "csv/c_infracciones"

# Función para transformar los datos antes de insertarlos
def TRANSFORM_FUNC(df):
    """Transforma el DataFrame antes de insertarlo en la BD"""
    
    # Transformar la columna 'status' a valores válidos
    # Ajusta los valores según lo que acepte tu constraint
    if 'status' in df.columns:
        # Convertir 'V' a 'active' y 'C' a 'inactive'
        df['status'] = df['status'].apply(lambda x: 'active' if x == 'V' else 'inactive')
    
    return df

