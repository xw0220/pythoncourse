class Animal:
    def __init__(self,name,gender,color,master,creater):
        self.name=name
        self.gender=gender
        self.color=color
        self.__master=master#私有成员
        self.creater=creater
    def eat(self):
        print("{}在吃东西".format(self.name))
    def sleep(self,hour):
        print("{}每天睡{}个小时".format(self.name,hour))
    def set_master(self,master_name):
        self.__master=master_name
    def show_master(self):
        print("{}的主人是{}".format(self.name,self.__master))

class Cat(Animal):
    def maimeng(self):
        print("猫会卖萌")
class Dog(Animal):
    def quanfei(self):
        print("犬吠")
tom=Cat("Tom Clus","male","white","baihu","baihu")
goffy=Dog("Goffy","female","black","baihu","baihu")
tom.maimeng()
goffy.quanfei()
tom.sleep(5)
goffy.eat()

