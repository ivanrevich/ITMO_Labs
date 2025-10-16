def genFibbon(n:int)->list:
    out = [1, 1]
    while len(out)<=(n+1):
        out.append(out[-1]+out[-2])
    return [*(out[1:-1:]).__reversed__()]

def transFromFib(num:str):
    if num=="0":
        return "0"
    if "11" in num:
        return "11 can't be in Fibonachi numbers"
    if "-" in num:
        return "negative nums not supported"
    l = genFibbon(len(num))
    out = 0
    for i, el in enumerate(l):
        if num[i]=="1":
            out+=el
    return str(out)

print("--------- ПЕРЕВОДЧИК ИЗ системы Фибоначчи в 10-ричную ---------")
print("Введите число: ", end="")
num10 = str(input())
print("Это число в 10-ричной системе: ", transFromFib(num10))
print("---------------------------------------------------------------")


