class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

p1 = Person("John",36)

print(p1.name)
print(p1.age)


a=1

b=2

try:
    soma=a+b
    print(soma)
    
except:
    print ("erro")