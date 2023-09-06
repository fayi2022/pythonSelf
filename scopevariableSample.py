value=20
def scopeGlobaltest() :
    x=29
    print("value="+str(value))  #Here value is a global variable
    print("x="+str(x))
scopeGlobaltest()

def scopeLocaltest() :
    y=43
    value=30
    #value+=30
    print("value=" + str(value))  # Here value is a local variable
    print("y=" + str(y))
scopeLocaltest()

def operVariables() :
    s=value+20
    print("s=" + str(s))
operVariables()

def oper(a,b=2,c=4) :
    print('a=',a,'b=',b,'c=',c)
oper(33)



