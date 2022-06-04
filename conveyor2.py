# Конструкция yield from позволяет создать связь между внешним и внутренним генераторами
# Значение, переданное (проброшенное) методу send внешнего генератора g, будет отправлено во внутренний генератор
# Значение переменной reset позволяет сбросить счетчик
# Конструкция yield from передает внтутреннему генератору в т.ч. исключения
# Yield from используется в асинхронном программировании

def range(start, stop):
    current = start
    while current < stop:
        reset = yield current
        if reset is not None:
            current = reset - 1
        current += 1

def two_ranges(start, stop):
    yield from range(start,stop)
    yield from range(start, stop)

g = two_ranges(0, 3)
print(next(g))
print(next(g))
print(g.send(-1))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
