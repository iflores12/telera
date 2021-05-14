import time
import board
import adafruit_ahtx0

from db_utils import insert_temp_reading, insert_humidity_reading


def get_reading():
    i2c = board.I2C()  # uses board.SCL and board.SDA
    sensor = adafruit_ahtx0.AHTx0(i2c)

    temp_readings_arr = []
    humidity_readings_arr = []

    for num in range(3):
        temp_readings_arr.append(sensor.temperature)
        humidity_readings_arr.append(sensor.relative_humidity)
        time.sleep(1)

    return temp_readings_arr, humidity_readings_arr


def avg_reading(arr):
    return sum(arr) / len(arr)


def insert_into_sqlite(run_id, reading):
    pass


def temp_and_humidity(run_id):
    temp, humidity = get_reading()
    avg_temp = avg_reading(temp)
    avg_humidity = avg_reading(humidity)

    print("\nTemperature: %0.1f C" % avg_temp)
    print("Humidity: %0.1f %%" % avg_humidity)

    insert_temp_reading(run_id, avg_temp)
    insert_humidity_reading(run_id, avg_humidity)
