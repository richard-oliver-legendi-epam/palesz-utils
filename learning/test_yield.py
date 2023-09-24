def test_yield():
    print(1)

    yield 1

    print(2)


print(">>", test_yield())
print(">>", next(test_yield()))
