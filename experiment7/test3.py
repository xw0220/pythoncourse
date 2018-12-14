class Animal:
    name=None
    gender=None
    color=None
    __master=None#私有成员
    creater="baihu"
    def eat(self):
        print("{}在吃东西".format(self.name))
    def sleep(self,hour):
        print("{}每天睡{}个小时".format(self.name,hour))
    def set_master(self,master_name):
        self.__master=master_name
    def show_master(self):
        print("{}的主人是{}".format(self.name,self.__master))
tom=Animal()
tom.name="Tom Clus"
tom.set_master("baihu")
tom.show_master()
