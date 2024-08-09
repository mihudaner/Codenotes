class a:
    y =0
    def __init__(self):
        self.x=0


    def func(self):
        self.x=y


a1 = a()

a.y=10
print(a1.y)

a1.y=20
print(a1.y)

a.y=30
print(a1.y)