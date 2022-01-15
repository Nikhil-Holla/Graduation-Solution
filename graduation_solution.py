def fact(n):
    if n == 0:
        return 1
    else:
        n = n * fact(n - 1)
    return n


def main():
    n = int(input('Enter number to calculate the your graduation success ratio: '))
    i = int(n / 2)
    w = 0
    p = 0

    while i <= n:
        w = w + int(fact(i + 1) / (fact(n - i) * fact(2 * i - n + 1)))
        if i < n:
            p = p + int(fact(i) / (fact(n - i - 1) * fact(2 * i - n + 1)))
        i = i + 1
    print(f'No. of ways of being absent at the ceremony: {p}')
    print(f'Total no. of ways to attend classes over N days: {w}')
    print(f"Final Probability: {str(p)} {'/'} {str(w)}")


main()
