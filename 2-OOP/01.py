'''
定义一个学生类，用来形容学生
'''


class Student():
    # 一个空类，pass代表直接跳过
    pass


# 定义一个对象
mingyue = Student()


# 定义一个类，用来描述听Python的学生
class PythonStudent():
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1.def doHomework 的缩进层级
    # 2.系统默认有一个self参数
    def doHomework(self):
        print("I 在做作业")
        # 推荐在函数的末尾使用return 语句
        return None

#  实例化一个叫yueyue的学生，是一个具体的人
yueyue =  PythonStudent()
yueyue.age = 20
yueyue.name ="yueyue"
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()
print(yueyue.__dict__)

sss
zzz


