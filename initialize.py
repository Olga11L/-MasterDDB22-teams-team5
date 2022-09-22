from typing import final
import psycopg2
from dbConfig import config

def createTables():
    """Create Tables in the Database"""

commands = (
     """
    CREATE TABLE movie (
        Movie_id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        genre VARCHAR(255) NOT NULL,
        url VARCHAR(255) NOT NULL
    )
    """,
    """
    CREATE TABLE sales(
        Sales_id SERIAL PRIMARY KEY,
        FOREIGN KEY (Movie_id)
            REFERENCES movie (Movie_id),
        box_office
    )
    """,
    """
    CREATE TABLE review(
        Reviewer_id SERIAL PRIMARY KEY,
        FOREIGN KEY (Review_id)
            REFERENCES review (Review_id),
        FOREIGN KEY (Movie_id)
            REFERENCES movie (Movie_id),
        review VARCHAR(255) NOT NULL,
        anx numeric NOT NULL,
        ang numeric NOT NULL,
        sad numeric NOT NULL,
        score integer NOT NULL
    )
    """,
    """
    CREATE TABLE reviewer(
        Review_id SERIAL PRIMARY KEY,
        FOREIGN KEY (Movie_id)
            REFERENCES movie (Movie_id),
        typesofrev integer  NOT NULL,
        name VARCHAR(255) NOT NULL  
    )
    """
)

conn = None

try:
    params = config() 
    conn = psycopg2.connect(**params)

    cur = conn.cursor()

    for command in commands:
        cur.execute(command)
        
        print("Tables are successfully created")

        cur.close()
        conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

if __name__ == "__main__":
    createTables()