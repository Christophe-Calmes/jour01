#Job17
debug = False
def modulo3 (i):
    if i%3 == 0:
        print("Fizz")

def modulo5 (i):
    if i%5 == 0:
        print("Buzz")
def modulo53 (i):
    if (i%3 == 0) & (i%5 == 0):
        print("FizzBuzz")
def otherwise(i):
       if (i%3 != 0) & (i%5 != 0):
        print(i)

for i in range(1, 100):
    if debug:
        print(i)
    modulo3(i)
    modulo5(i)
    modulo53(i)
    otherwise(i)
 