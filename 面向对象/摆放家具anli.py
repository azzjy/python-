class House(object):
    def __init__(self,area,addr):
        self.__area = area
        self.__addr = addr
        self.containerItem = []

    def addItem(self,item):
        needArea = item.getUsedArea()
        if self.__area > needArea:
            self.containerItem.append(item)
            self.__area -= needArea
            print('家具摆放成功')
        else:
            print(f'由于家具的面积{item.getUsedArea()}大于房间的剩余面积{self.__area},所以无法摆放此家具')
    def __str__(self):
        msg = '房子地址'+self.__addr+',房子的面积为:'+str(self.__area)+',房子的剩余面积'+str(self.__area)+'家具有'
        if len(self.containerItem) > 0:
            for i in self.containerItem:
                msg +=i.getName()+ ','
            msg = msg.strip(', ')
        else:
            msg += '暂无家具'
        return msg



class Bed(object):
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def getName(self):
        return self.name
    def getUsedArea(self):
        return self.area
newHouse = House(100,'深圳市宝安区')

#print(newHouse)


newBed = Bed('席梦思',30)
newBed1 = Bed('餐桌',50)
newHouse.addItem(newBed)
newHouse.addItem(newBed1)

print(newHouse)