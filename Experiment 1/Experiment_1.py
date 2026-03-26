import time

dpth = 0

def complexRec(n):
    global dpth
    dpth += 1

    if n <= 2:
        print(dpth)
        return

    p = n
    while p > 0:
        temp = [0] * n
        for i in range(n):
            temp[i] = i ^ p
        p >>= 1

    small = [0] * n
    for i in range(n):
        small[i] = i * i

    if n % 3 == 0:
        small.reverse()
    else:
        small.reverse()

    complexRec(n // 2)
    complexRec(n // 2)
    complexRec(n // 2)


if __name__ == "__main__":
    n = int(input())

    start = time.time()

    complexRec(n)

    end = time.time()

    duration = (end - start) * 1000  # convert to milliseconds

    print("Recursion Depth =", dpth)
    print("Time =", int(duration))
