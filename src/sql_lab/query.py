#importing :))) 
import logging
import os
import mysql.connector

#reading database info from variables
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

logging.basicConfig(level=logging.INFO)

def get_data_by_group(value):
    """Return rows where the group column matches the value."""
    logging.info("Getting data by group")
#connecting to database
    db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)

    cursor = db.cursor()
#finding the rows that match the group with certain requirements 
    query = "SELECT * FROM mock WHERE `group` = %s"
    cursor.execute(query, (value,))

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results
#counting data
def plot_counts(groupby):
    """Count rows for each value in a column."""
    logging.info("Counting data")

    db = mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)

    cursor = db.cursor()
#counting how many rows are in groups
    query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    db.close()

    return results
#printing 
def main():
    """running example database queries."""
    print(get_data_by_group("A"))
    print(plot_counts("group"))


if __name__ == "__main__":
    main()

