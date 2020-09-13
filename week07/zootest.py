class Zoo(object):  
    def __init__(self,name):
        self.name = name
        self.animals=[]
    
    def add_animal(self,animal):
        if animal not in self.animals:
            self.animals.append(animal)
    
    def get_animal(self):
        return self.animals

class Animal():
    def __init__(self,eattype,size,character):
        self.eattype = eattype
        self.size = size
        self.character = character
        self.isFerocity = Animal.__is_ferocity(eattype,size,character)
    
    @staticmethod
    def __is_ferocity(eattype,size,character):
        if (size == '中' or size == '大') and eattype == '食肉' and character == '凶猛':
            return True
        else:
            return False
    
class Cat(Animal):
    _cry = '喵喵'
    def __init__(self,name,eattype,size,character):
        self.name = name
        super().__init__(eattype,size,character)
        self.isPet = not self.isFerocity
    def __str__(self):
        return f'名字:%s,类型:%s,体型:%s,性格:%s,是否凶猛动物:%s,是否宠物:%s'%(self.name,self.eattype,self.size,self.character,self.isFerocity,self.isPet)

class Dog(Animal):
    _cry = '旺旺'
    def __init__(self,name,eattype,size,character):
        self.name = name
        super().__init__(eattype,size,character)
        self.isPet = not self.isFerocity
    def __str__(self):
        return f'名字:%s,类型:%s,体型:%s,性格:%s,是否凶猛动物:%s,是否宠物:%s'%(self.name,self.eattype,self.size,self.character,self.isFerocity,self.isPet)

if __name__ == '__main__':
    z = Zoo('时间动物园')
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    dog1 = Dog('藏獒 1','食肉','大','凶猛')
    dog2 = Dog('法斗','食肉','小','凶猛')
    z.add_animal(cat1)
    z.add_animal(cat1)
    z.add_animal(dog1)
    z.add_animal(dog2)
    # 动物园是否有猫这种动物
    # have_cat = hasattr(z, 'Cat')
    for animal in z.get_animal():
        print(animal)