import logging
import os
from progress.bar import Bar
import pandas as pd
from sqlalchemy import (
    create_engine,
    String,
    Float,
    BigInteger,
    MetaData,
    Table,
    Column,
)
from sqlalchemy.dialects.postgresql import insert

logging.basicConfig(
    format="%(asctime)s - %(levelname)s: %(message)s", level=logging.DEBUG
)


TABLES = [
    # put a list of file names here from the data/ folder
]


def pandas_dtype_to_sql(dtype):
    if dtype == "object":
        return "TEXT"
    elif dtype == "float64":
        return "FLOAT"
    elif dtype == "int64":
        return "BIGINT"
    else:
        return "TEXT"  # Default, or you can raise an error


def pandas_dtype_to_sqlalchemy_type(dtype):
    if dtype == "object":
        return String
    elif dtype == "float64":
        return Float
    elif dtype == "int64":
        return BigInteger
    else:
        return String  # Default, or you can raise an error


def create_table_from_csv(csv_file, table_name):
    engine = create_engine(
        os.environ.get("DATABASE_URL"),
    )
    metadata = MetaData()

    logging.info(f"Loading {table_name}...")
    df = pd.read_csv(csv_file, delimiter="|", low_memory=False)
    logging.debug(f"{table_name} len: {len(df)}")

    columns = [
        Column(column, pandas_dtype_to_sqlalchemy_type(str(dtype)))
        for column, dtype in df.dtypes.items()
    ]

    table = Table(table_name, metadata, *columns)

    logging.info(f"Creating table {table_name}...")
    metadata.create_all(engine)
    logging.info(f"Created table {table_name}...")

    logging.info(f"Inserting data into {table_name}...")
    with engine.connect() as conn:
        with Bar("Processing", max=len(df)) as bar:
            for _, row in df.iterrows():
                stmt = insert(table).values(**row.to_dict())
                conn.execute(stmt)
                bar.next()


if __name__ == "__main__":
    with Bar("Processing", max=len(TABLES)) as bar:
        for table in TABLES:
            create_table_from_csv(
                f"./data/{table}",
                table.split("-")[0],
            )
            bar.next()
