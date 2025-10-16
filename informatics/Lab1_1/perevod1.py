A = input() # число
B = int(input()) # его система
C = int(input()) # система в которую надо перевести

#from B to 10
l2n = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20}
n2l = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", 16:"G", 17:"H", 18:"I", 19:"J", 20:"K"}
            

def fromB_to_10(A:list, B):
    res = []
    print("FROM B to 10: ", end="")
    for i in range(len(A), 0, -1):
        n=A[len(A)-i]
        if A[len(A)-i] in l2n.keys():
            n = l2n[A[len(A)-i]]
        a=int(n)*(B**(i-1))
        print(f"{int(n)}*{(B)}**{(i-1)}", end="")
        if i!=1:
            print("+", end="")
        res.append(a)
    print(f"={sum(res)}")
    return sum(res)

res = fromB_to_10(A, B)

#from 10 to C
def fromA_to_C(A, C):
    n = A
    s = []
    
    print("FROM 10 to C: ", end="")
    while n>0:
        print(n, "/", C, "=", n//C, str(n%C))
        s.append(str(n%C))
        n=n//C
    print(s)
    s.reverse()
    print(s)
    print("".join(s))


def FracFromTo10()

fromA_to_C(res, C)