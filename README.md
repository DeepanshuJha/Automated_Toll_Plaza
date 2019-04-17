# Automated Toll Plaza

This is a IoT based project. As we know that standing at toll plaza for so many hours is a time taking task so the solution for this problem is to make a web application or mobile app where users can register themselves and provide vehicle details as well. So when they are making a trip to some place then they can pay the toll prize before reaching to the toll pay booth. So that when the vehicle is passing then camera can capture the image before hand and send the captured image for number plate extraction. After the number plate is extracted in String Form then we can check that if the user with this vehicle id has paid then accordingly the gates will be open.

Otherwise the user has to pay the toll. So there are two lanes for incoming and outgoing. One we will use for the users who have paid the task already and they can use the fast lane and the other who have not paid will use the normal lane.

Lets now install the Hardware and Software part of project.

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

