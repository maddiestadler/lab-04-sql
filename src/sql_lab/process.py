#importing everything 
import logging
import os
import mysql.connector
import pandas as pd

#these read database info from variables
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

logging.basicConfig(level=logging.INFO)

def read_data(filename):
    """reading the CSV file and return a dataframe."""
    logging.info("Reading data")

    data = pd.read_csv(filename)

    return data

def clean_data(data):
    """removes rows with missing values."""
    logging.info("Cleaning data")
#this is the part that actually removes rows that have missing values
    data = data.dropna()

    return data
#part that actually loads the data
def load_data(data, table):
    """uploading data to the mysql."""
    logging.info("Loading data")
#connects to the sql database
    try:
        db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)

        cursor = db.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS mock (id BIGINT,`group` VARCHAR(255), name VARCHAR(255), age DOUBLE, email VARCHAR(255), score BIGINT)""")

        query = """INSERT INTO mock
            VALUES (%s, %s, %s, %s, %s, %s)
        """
#inserts rows into the mock table
        for row in data.itertuples(index=False, name=None):
            cursor.execute(query, row)

        db.commit()
        cursor.close()
        db.close()

        logging.info("Data uploaded")
#prepares for errors
    except mysql.connector.Error as error:
        logging.error(error)
#allowing it to run
def main():
    """running the data after processing."""
    data = read_data("MOCK_DATA.csv")
    data = clean_data(data)
    load_data(data, "mock")

if __name__ == "__main__":
    main()

