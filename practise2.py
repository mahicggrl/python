class Practice():
    global test_var
    test_var = 1
    def Test(self):

        for x in range(1, 50):
            if x % 3 == 0 or x % 5 == 0:
                continue
            print(x)
    def Test2(self, aa, bb):
        a = aa
        b = bb
        if a == b:
            print("a value is ", a)
        elif a > b:
            print("a value is", a)
        else:
            print("failed")

    def Test3(self):
        #i = 1
        global test_var

        while test_var <= 5:
            print(test_var)
            test_var += 1
    def Test4(self):
        i = 5
        if i % 2 == 0:
            print(i, " is even number")
        else:
            print(i, " is odd number")

result = Practice()
#result.Test()
#result.Test2(20, 30)
result.Test3()

