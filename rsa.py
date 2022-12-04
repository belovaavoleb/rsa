# алгоритм евклида для проверки взаимной простоты пары чисел
def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


def task(n, m):
    return gcd(n, m) == 1


# формирование массива простых чисел (для проверки на простоту)
prost = []
for i in range(2, 1000):
    count = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            count += 1
    if count == 0:
        prost.append(i)

while True:
    # подготовка ключей для шифрования
    print(" ")
    print("Нам надо подготовить ключи для шифрования!")

    p, q = map(int, input("Введите два простых числа: ").split())

    if (p in prost) and (q in prost):
        n = p * q  # модуль - произведение наших простых чисел
        f = (p - 1) * (q - 1)  # функция Эйлера

        mas_e = [] # формируем массив из всех возможных чисел e
        for i in range(2, f + 1):
            if (i in prost) and task(i, f) == True: # критерии для e : простое, меньше f и взаимно простое с f
                mas_e.append(i)

        print("Выберете одно из чисел для e:", *mas_e)
        e = int(input()) # ввод выбранного числа e

        # пара чисел (е, n) - открытый ключ шифрования
        if e in mas_e: #найдем число d - для закрытого ключа - условие для d: (d × е) % f = 1
            d = 0
            for i in range(2, n):
                if (i * e) % f == 1:
                    d = i

        # пара чисел (d, n) - закрытый ключ для расшифровки

            try:
                message = input("Введите сообщение в виде числа (меньшее p*q): ")
                message = int(message)
                if message < n:

                    shifr = (message ** e) % n
                    print("После шифровки: ", shifr)

                    deshifr = (shifr ** d) % n
                    print("После расшифровки: ", deshifr)
                else:
                    print("Вы ввели слишком большое число!")
            except:
                print("Вы ввели некорректное сообщение!")

        else:
            print("Вы ввели некоректное значение е!")
    else:
        print("Вы ввели некоректные числа!")
