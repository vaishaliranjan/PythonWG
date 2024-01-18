from collections import deque
from types import coroutine
friends= deque(("Rolf","Jose","Vaishali"))

@coroutine
def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting=yield
        print(f'{greeting}{friend}')

async def greet(g):
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)
    print("starting")
    await g
    print("ending") # until all friends is empty and func ends or end the coroutine

greeter = greet(friends_upper())
greeter.send(None)
greeter.send("Hello")
print("doint multitasking  ")
greeter.send("How are you?")