**Python技巧**
------


----------


#### 两条原则

* 当需要排序的时候,尽量设法使用内建 Python 列表的 sort 方法;
* 当需要搜索的时候,尽量设法使用内建的字典

#### list转换成字符串
	"\n".join(['first line', 'second line'])

#### 过滤序列里面不满足条件的元素
	a = [1, 2, 3, 4, 5]; filter(lambda x: x>5, a);   #>>> [3,4,5]

#### 对一个或多个序列的元素进行操作
	a1 = map(lambda x: x+'1',['a','b','c'])；
	a2 = map(lambda x: x+'2',['a','b','c'])；
	map(lambda x,y: x+y, a1, a2)；  #>>>  ['a1a2', 'b1b2', 'c1c2']

#### 对一个序列的元素进行迭操作（每次操作的结果将成为下一次的初始值）
	reduce(lambda x, y: x+y, [2, 3, 4], 1)   #>>> 10

#### 遇到有关“时间变化”或者“时间差”的问题,优先先考虑 datetime.timedelta
	import datetime;
	oneday = datetime.timedelta(1);#时间间隔为1天
	today = datetime.date.today(); 
	tomorrow = today + oneday

#### 将多个序列按索引值进行合并 
	zip([1, 2], [4, 5])     #>> [(1, 4), (2, 5)]
	zip([1, 2, 3], [4, 5])     #>> [(1, 4), (2, 5)] 按最短的序列进行合并

#### 给字典初始化并设置默认值
	d = dict();  
	d.setdefault('key', 'value');  #>>  {'key': 'value'}

#### Namedtuple：动态生成类

    import collections  
    # 生成一个Person类. 它拥有3个attrs, name, age, gender. 试试吧
    Person = collections.namedtuple('Person','name age gender',verbose=True)  