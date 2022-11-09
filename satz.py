class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(age)

    def func(self,satz,roman=4):
        print("hiii")    
        print(self.name ,self.age)    
        # print(roman)    
obj=myclass("satz", 2)
print(obj.name )        
print(obj.age )        
obj.func(2,3)       
