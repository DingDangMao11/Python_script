### 1.strip()方法:
```
strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
格式：
strip([chars]);
参数：
    chars -- 移除字符串头尾指定的字符序列。
```
```
#############案例############################
#!/usr/bin/python
# -*- coding: UTF-8 -*-
str = "00000003210Runoob01230000000"; 
print str.strip( '0' );  # 去除首尾字符 0

str2 = "   Runoob      ";   # 去除首尾空格
print str2.strip();
#以上实例输出结果如下：
3210Runoob0123
Runoob
```
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
str = "123abcrunoob321"
print (str.strip( '12' ))  # 字符序列为 12
以上实例输出结果如下：
3abcrunoob3
```
### 2. append()函数:
```
append() 方法用于在列表末尾添加新的对象。
```
###  3.zip() 函数:
```
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
zip 语法：
zip([iterable, ...])
```
```
实例
以下实例展示了 zip 的使用方法：
```
```
Python2中：
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)
print(zipped)
# 输出结果：
[(1, 4), (2, 5), (3, 6)]
```
```
Python3中：
a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b)
print(zipped)
输出结果：
<zip object at 0x02B01B48> #返回的是一个对象
# 打包为元组的列表
#使用list()函数转换为列表
print(list(zipped))
# 输出结果：
[(1, 4), (2, 5), (3, 6)]
```
