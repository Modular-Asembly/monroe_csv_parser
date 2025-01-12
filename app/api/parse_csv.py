import pandas as pd
from typing import IO
from app.api.insert_data import insert_data

def parse_csv(file: IO[bytes]) -> None:
    """
    Parses a CSV file, extracts the table name, column names, and data rows,
    and inserts the data into the specified table in the database.

    :param file: A file-like object representing the CSV file.
    """
    # Read the CSV file
    df = pd.read_csv(file)

    # Extract the table name from the first column
    table_name = df.columns[0]

    # Extract column names from the second row
    column_names = df.iloc[0].tolist()

    # Extract data rows starting from the third row
    data_rows = df.iloc[1:].to_dict(orient='records')

    # Map data rows to the column names
    mapped_data = [{column_names[i]: row[column_names[i]] for i in range(len(column_names))} for row in data_rows]

    # Insert data into the specified table
    insert_data(mapped_data, table_name)
