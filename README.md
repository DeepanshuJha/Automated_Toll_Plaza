# Automated Toll Plaza

This is a IoT based project. As we know that standing at toll plaza for so many hours is a time taking task so the solution for this problem is to make a web application or mobile app where users can register themselves and provide vehicle details as well. So when they are making a trip to some place then they can pay the toll prize before reaching to the toll pay booth. So that when the vehicle is passing then camera can capture the image before hand and send the captured image for number plate extraction. After the number plate is extracted in String Form then we can check that if the user with this vehicle id has paid then accordingly the gates will be open.

Otherwise the user has to pay the toll. So there are two lanes for incoming and outgoing. One we will use for the users who have paid the task already and they can use the fast lane and the other who have not paid will use the normal lane.

Let's now install the Hardware and Software part of project.

## Hardware Requirements

1. Raspberry Pi 3
2. Pi Camera Module
3. IR Sensor
4. Servo Motor
5. Male to Female Wires

## Software requirements

1. [Node.js](https://nodejs.org/en/download/)
2. [MongoDB](https://docs.mongodb.com/v3.2/administration/install-community/)
3. Python3
4. [Raspbian Stretch with Desktop and recommended software](https://www.raspberrypi.org/downloads/raspbian/)

## Installation

To install all modules of node

```node.js
npm init
npm install mongoose 
npm install express 
npm install express-ejs-layouts 
npm install connect-flash express-session passport
npm bcryptjs
```

To install python modules

```python
pip install dnspython
```

To install pymongo

```bash
sudo apt-get remove python-pip
sudo apt-get remove pymongo

wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

sudo python -m pip install pymongo==3.0.3
```

Check it out

```python
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['local']
collection = db['local']
startlog = db.startup_log
startlog.find_one()
```

## Circuit  Connections

IR sensor 
* Connect Vout to signal pin 16 of Pi 3.
* Connect Ground to signal pin 34 of Pi 3.
* Connect Vcc to signal pin 4 of Pi 3.

Note : Here signal pin does not mean GPIO pin.

Servo Motor
* Connect Orange(PWM) wire to signal pin 3 of Pi 3.
* Connect Red(+5v) wire to signal pin 2 of Pi 3.
* Connect Brown(Ground) wire to signal pin 6 of Pi 3.

Pi Camera
* Insert the cable of Pi camera to camera module of Pi 3.

## Running the project

Part 1 (pi 3 part)
1. After connecting all the connections with Pi 3 properly, start the Pi 3 and open Thonny Editor.
2. Open data_extractor.py and paste your user id and password from [MongoDb Atlas](https://www.mongodb.com/cloud/atlas)
3. Run the servo.py.

Part 2 (Web Interface)

1. Open app.js and paste your user id and password of mongodb atlas.
2. Then run app.js by typing below command in terminal.

```node.js
node app.js
```
3. Go on to the browser and type localhost:8000.

The web app demo is shown [here](https://pure-beyond-56772.herokuapp.com/).
Demo for full working model is [here](https://drive.google.com/open?id=17U2GXdK9pPVyYAf33utGGPj84EgG-Jg7).
