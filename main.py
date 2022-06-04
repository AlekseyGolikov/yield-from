
def gen1():
    yield 1
    yield 2
    yield 3
    yield 4

def gen2():
    yield 9000

    # for i in gen1():
    #     yield i
    yield from gen1()

    yield 9999

for i in gen2():
    print(i)