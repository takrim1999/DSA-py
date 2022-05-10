# Practical of how recursion works
# downward stacks
def first():
    second()
    print("first one")
def second():
    third()
    print("Second one")
def third():
    fourth()
    print("third one")
def fourth():
    fifth()
    print("fourth one")
def fifth():
    sixth()
    print("fifth one")
def sixth():
    print("sixth one")
first()