import time

def greet(name, cb):
    print(f"Hello, {name}")
    time.sleep(3)
    cb()

def say_bye():
    print("Bye!!")

#Main
greet("Steve", say_bye)


print("Continuing main ...")
#More statements