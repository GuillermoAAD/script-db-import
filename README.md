# Script DB Import

Script en Python para importar archivos CSV a PostgreSQL con mapeo personalizado de columnas y transformaciones de datos.

## 📋 Requisitos

- Python 3.x
- PostgreSQL

## 🚀 Instalación

1. Clonar el repositorio
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Copiar el archivo de configuración:
```bash
cp .env.example .env
```

4. Configurar las variables de entorno en `.env`

## ⚙️ Variables de Entorno

### Conexión a la Base de Datos

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `DB_CONNECTION` | Tipo de conexión a la base de datos | `pgsql` |
| `DB_HOST` | Host del servidor PostgreSQL | `localhost` |
| `DB_PORT` | Puerto del servidor PostgreSQL | `5432` |
| `DB_DATABASE` | Nombre de la base de datos | `mi_base_datos` |
| `DB_USERNAME` | Usuario de PostgreSQL | `postgres_user` |
| `DB_PASSWORD` | Contraseña del usuario | `mi_password` |

### Configuración de Importación

| Variable | Descripción | Ejemplo |
|----------|-------------|---------|
| `CONFIG_FILE` | Archivo de configuración a utilizar (usar notación de puntos) | `configs.config_infracciones` |

**Nota:** Para la variable `CONFIG_FILE`, usa la notación de puntos de Python. Por ejemplo:
- `configs.config_infracciones` para el archivo `configs/config_infracciones.py`
- `configs.config_clientes` para el archivo `configs/config_clientes.py`


## 🔧 Configuración

Cada archivo de configuración en `configs/` debe contener:

- `COLUMN_MAP`: Diccionario de mapeo `{columna_bd: columna_csv}`
- `TABLE_NAME`: Nombre de la tabla destino
- `CSV_DIR_PATH`: Ruta al directorio con los CSVs
- `COLUMNS_NOT_NULLABLE` (opcional): Lista de columnas que no pueden ser NULL
- `TRANSFORM_FUNC` (opcional): Función para transformar datos antes de insertar


## Entorno virtual

Para hacer uso de un entorno virtual revisar el siguiente [documento](docs/venv.md)

## 🏃 Uso

```bash
python3 main.py
```
