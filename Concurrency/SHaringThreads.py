import time
from threading import Thread
import random

counter=0

def increment_counter():
    global counter
    time.sleep(random.random())
    counter +=1
    time.sleep(random.random())
    print(f"New counter vale {counter}")
    time.sleep(random.random())
    print("________")

for x in range(10):
    t=Thread(target=increment_counter)
    time.sleep(random.random())
    t.start()

