# Q1 mall's product --> tags
# product name (vowels) -> new vowel
# BorolinU => BurulonA

from statistics import mean, mode

def ArrayFunction(strr):
    strr = strr.split(", ")
    strr[0] = strr[0][1:]
    strr[-1] = strr[-1][:-1]
    temp = list(map(lambda x: int(x), strr))
    return 1 if mode(temp) == mean(temp) else 0


print(ArrayFunction(input()))

# input [1, 3, 45, 34, 346, 23]