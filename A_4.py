# работа по алгоритмам
#1
print("4ast 1")
k=int(input("vvedite 4islo: "))
def bin(n,it):
    if n//2!=0:
       # print(n%2)
        a=n%2
        it = str(a) + it
        if n//2==1:
           # print(n//2)
            a = n // 2
            it = str(a)+it
            print(it, " b bin")
        bin(n//2, it)
bin(k,it="")

#2
print("4ast 2")
n=int(input("vvedite 1 mnoxetel: "))
m=int(input("vvedite 2 mnoxetel: "))

def umn(n1,m1,it):
    if m1>0:
        it=it+n1
        m1-=1
        umn(n1, m1,it)
    else:
        print("rezult: ", it)
umn(n,m,it=0)

#3
print("4ast 3")
u=int(input("vvedite 4islo: "))
s=int(input("vvedite stepen: "))
def step(n1,m1,it):
    if m1>0:
        it=it*n1
        m1-=1
        step(n1, m1,it)
    else:
        print("rezult: ", it)
step(u,s,it=1)