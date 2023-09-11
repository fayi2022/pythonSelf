#Program to check the scope of a varible after using nonlocal and global keyword
def check_Scope() :
    def do_LocalTest() :
        test="local"
    def do_NonLocalTest() :
        nonlocal test
        test="nonlocal"
    def do_GlobalTest() :
        global test
        test="global"
    do_LocalTest()
    test="default"
    print("The value of test is "+test)
    do_NonLocalTest()
    print("The value of test after nonlocal is " + test)
    do_GlobalTest()
    print("The value of test after global is " + test)
check_Scope()
print("The value of test after main:"+test)