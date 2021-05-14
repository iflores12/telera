from datetime import datetime
from range_readings import height
from gas_readings import gas
from temp_humidity import temp_and_humidity


def baguette():
    run_id = datetime.now()

    height(run_id)
    gas(run_id)
    temp_and_humidity(run_id)

if __name__ == "__main__":
    baguette()
