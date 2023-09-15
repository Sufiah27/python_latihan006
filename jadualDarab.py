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
    for k in range(1,13):
        print(f"\t(k)\t", end="")
    print()

    saizJadual = 12
    for i in range(1, saizJadual + 1):
        for l in range(1, saizJadual + 1):
            jumlah = i * l
            print(f"{jumlah:>5}", end=" ")
        print()


if __name__ == '__main__':
    darab()
