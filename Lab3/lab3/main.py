from lab_serializer.serializers.serializer_factory import SerializerFactory
import math

'''def printdict(dictionary,tab=0):
    for key,value in dictionary.items():
        if isinstance(value,dict):
            print(' |'*tab,key)
            printdict(value,tab+1)
        else:
            print(' |'*tab,key,value)'''
'''

def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = SerializerFactory.get_serializer('json')

# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)

C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())



# f = C(1, 2)
# print(f.my_sin(11))
'''
def my_dec(func):
    def decorated(*args,**kwargs):
        length=len(args)+len(kwargs)
        if length>10:
            print("more than 10")
        else:
            print("less than 10")
        return func(args,kwargs)
    return decorated



@my_dec
def func(*args,**kwargs):
    ser = SerializerFactory.get_serializer(json)
    ser.dump(my_dec(func), file=open("file"))

func(1,2,3,4,5,6,7,8,9,10,11)
