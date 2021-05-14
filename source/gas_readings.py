import time
import board
import busio
import adafruit_sgp30

from db_utils import insert_gas_reading


def get_reading():
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    sensor = adafruit_sgp30.Adafruit_SGP30(i2c)

    sensor.iaq_init()
    sensor.set_iaq_baseline(0x8973, 0x8AAE)

    elapsed_sec = 0
    co2_arr = []

    while elapsed_sec < 20:
        time.sleep(1)
        elapsed_sec += 1
        if elapsed_sec > 15:
            co2_arr.append(sensor.eCO2)

    return co2_arr



def avg_reading(arr):
    return sum(arr) / len(arr)


def insert_into_sqlite(run_id, reading):
    pass


def gas(run_id):
    co2_arr = get_reading()
    avg_co2 = avg_reading(co2_arr)

    print(f'eCO2 = {avg_co2} ppm')
    insert_gas_reading(run_id, avg_co2)
