def fibonacci(x, y, count):
    if count == 0:
        return x
    return fibonacci(y, x+y, count-1)

if __name__ == '__main__':
    print(fibonacci(0, 1, 10))