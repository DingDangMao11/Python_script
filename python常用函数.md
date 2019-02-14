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
