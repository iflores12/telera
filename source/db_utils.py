import sqlite3

def get_connection():
    return sqlite3.connect("../db/sourdough.db")

def insert_gas_reading(run_id, reading):
    connection = get_connection()
    cursor = connection.cursor() 

    sql = f"""insert into carbon_dioxide values('{run_id}', '{reading}')"""
    cursor.execute(sql)
    connection.commit()
    connection.close()


def insert_temp_reading(run_id, reading):
    connection = get_connection()
    cursor = connection.cursor()

    sql = f"insert into temperature values('{run_id}', '{reading}')"
    cursor.execute(sql)
    connection.commit()
    connection.close()


def insert_humidity_reading(run_id, reading):
    connection = get_connection()
    cursor = connection.cursor()

    sql = f"insert into humidity values('{run_id}', '{reading}')"
    cursor.execute(sql)
    connection.commit()
    connection.close()


def insert_range_reading(run_id, reading):
    connection = get_connection()
    cursor = connection.cursor()

    sql = f"insert into range values('{run_id}', '{reading}')"
    cursor.execute(sql)
    connection.commit()
    connection.close()
