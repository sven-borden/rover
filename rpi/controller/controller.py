## Module controller
from controller.communications.communications import Communications
from controller.sensors.sensors import Sensors
import time

class Controller:

    def __init__(self):
        self.com = Communications()
        self.sensors = Sensors()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def run(self):
        self.com.send('0,0,\n')
        while(True):
            self.com.send('20,20,\n')
            time.sleep(0.2)

    def get_sensors(self):
        self.com.send('SEN\n')
        data = self.com.read()
        self.sensors.update(data)

    def get_distance(self):
        self.com.send('DIS\n')
        data = self.com.read()
        if len(data) > 0:
            data = data[0].decode()
            self.sensors.distance = int(data)
