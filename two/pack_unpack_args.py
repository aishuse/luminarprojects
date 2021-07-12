def fun(a,b,c,d):
    print(a,b,c,d)
    print(a)
mylist=[1,2,3,4]
fun(*mylist)

def mysum(*mylist):
    print(*mylist)
mylist=[11,22,33,44,55,66,77,88,99]
mysum(*mylist)

def new(*abc):
    return min(*abc)
abc=[11,22,10,11]
print(new(*abc))

def fun1(a,b,c):
    print(a,b,c)
def fun2(*args):
    x=list(args)
    x[0]="amelia"
    x[1]="aamikutty"
    print(*x)
    fun1(*args)
fun2("hello","aishu","world")


#dictionary pack unpack

def dictfun(a,b,c):
    print(a,b,c)
dvalue={'a':78,'b':89,'c':96}
dictfun(**dvalue)

def dfun(**args):
    print(type(args))
    for key in args:
        print("%s is %s"%(key,args[key]))
dfun(name="aish",id='78',lang="python")

qw="dhfjk"
gh="jhwekf"
print("%s as %s"%(qw,gh))

