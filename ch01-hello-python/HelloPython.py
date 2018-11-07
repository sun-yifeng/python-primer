name = input("Please input your name:")
# 打印输出有下面三种方法，最常用的是第一种
print("hello {0}".format(name))
print("hello " + name)
print("hello %s" %name)

# 不加括号是2.x的语法
# print "hello"