from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import Table, MetaData
from app.modassembly.database.sql.get_sql_session import get_sql_session

def insert_data(data: List[Dict[str, Any]], table_name: str) -> None:
    """
    Inserts parsed data into the specified table in the database.

    :param data: A list of dictionaries where each dictionary represents a row to be inserted.
    :param table_name: The name of the table where data should be inserted.
    """
    metadata = MetaData()
    with get_sql_session() as session:  # type: Session
        table = Table(table_name, metadata, autoload_with=session.bind)
        session.execute(table.insert(), data)
        session.commit()
