# pip install -e .
# these imports should work
#   from package1 import ...
#   from package2.module1 import ...

from package1 import module1



def myscript1():
    # put whatever main1.py did here
    print("hello")

def myscript2():
    # put whatever main2.py did here
    print("world")


def myscript3():
    # put whatever main2.py did here
    # print("world")
    module1.testVal()
    print("My values are:")
    print(module1.myInteger())
    print(module1.myBoolean())
    print(module1.myString())
