from collections import deque

friends = deque(("Vaihsali","Ritika"))

def get_freind():
    yield from friends

def greet(g):
    while True:
        try:
            friend= next(g)
            yield f"Hello {friend}"
        except StopIteration:
            pass

friends_generator= get_freind()
g=greet(friends_generator)
print(next(g))
print(next(g))


