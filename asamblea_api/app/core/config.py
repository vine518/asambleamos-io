import os
import pathlib

from dotenv import load_dotenv


def load_environment():
    """Carga el archivo .env adecuado basado en APP_ENV."""
    # Define el entorno actual (por defecto, 'local')
    env = os.getenv("APP_ENV", "local").lower()

    # Define el nombre del archivo .env basado en el entorno
    env_file = f".env.{env}"
    file_path = pathlib.Path(env_file)

    # Carga el archivo .env usando python-dotenv
    if os.path.exists(file_path):
        load_dotenv(file_path)
        print(f"Loaded environment: {file_path}")
    else:
        raise FileNotFoundError(f"Environment file {file_path} not found.")


load_environment()
