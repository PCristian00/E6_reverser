def reverser(stringa):
    indice = (len(stringa) - 1)
    rev = ""
    while indice >= 0:
        rev += stringa[indice]
        indice -= 1
    print(rev)


s = input("Inserire stringa da invertire: ")
reverser(s)
