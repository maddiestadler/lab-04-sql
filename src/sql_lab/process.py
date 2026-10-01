import logging
import os

import mysql.connector
import pandas as pd

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

logging.basicConfig(level=logging.INFO)

def read_data(filename):
    """Read a CSV file and return a DataFrame."""
    logging.info("Reading data")

    data = pd.read_csv(filename)

    return data

def clean_data(data):
    """Remove rows with missing values."""
    logging.info("Cleaning data")

    data = data.dropna()

    return data

def load_data(data, table):
    """Upload the data to MySQL."""
    logging.info("Loading data")

    try:
        db = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME
        )

        cursor = db.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mock (
                id BIGINT,
                `group` VARCHAR(255),
                name VARCHAR(255),
                age DOUBLE,
                email VARCHAR(255),
                score BIGINT
            )
        """)

        query = """
            INSERT INTO mock
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for row in data.itertuples(index=False, name=None):
            cursor.execute(query, row)

        db.commit()
        cursor.close()
        db.close()

        logging.info("Data uploaded")

    except mysql.connector.Error as error:
        logging.error(error)

def main():
    """Run the data upload process."""
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data, "mock")

if __name__ == "__main__":
    main()

