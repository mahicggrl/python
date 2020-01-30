class SchollDetails():
    def __init__(self, first_class_strenth, second_class_strenth, teachers_strenth):
        pass
        self.first_class_strenth = first_class_strenth
        self.second_class_strenth = second_class_strenth
        self.teachers_strenth = teachers_strenth

    def student_details(self):
        print("First class Strenth is: ",self.first_class_strenth)
        print("Second class strenth is: ", self.second_class_strenth)


    def head_master_details(self):
        head_master = "nityanandha"
        return head_master

    def teacher_details(self):
        teacher_list = self.teachers_strenth
        return teacher_list


scholl_details = SchollDetails(26, 36, 5)
scholl_details.student_details()
scholl_details.teacher_details()

head_list = scholl_details.head_master_details()
print("Head Master Name is: ",head_list)

teacher_info = scholl_details.teacher_details()
print("Teachers Strenth is: ",teacher_info)


