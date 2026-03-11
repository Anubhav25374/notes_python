def hi():
    print("hello")


def hey(func):
    print(func.__name__)

hey(hi)