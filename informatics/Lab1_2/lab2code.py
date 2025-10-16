print("Введите сообщение: ", end = "")
msg = [int(i) for i in str(input())]

if len(msg)!=7:
    raise ValueError("Ожидалось другое сообщение")

def printTable(msg:list):
    print("КОД:", "".join([*map(str, msg)]), "СООБЩЕНИЕ: ", "".join([*map(str, [msg[2], msg[4], msg[5], msg[6]])]))
    print("|  r1  |  r2  |  i1  |  r3  |  i2  |  i3  |  i4  |")
    print("| ","   |  ".join([*map(str, msg)]), "  |")

def printAndCalcSyndroms(msg):
    r1, r2, i1, r3, i2, i3, i4 = msg
    s1 = r1 ^ i1 ^ i2 ^ i4
    s2 = r2 ^ i1 ^ i3 ^ i4
    s3 = r3 ^ i2 ^ i3 ^ i4
    bits = ["r1","r2","i1","r3","i2","i3","i4"]
    print("s1 = r1 ⊕ i1 ⊕ i2 ⊕ i4 =", r1, "^", i1, "^", i2, "^", i4, "=",  s1)
    print("s2 = r2 ⊕ i1 ⊕ i3 ⊕ i4 =", r2, "^", i1, "^", i3, "^", i4, "=", s2)
    print("s3 = r3 ⊕ i2 ⊕ i3 ⊕ i4 =", r3, "^", i2, "^", i3, "^", i4, "=", s3)
    syndr = "".join(map(str, [s1, s2, s3]))
    errNBit=int(syndr[::-1], base=2)
    if errNBit!=0:
        print(f"s = (s1, s2, s3) = {syndr}", "ошибка в бите: ", errNBit, f"- символ {bits[errNBit-1]} бит")
    else:
        print(f"s = (s1, s2, s3) = {syndr} - ошибок нет")
    return errNBit-1

def correctAndPrintMsg(msg, errBit):
    msg[errBit]=int(not msg[errBit])
    print("ПРАВИЛЬНЫЙ КОД:", "".join([*map(str, msg)]),  "ПРАВИЛЬНОЕ СООБЩЕНИЕ: ", "".join([*map(str, [msg[2], msg[4], msg[5], msg[6]])]))

printTable(msg)
errIndexBit = printAndCalcSyndroms(msg)
if errIndexBit>=0:
    correctAndPrintMsg(msg, errIndexBit)
else:
    print("Все верно!")