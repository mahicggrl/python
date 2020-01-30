class LoopingTest():
    def loopingTest1(self):
        print("Testing loops.......")
        record_count = 10

        for count1 in range(10):
            print("Testing count.......", str(count1))

        for tmp_list in ["raghu", 2345, "mohan", "4567", "bhanu", True]:
            print("Testing count...templist...." , str(tmp_list))

        while record_count <= 20:
            print ("Some Statements....")
            record_count += 1
            print (record_count)

    def testFunctionWithArguments(self, name, designation, age): #function/method with arguments
        print ("Employee Details............")
        print ("Name...........", name)
        print ("designation...........", designation)
        print ("Name...........", age)


loopTest = LoopingTest()
#loopTest.loopingTest1()

employee_name = "bhanu"
designation = "AWS Developer"
age = 26

loopTest.testFunctionWithArguments(employee_name, designation, age)

