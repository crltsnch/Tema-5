import datetime
import time
import os

def main():
    while True:
        os.system('clear')
        dt = datetime.datetime.now()
        print('{}:{}:{}'.format(dt.hour, dt.minute, dt.second))
        time.sleep(1)