import os
import json
from dotenv import load_dotenv
from pathlib import Path
from configparser import ConfigParser


class Configurations:

    @staticmethod
    def get_config():
        path = os.getcwd()
        total_path = path + '/.env'
        dotenv_path = Path(total_path)
        load_dotenv(dotenv_path=dotenv_path)

        config = {
            "directory_path": os.getcwd(),
            "env": os.environ.get("ENV"),
            "db_name": os.environ.get("DB_NAME"),
            "db_user": os.environ.get("DB_USER"),
            "db_password": os.environ.get("DB_PASSWORD"),
            "db_host": os.environ.get("DB_HOST"),
            "db_port": os.environ.get("DB_PORT")
        }
        return config
