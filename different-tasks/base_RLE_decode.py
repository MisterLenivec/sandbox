# Кодирование длин серий — это базовый алгоритм сжатия данных.
# В этой задаче мы реализуем алгоритм дешифровки строк, закодированных с помощью одного из самых простых
# вариантов кодирования длин серий.
# На вход алгоритму подаётся строка, содержащая цифры и символы латинского алфавита.
# Эта строка разбивается на так называемые "серии", которые кодируются парой число-символ или просто символ
# (в таком случае число считается равным единице). Результат должен содержать эти серии в том же порядке,
# что они и встречаются в исходной строке, при этом каждая серия раскрывается в последовательность символов
# соответствующей длины.
# Sample Input:
# 3ab4c2CaB
# Sample Output:
# aaabccccCCaB

def dec(val):
    num, string = '', ''
    for symb in val:
        if (symb.isdigit()):
            num += symb
        else:
            if (num):
                string += symb * int(num)
                num = ''
            else:
                string += symb
    return string


if (__name__ == '__main__'):
    print(dec(input()))