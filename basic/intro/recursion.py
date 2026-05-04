import sys
from time import sleep

sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

def greet():
    print("Habari")
    sleep(0.02)
    greet()

greet()