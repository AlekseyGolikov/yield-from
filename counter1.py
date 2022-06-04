def main(n):
    """Программа в цикле перебираем числа от 1 до n
    и для каждого значения подсчитывает сумму предыдущих значений
    Пример:
    >>> main(5)
    [1, 3, 6, 10]
    >>> main(6)
    [1, 3, 6, 10, 15]
    >>> main(7)
    [1, 3, 6, 10, 15, 21]"""

    def sum():
        _sum = 0
        while True:
            n = yield _sum
            _sum = 0
            for j in range(n+1):
                _sum += j

    def count():
        while True:
            yield from sum()

    c = count()
    c.__next__()
    l = []
    for i in range(1, n):
        l.append(c.send(i))

    return l

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
