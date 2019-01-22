###  prettytable-----漂亮的表格输出
import prettytable as pt

## 按行添加数据
```
tb = pt.PrettyTable()
tb.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
tb.add_row(["Adelaide",1295, 1158259, 600.5])
tb.add_row(["Brisbane",5905, 1857594, 1146.4])
tb.add_row(["Darwin", 112, 120900, 1714.7])
tb.add_row(["Hobart", 1357, 205556,619.5])

print(tb)
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
+-----------+------+------------+-----------------+
```


## 按列添加数据
```
tb.add_column('index',[1,2,3,4])
print(tb)
+-----------+------+------------+-----------------+-------+
| City name | Area | Population | Annual Rainfall | index |
+-----------+------+------------+-----------------+-------+
|  Adelaide | 1295 |  1158259   |      600.5      |   1   |
|  Brisbane | 5905 |  1857594   |      1146.4     |   2   |
|   Darwin  | 112  |   120900   |      1714.7     |   3   |
|   Hobart  | 1357 |   205556   |      619.5      |   4   |
+-----------+------+------------+-----------------+-------+
```

## 使用不同的输出风格
```
tb.set_style(pt.MSWORD_FRIENDLY)
print('--- style：MSWORD_FRIENDLY -----')
print(tb)

tb.set_style(pt.PLAIN_COLUMNS)
print('--- style：PLAIN_COLUMNS -----')
print(tb)
```
## 随机风格，每次不同
```
tb.set_style(pt.RANDOM)
print('--- style：MSWORD_FRIENDLY -----')
print(tb)

tb.set_style(pt.DEFAULT)
print('--- style：DEFAULT -----')
print(tb)
```
```
--- style：MSWORD_FRIENDLY -----
| City name | Area | Population | Annual Rainfall |
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
--- style：PLAIN_COLUMNS -----
City name        Area        Population        Annual Rainfall        
 Adelaide        1295         1158259               600.5             
 Brisbane        5905         1857594               1146.4            
  Darwin         112           120900               1714.7            
  Hobart         1357          205556               619.5             
--- style：MSWORD_FRIENDLY -----
@    Adelaide     1295     1158259     600.5 @
@    Brisbane     5905     1857594     1146.4@
@     Darwin      112       120900     1714.7@
@     Hobart      1357      205556     619.5 @
--- style：DEFAULT -----
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
+-----------+------+------------+-----------------+
```

## 不打印，获取表格字符串
```
s = tb.get_string()
print(s)
```

## 可以只获取指定列或行
```
s = tb.get_string(fields=["City name", "Population"],start=1,end=4)
print(s)

+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
+-----------+------+------------+-----------------+
+-----------+------------+
| City name | Population |
+-----------+------------+
|  Brisbane |  1857594   |
|   Darwin  |   120900   |
|   Hobart  |   205556   |
+-----------+------------+
```

## 自定义表格输出样式
### 设定左对齐
```
tb.align = 'l'
```
### 设定数字输出格式
```
tb.float_format = "2.2"
```
### 设定边框连接符为'*"
```
tb.junction_char = "*"
```
### 设定排序方式
```
tb.sortby = "City name"
```
### 设定左侧不填充空白字符
```
tb.left_padding_width = 0
print(tb)

*----------*-----*-----------*----------------*
|City name |Area |Population |Annual Rainfall |
*----------*-----*-----------*----------------*
|Adelaide  |1295 |1158259    |600.50          |
|Brisbane  |5905 |1857594    |1146.40         |
|Darwin    |112  |120900     |1714.70         |
|Hobart    |1357 |205556     |619.50          |
*----------*-----*-----------*----------------*
```
## 不显示边框
```
tb.border = 0
print(tb)
```
## 修改边框分隔符
```
tb.set_style(pt.DEFAULT)
tb.horizontal_char = '+'
print(tb)
City name Area Population Annual Rainfall 
Adelaide  1295 1158259    600.50          
Brisbane  5905 1857594    1146.40         
Darwin    112  120900     1714.70         
Hobart    1357 205556     619.50          
+++++++++++++++++++++++++++++++++++++++++++++++++++
| City name | Area | Population | Annual Rainfall |
+++++++++++++++++++++++++++++++++++++++++++++++++++
| Adelaide  | 1295 | 1158259    | 600.50          |
| Brisbane  | 5905 | 1857594    | 1146.40         |
| Darwin    | 112  | 120900     | 1714.70         |
| Hobart    | 1357 | 205556     | 619.50          |
+++++++++++++++++++++++++++++++++++++++++++++++++++
```



## prettytable也支持输出HTML代码
```
s = tb.get_html_string()
print(s)
<table>
    <tr>
        <th>City name</th>
        <th>Area</th>
        <th>Population</th>
        <th>Annual Rainfall</th>
    </tr>
    <tr>
        <td>Adelaide</td>
        <td>1295</td>
        <td>1158259</td>
        <td>600.50</td>
    </tr>
    <tr>
        <td>Brisbane</td>
        <td>5905</td>
        <td>1857594</td>
        <td>1146.40</td>
    </tr>
    <tr>
        <td>Darwin</td>
        <td>112</td>
        <td>120900</td>
        <td>1714.70</td>
    </tr>
    <tr>
        <td>Hobart</td>
        <td>1357</td>
        <td>205556</td>
        <td>619.50</td>
    </tr>
</table>
```
## 使用copy方法复制对象
```
#tb.set_style(pt.DEFAULT)
tb.horizontal_char = '.'
tb2 = tb.copy()
tb.align  = 'l'
tb2.align = 'r'
print(tb)
print(tb2)
```
## 直接赋值，得到的是索引
```
tb.horizontal_char = '-'
tb.aliign = 'l'
tb3 = tb
tb3.align = 'r'
print(tb)
print(tb3)

+...........+......+............+.................+
| City name | Area | Population | Annual Rainfall |
+...........+......+............+.................+
| Adelaide  | 1295 | 1158259    | 600.50          |
| Brisbane  | 5905 | 1857594    | 1146.40         |
| Darwin    | 112  | 120900     | 1714.70         |
| Hobart    | 1357 | 205556     | 619.50          |
+...........+......+............+.................+
+...........+......+............+.................+
| City name | Area | Population | Annual Rainfall |
+...........+......+............+.................+
|  Adelaide | 1295 |    1158259 |          600.50 |
|  Brisbane | 5905 |    1857594 |         1146.40 |
|    Darwin |  112 |     120900 |         1714.70 |
|    Hobart | 1357 |     205556 |          619.50 |
+...........+......+............+.................+
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |    1158259 |          600.50 |
|  Brisbane | 5905 |    1857594 |         1146.40 |
|    Darwin |  112 |     120900 |         1714.70 |
|    Hobart | 1357 |     205556 |          619.50 |
+-----------+------+------------+-----------------+
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|  Adelaide | 1295 |    1158259 |          600.50 |
|  Brisbane | 5905 |    1857594 |         1146.40 |
|    Darwin |  112 |     120900 |         1714.70 |
|    Hobart | 1357 |     205556 |          619.50 |
+-----------+------+------------+-----------------+
```
