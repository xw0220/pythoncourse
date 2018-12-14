class Animal:
    name=None
    gender=None
    color=None
    master=None
    creater="baihu"

    def eat(self):
        print("{}在吃东西".format(self.name))
    def sleep(self,hour):
        print("{}每天睡{}个小时".format(self.name,hour))

tom=Animal()
jerry=Animal()
tom.name="Tom Clus"
tom.gender="male"
tom.color="white"
jerry.name="Jerry"
jerry.gender="female"
jerry.color="black"

jerry.sleep("forever")

tom.eat()
#Animal.eat(tom)