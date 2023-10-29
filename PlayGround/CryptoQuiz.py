import random


def modulo_quiz1():
    print("modulo quiz1")
    p = 0x10001
    a = random.randint(1, p)
    b = random.randint(1, p)
    print(f"{a = }")
    print(f"{b = }")

    if int(input("a + b = ? (mod p) > ")) != (a + b) % p:
        exit("Wrong!")
    if int(input("a - b = ? (mod p) > ")) != (a - b) % p:
        exit("Wrong!")
    if int(input("a * b = ? (mod p) > ")) != (a * b) % p:
        exit("Wrong!")

    print("Good Job!")


def modulo_quiz2():
    print("modulo quiz2")
    p = 15260339158265275051  # 64bit prime
    a = random.randint(1, p)
    b = random.randint(1, p)
    print(f"{a = }")
    print(f"{b = }")

    d = int(input("a / b = ? (mod p) > "))
    if (d * b - a) % p != 0:
        exit("Wrong!")

    print("Good Job!")


def modulo_quiz3():
    print("modulo quiz3")
    p = 15260339158265275051  # 64bit prime
    a = random.randint(1, p)
    b = random.randint(1, p)
    print(f"{a = }")
    print(f"{b = }")

    if int(input("a**b = ? (mod p) > ")) != pow(a, b, p):
        exit("Wrong!")

    print("Good Job!")


if __name__ == "__main__":
    modulo_quiz1()
    modulo_quiz2()
    modulo_quiz3()

    flag = open("flag", "rb").read()
    print(flag)
