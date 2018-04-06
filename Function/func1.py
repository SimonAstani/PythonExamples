def prhello():
    "Print Hello"
    print("Hello, world")

prhello()

def prlines(str, num):
    for n in range(0, num):
        print(str * (n+1))

prlines('z',5)
print()
prlines('fred', 4)
