def greet(name, cb):
    print(f"Hello, {name}")
    cb()

#def say_bye():
 #   print("Bye!!")

#Main
greet("Steve", lambda: print("Bye!!"))
