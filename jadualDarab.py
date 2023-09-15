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
    print("", end="")
    for k in range(1, 13):
        print(f"\t\t{k:<2}", end="")
    print()

    saizJadual = 12
    for i in range(1, saizJadual + 1):
        print(f"{i}\t", end="")
        for l in range(1, saizJadual + 1):
            jumlah = i * l
            print(f"{jumlah:>5}", end="\t")
        print()


if __name__ == '__main__':
    darab()
