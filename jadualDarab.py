def jadual():
    rows = 4
    columns = 15
    for i in range(rows):
        for k in range(columns):
            print("*", end=" ")
    print()


def jadual_sifir():
    jadual()
    nama = "Jadual Darab"
    n = nama.center(105)
    print(n)
    jadual()


def darab():
    jadual_sifir()
    for i in range(1, 13):
        print(i)
    for l in range(2, 13):
        print(rjust())


if __name__ == '__main__':
    darab()
