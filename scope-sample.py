#Program to check the scope of a varible
def check_Scope() :
    def do_LocalTest() :
        test="local"
    def do_NonLocalTest() :
        test="nonlocal"
    def do_GlobalTest() :
        test="global"
    do_LocalTest()
    test="default"
    print("The value of test is "+test)
check_Scope()