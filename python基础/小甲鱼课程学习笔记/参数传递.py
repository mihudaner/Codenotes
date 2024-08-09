def func3(a,b,c=1,*args,**argss):
    print(a,b,c)
    print(args,argss)
 
 
func3(1,2,3,4,5,6,7,d=5,e=6,f=7)



def func(a,b,c):
    print(a,b,c)
 
 

func(*[1,2,3])#将list中的元素当做元组的方式传递
func(*{'x':1,'y':2,'z':3})  #一个*只取字典中的变量名
func(**{'a':1,'b':2,'c':3}) #两个*（**）则代表的是取字典中的值作为实参