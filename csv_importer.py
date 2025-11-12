"""
Módulo para importar archivos CSV a PostgreSQL
"""
import pandas as pd
from pathlib import Path
from database import connect_postgres


def import_csv_to_db(csv_dir_path, table_name, column_map, transform_func=None, columns_not_nullable=None):
    """
    Lee todos los CSVs de una carpeta y los carga a PostgreSQL con nombres de columnas personalizados
    
    Args:
        csv_dir_path: Ruta al directorio donde están los CSVs
        table_name: Nombre de la tabla en la BD
        column_map: Diccionario con mapeo {nombre_bd: nombre_csv}
        transform_func: Función opcional para transformar el DataFrame antes de insertarlo
        columns_not_nullable: Lista de columnas que no pueden ser NULL (se reemplazan con '-')
    """
    # 1. Conectar a la base de datos
    engine = connect_postgres()
    if engine is None:
        return
    
    # 2. Obtener todos los archivos CSV del directorio
    csv_dir = Path(csv_dir_path)
    if not csv_dir.exists():
        print(f"❌ No se encontró el directorio: {csv_dir_path}")
        return
    
    csv_files = list(csv_dir.glob("*.csv"))
    
    if not csv_files:
        print(f"⚠️ No se encontraron archivos CSV en: {csv_dir_path}")
        return
    
    print(f"📁 Encontrados {len(csv_files)} archivos CSV en '{csv_dir_path}'")
    print("-" * 60)
    
    total_rows = 0
    successful_files = 0
    failed_files = 0
    
    # 3. Procesar cada archivo CSV
    for csv_file in csv_files:
        try:
            print(f"\n📖 Procesando: {csv_file.name}")
            
            # Leer el CSV
            df = pd.read_csv(csv_file)
            print(f"   ✅ Leídas {len(df)} filas")
            
            # Crear un DataFrame nuevo con las columnas mapeadas
            df_new = pd.DataFrame()
            
            # Ahora el mapeo es: {nombre_bd: nombre_csv}
            for db_col, csv_col in column_map.items():
                if csv_col in df.columns:
                    # Copiar la columna del CSV y asignarla al nombre de la BD
                    df_new[db_col] = df[csv_col].apply(
                        lambda x: x.strip() if isinstance(x, str) else x
                    )
                else:
                    # Si no existe en el CSV, crear columna vacía
                    df_new[db_col] = None

            # Aplicar transformaciones personalizadas si existen
            if transform_func:
                df_new = transform_func(df_new)
            
            # Reemplazar NULL con guión en columnas no nullables
            if columns_not_nullable:
                for col in columns_not_nullable:
                    if col in df_new.columns:
                        df_new[col] = df_new[col].fillna('-')
            
            # Cargar a la base de datos
            df_new.to_sql(
                name=table_name,
                con=engine,
                if_exists='append',  # Agrega a la tabla existente
                index=False
            )
            
            print(f"   ✅ {len(df_new)} registros cargados a '{table_name}'")
            total_rows += len(df_new)
            successful_files += 1
            
        except Exception as e:
            print(f"   ❌ Error al procesar {csv_file.name}:")
            print(f"   {str(e)}")
            failed_files += 1
    
    # 4. Resumen final
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN:")
    print(f"   ✅ Archivos procesados exitosamente: {successful_files}")
    print(f"   ❌ Archivos con error: {failed_files}")
    print(f"   📈 Total de registros cargados: {total_rows}")
    print("=" * 60)
