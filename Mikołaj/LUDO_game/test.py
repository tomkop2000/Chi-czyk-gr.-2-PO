class test_1():
    ziemniaczek = 1

class test_2():
    ziemniaczek = 1


a = test_1()
b = test_2()

c = type(a)


print(type(a))
print(type(b))



if isinstance(a, test_1):
    print("test_1")
if isinstance(b, test_2):
    print("test_2")