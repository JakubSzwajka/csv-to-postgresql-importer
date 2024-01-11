# Overview

This Python script automates the process of importing CSV files into a PostgreSQL database. It reads the CSV files, infers the data types of each column, creates corresponding tables in the PostgreSQL database, and then inserts the data into these tables.

## Requirements

- Python 3.x
- Pandas
- SQLAlchemy
- Progress

## Installation

Before running the script, ensure that you have the required Python libraries installed. You can install them using pip:

```bash
pip install pandas sqlalchemy progress
```

## Configuration

- Place your CSV files in the data folder.
- Update the TABLES list in the script with the names of your CSV files.
- Set your database URL in the environment variable DATABASE_URL.

## Usage

To run the script, execute the following command:

```bash
python path_to_script.py
```

Replace `path_to_script.py` with the actual path to the script if it's not in your current directory.

## How It Works

- Reading CSV: The script reads each CSV file from the specified list.
- Inferring Data Types: Data types for each column in the CSV are inferred using Pandas.
- Creating Tables: Corresponding tables with appropriate data types are created in the PostgreSQL database.
- Inserting Data: Data from the CSV files are inserted into the created tables.

## Customization

Modify the `pandas_dtype_to_sql` and `pandas_dtype_to_sqlalchemy_type` functions to handle additional data types or to change the data type mappings.
Adjust the logging level or format as needed for your debugging purposes.

## Important Notes

Ensure that your PostgreSQL database is accessible and that the `DATABASE_URL` is correctly set.
The script currently handles common data types like object, float64, and int64. Additional data types may require extra handling.
Large CSV files might take a significant amount of time to process and import.