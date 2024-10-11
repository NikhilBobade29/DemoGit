class A:
    def __init__(self,id,name,city):
        self.id = id
        self.name = name
        self.city = city

    def show(self):
         print("Id:",self.id)
         print("Name:",self.name)
         print("City:",self.city)

class B(A):
    def __init__(self,id,name,city, sal,pan):
        super().__init__(id,name,city)
        self.sal = sal
        self.pan = pan


    def show(self):
        super().show()
        print("Sal:", self.sal)
        print("Pan:", self.pan)


obj =B(101,'nikhil','pune','78456','XQP789')
obj.show()

