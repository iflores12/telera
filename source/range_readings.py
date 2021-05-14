import time
import board
import busio
import adafruit_vl53l0x

from db_utils import insert_range_reading

def get_reading():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_vl53l0x.VL53L0X(i2c)

    range_readings_arr = []
    for num in range(3):
        range_readings_arr.append(sensor.range)
        time.sleep(1)
    
    return range_readings_arr 


def avg_reading(arr):
    return sum(arr) / len(arr)


def insert_into_sqlite(run_id, reading):
    pass


def height(run_id):
    readings = get_reading()
    avg_range = avg_reading(readings)

    print('Range: {}mm'.format(avg_range))
    insert_range_reading(run_id, avg_range)
