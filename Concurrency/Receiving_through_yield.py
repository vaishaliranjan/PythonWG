# def greet():
#     friend = yield
#     print(f"Hello {friend}")
#
#
# g=greet()
# g.send(None) # priming the generator it runs right before the yield
# g.send('Vaishali')

from collections import deque

friends= deque(("Rolf","Jose","Vaishali"))

def friends_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting=yield
        print(f'{greeting}{friend}')

def greet(g):
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)
    yield from g

greeter = greet(friends_upper())
greeter.send(None)
greeter.send("Hello")
print("doint multitasking  ")
greeter.send("How are you?")