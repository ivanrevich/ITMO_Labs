def genFibbon(max:int)->list:
    out = [1, 1]
    while out[-1]<=max:
        out.append(out[-1]+out[-2])
    return [*(out[1:-1:]).__reversed__()]

def transToFib(num:int):
    if num==0:
        return [0], "0" 
    if num<0:
        return [], "negative numbers are not supported"
    l = genFibbon(num)
    a = num
    els = []
    out = " "
    for el in l:
        if out[-1]=="1":
            out+="0"
            continue
        if (a-el)>=0:
            a-=el
            els.append(el)
            out+="1"
        else:
            out+="0"
    return els, out[1::]

print("---------ПЕРЕВОДЧИК ИЗ 10-ричной системы в систему Фибоначчи---------")
print("Введите число: ", end="")
num10 = int(input())
els, out = transToFib(num10)
print("Это число в системе Фибоначчи: ", out)

print("---------------------------------------------------------------")