# Configuración para importar datos de infracciones
import pandas as pd
from datetime import datetime

COLUMN_MAP = {
    # //! Estos son los que tiene la tabla infracciones
    # id_infraccion
    # id_placa #! Sin equivalente
    # placa
    # paterno_infraccion
    # materno_infraccion
    # fecha_multa
    # cve_infraccion #TODO: Posible equivalencia
    # importe_infraccion
    # descuento_infraccion #! Sin equivalente
    # hora_infraccion #? YA se implementa en date
    # cve_agente #TODO: Posible equivalencia
    # grua #! Sin equivalente
    # examen_medico #! Sin equivalente
    # almacenaje #! Sin equivalente
    # conduccion_punible #! Sin equivalente
    # total_importe_infraccion #! Sin equivalente
    # id_pago #! Sin equivalente
    # capturo
    # vigencia
    # fecha
    # adicional_obras #! Sin equivalente
    # adicional_asistencia #! Sin equivalente
    # adicional_mejoramiento #! Sin equivalente
    # grua_a_cobrar #! Sin equivalente
    # examen_medico_a_cobrar #! Sin equivalente
    # almacenaje_a_cobrar #! Sin equivalente
    # numero_captura #! Sin equivalente
    # observaciones
    # captura
    # serie #! Sin equivalente
    # c_id_infracciones #! Sin equivalente
    # id_c_infraccion #! Sin equivalente
    # adicional_deportivo #! Sin equivalente
    # adicional_educacion #! Sin equivalente
    # grado #! Sin equivalente
    # corralon_folio #! Sin equivalente
    # descuento_punible #! Sin equivalente
    # descuento_almacenaje #! Sin equivalente
    # descuento_examen #! Sin equivalente
    # descuento_grua #! Sin equivalente
    # art27 #! Sin equivalente
    # marca #! Sin equivalente
    # tipo_vehiculo #! Sin equivalente
    # color #! Sin equivalente
    # procedencia #! Sin equivalente
    # domicilio_conductor #! Sin equivalente
    # colonia_conductor #! Sin equivalente
    # ciudad_conductor #! Sin equivalente
    # licencia_conductor
    # tipo
    # nombre_propietario #! Sin equivalente
    # domicilio_propietario #! Sin equivalente
    # colonia_propietario #! Sin equivalente
    # ciudad_propietario #! Sin equivalente
    # observaciones_tablet #! Sin equivalente
    # boleta
    # linea #! Sin equivalente
    # lugar_infraccion
    # procesar #! Sin equivalente
    # modelo #! Sin equivalente
    # serie_infracciones #! Sin equivalente
    # vigencia_placa #! Sin equivalente
    # cve_infraccion1 #! Sin equivalente
    # cve_infraccion2 #! Sin equivalente
    # cve_infraccion3 #! Sin equivalente
    # cve_infraccion4 #! Sin equivalente
    # cve_infraccion5 #! Sin equivalente
    # nombres_infraccion #! Sin equivalente
    # nombre_archivo #! Sin equivalente
    # articulos #! Sin equivalente
    # latitud
    # longitud
    # id_bitacora_cargado_masivo_infracciones #! Sin equivalente

    # //! Estos son los que tiene la tabla pim_ticket_types
    "id": "id_infraccion", #?
    "folio": "boleta", #! Sin equivalente (pim usa int y este tiene letras)
    "date": "fecha_multa", #?
    "cancel_date": None,#! Sin equivalente
    "latitude": "latitud", #?
    "longitude": "longitud", #?
    "amount": "importe_infraccion", #?
    "uploaded_to_state": None,
    "status_ticket": None,
    # "agent_id": None,
    # "state_id": None,
    "created_at": None,
    "updated_at": None,
    "canceled_at": None,
    "driver_identification_type": None,
    "driver_identification_number": "licencia_conductor", #?
    "comment_ticket": None,
    "ticket_comment": None,
    "created_by": "capturo", #?
    "updated_by": None,
    "canceled_by": None,
    "plate": "placa", #?
    "street": "lugar_infraccion", #?
    "neighborhood": "lugar_infraccion",
    "cross_street": None,
    "cross_street_2": None,
    "driver_firstname": None,
    "driver_first_lastname": "paterno_infraccion", #?
    "observations": "observaciones", #?
    "driver_second_lastname": "materno_infraccion", #?
    "line": None,
    "status": "vigencia", #?
    "class_service": None,
}

TABLE_NAME = "pim_tickets"

CSV_DIR_PATH = "csv/infracciones"

COLUMNS_NOT_NULLABLE = [
    'plate',
    'street',
    'neighborhood',
    'created_by',
    'updated_by',

    # 'amount',
]

# Función para transformar los datos antes de insertarlos
def TRANSFORM_FUNC(df):
    """Transforma el DataFrame antes de insertarlo en la BD"""
    
    # Transformar la columna 'status' a valores válidos
    # Ajusta los valores según lo que acepte tu constraint
    if 'status' in df.columns:
        # Convertir valores: V='active', P='paid', C='canceled', otros='canceled'
        def transform_status(x):
            if x == 'V':
                return 'active'
            elif x == 'P':
                return 'paid'
            elif x == 'C':
                return 'canceled'
            else:
                return 'canceled'  # Cualquier otro valor
        
        df['status'] = df['status'].apply(transform_status)
    
    # Limitar la columna 'plate' a 7 caracteres
    if 'plate' in df.columns:
        df['plate'] = df['plate'].apply(
            lambda x: str(x)[:7] if pd.notna(x) else x
        )
    
    # Agregar fecha actual si 'date' está NULL
    if 'date' in df.columns:
        df['date'] = df['date'].fillna(datetime.now())

    # Reemplazar NULL en 'amount' con 0.0
    if 'amount' in df.columns:
        df['amount'] = df['amount'].fillna(0.0)
    
    return df