from machine import Pin
import time

class TrafficLight:
    def __init__(self, red_pin, yellow_pin, green_pin):
        self.red = Pin(red_pin, Pin.OUT)
        self.yellow = Pin(yellow_pin, Pin.OUT)
        self.green = Pin(green_pin, Pin.OUT)
        
    def set_state(self, r, y, g, delay):
        self.red.value(r)
        self.yellow.value(y)
        self.green.value(g)
        time.sleep(delay)
        
    def run_normal_cycle(self):
        self.set_state(1, 0, 0, 10)
        self.set_state(1, 1, 0, 3)
        self.set_state(0, 0, 1, 10)
        for i in range(3):
            self.set_state(0, 0, 1, 0.3)
            self.set_state(0, 0, 0, 0.3)
        self.set_state(0, 1, 0, 2)
        
    def run_alarm_cycle(self):
        self.set_state(0, 1, 0, 0.5)
        self.set_state(0, 0, 0, 0.5)

        
first_traffic_light = TrafficLight(12, 13, 14)

while True:
    first_traffic_light.run_normal_cycle()