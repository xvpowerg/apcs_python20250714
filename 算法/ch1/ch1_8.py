def test1(n):
    print("Start:",n)
    if n < 5:
        test1(n + 1)
        print("End:",n)

test1(1)
print("End")
