import logging

from sqlalchemy import event, Engine

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("assembly-system")


logger = configure_logging()



@event.listens_for(Engine, "before_cursor_execute")
def log_sql_calls(conn, cursor, statement, parameters, context, executemany):
    print(f"SQL: {statement}")  # Logs the SQL executed
