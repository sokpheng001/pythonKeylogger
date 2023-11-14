import psycopg2
import uuid
import random

uuid_value = uuid.uuid4();
number = random.randint(1,999999);

role = "";


try :
    print("Insert role: ", "", end="");
    role = str(input(""));
    conn = psycopg2.connect(
        database="tester", user='postgres', password='123', host='localhost', port='5432'
    )

    conn.autocommit = True;
    cursor = conn.cursor();
    # cursor.execute('CREATE TABLE roles (id SERIAL PRIMARY KEY, role VARCHAR(255))')
    # conn.commit()

    # cursor.execute('''DELETE FROM roles WHERE id IS NOT NULL''');
    # conn.commit();

    cursor.execute(f'''INSERT INTO roles (id, role) VALUES ({number},  '{role.upper()}')''');
    # Commit your changes in the database
    conn.commit()

    print("Records inserted........")
    cursor.execute("SELECT * FROM roles");
    print(cursor.fetchall());
    print("Connection is successfully")
    conn.close();
except EnvironmentError:
    print(EnvironmentError);


