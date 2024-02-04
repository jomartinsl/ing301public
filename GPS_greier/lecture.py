
from typing import List


class Sensor:
    def __init__(self, id: str):
        self.id = id


class GPSSensor(Sensor):

    def __init__(self, id, time_now):
        super().__init__(id) # super() forteller oss at den refererer til den klassen vi arver fra, altså Sensor
        self.time_now = time_now

    def record_position(self):
        pass 

class Speedometer(Sensor): # Arver fra Sensor klassen
    pass

class TemperaturSensor(Sensor):
    pass

class HeartFrequencySensor(Sensor):
    pass

class GPSPoint:
    def __init__(self, timestamp: str, latitude: float, longditute: float, height: float):
        self.timestamp = timestamp
        self.latitude = latitude
        self.longditute = longditute
        self.height = height

class BikeComputer:
    def __init__(self, sensors:List[Sensor]) -> None:
        self.sensors = sensors

