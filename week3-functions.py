def sayGoodbye():
    print("see you later")
    

def sayHello(name):
    isMorning = True
    if (isMorning):
        print("good morning " + name + "!")
    else:
        print("hello " + name + "!")
    
    sayGoodbye()

sayHello("bruno")
sayHello("class")
# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()


def isGreater(x, y):
  return (x > y)

# print(isGreater(1,0)) #False
isGreater(1,0) #True