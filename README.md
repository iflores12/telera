# telera

Welcome to a small hobby project of mine! With a little help I built a sourdough starter monitoring device using a raspberry pi zero w and some sensors. This is a detailed explanation of how to do the same and how to run this code so that you can save the output of the sensors to a small database

## Parts List

* Raspberry Pi Zero W

* Raspberry Pi Case

* [Adafruit VL53L0X]: https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/python-circuitpython

* [Adafruit AHT20]: https://learn.adafruit.com/adafruit-aht20/python-circuitpython

* [Adafruit SGP30]: https://learn.adafruit.com/adafruit-sgp30-gas-tvoc-eco2-mox-sensor/

* Mason Jar

* Plastic Mason Jar List

![](/Users/ifloreshuerta/Documents/telera/photos/cap.jpeg)

![sensors](/Users/ifloreshuerta/Documents/telera/photos/sensors.jpeg)

![sourdough_contraption](/Users/ifloreshuerta/Documents/telera/photos/sourdough_contraption.jpeg)

![sourdough_in_action](/Users/ifloreshuerta/Documents/telera/photos/sourdough_in_action.jpeg)

## Running The Code

You're going to want to create the database using the schema file so that all the relevant columns and tables are there. Make sure to use a persistent database – you have to specify so for sqlite3.

Open up crontab by typing `crontab -e`. From there add in the line `* * * * * /home/pi/baguette/run.sh`. This will run the scripts in the repo every minute and insert a new row into the sqlite database. You can adjust the cron as you see fit so that it runs at the cadence you want. I would not recommend running less than 30 seconds because it takes around 30 seconds to run the scripts. The reason it takes this long is because it takes 15-20 seconds for the eCO2 sensor to get a baseline reading so it can take some real measurements. Each sensor takes 4-5 readings and averages them just to make sure that nothing too weird is happening. 



You can output the tables to CSV and load them into excel/google sheets. Go wild and do some data analysis on all the measurements!