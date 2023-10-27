def feladat1():
    n = 0
    while n < 150:
        if n % 2 == 0:
            print(n, end="; ")
        n += 1
    print(150, end="")

def feladat2():
    oszt = 0
    sorszam = 1

    while sorszam <= 10:
        szam = int(input(f"Kérem adja meg a(z) {sorszam}. számot: "))
        if szam % 3 == 0:
            oszt += 1
        sorszam += 1
    print(f"A bekért számok esetében {oszt} olyan szám található, amely 3-mal osztahtó.")

def feladat3():
    x = int(input("Kérem adjon meg egy olyan számot, ami 10-zel osztható: "))
    while not(x % 10 == 0):
        x = int(input("Kérem adjon meg egy olyan számot, ami 10-zel osztható: "))

def feladat4():
    n = int(input("Kérem adjon meg egy kétjegyű páros számot: "))
    while not (n % 2 == 0 and (100 > n > 9 or -100 < n < -9)):
        n = int(input("Hibás szám! Nem kétjegyű páros számot adott meg! Kétjegyű, páros szám: "))
    print("Gratulálunk, kétjegyű, páros számot adtál meg!")

def feladat5():
    n2 = int(input("Kérem adjon meg egy pozitív, páratlan számot: "))
    while not (n2 % 2 == 1 and (0 < n2)):
        n2 = int(input("Hibás szám! Nem pozitív, páratlan számot adott meg! Pozitív, páratlan szám: "))
    print("Gratulálunk, pozitív, páratlan számot adtál meg!")

# def feladat6():
#     ...

def feladat7():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    while not(a + b > c and c + b > a and a + c > b):
        print("A háromszög nem szerkeszthető.")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    print("A háromszög szerkeszthető.")

def feladat8():
    szoveg = input("Kérem adjon meg egy szöveget, ami legalább 3 karakteres: ")
    while not(len(szoveg) >= 3):
        szoveg = input("Kérem adjon meg egy szöveget, ami legalább 3 karakteres: ")
    print(str.upper(szoveg))
