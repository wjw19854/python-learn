import unittest
from collections import deque

class CommonFuncitonTest(unittest.TestCase):
    """"常用功能演示
    
    文档常用格式,第一行为摘要,后面空一行,后面是详细介绍"""

    def test_range(self):
        a = ['Mary', 'had', 'a', 'little', 'lamb']
        for i in range(len(a)):
            print(i, a[i])

    def test_lambda(self):
        a = lambda x: x + 1
        self.assertEqual(7,a(6))

    # 函数标注
    def test_func_anno(self):
        def f(ham: str, eggs:str = 'egggs') -> str:
            print("函数定义:",f.__annotations__)
            print("参数:",ham,eggs)
            return ham + ' and ' + eggs
        with self.assertRaises(TypeError):
            # 会报类型错误
            f(1)
    
    # 列表
    def test_list(self):
        a = []
        # 增加元素
        a.append(1)
        self.assertCountEqual(a, [1])
        # 扩展列表
        a.extend([3, 4])
        self.assertCountEqual(a, [1,3,4])
        # 插入元素
        a.insert(len(a),5)
        self.assertCountEqual(a, [1,3,4,5])
        # 移除列表中第一个值为x的元素
        a.remove(5)
        self.assertCountEqual(a, [1,3,4])
        # 如果元素不存在则抛出异常
        with self.assertRaises(ValueError):
            a.remove(5)
        # 删除列表中给定位置的元素并返回它, 不传参数则返回最后一个
        last = a[len(a)-1]
        self.assertEqual(last, a.pop())
        # 移除列表所有元素
        self.assertEqual(None,a.clear())
        # index count sort reverse copy

    # 只是用append和pop 可以把列表做成一个栈来是用 列表的结构作为栈的时间复杂度为O(1)

    # 列表也可以作为队列是用,但是效率比较低.推荐是用deque
    def test_deque(self):
        queue = deque(["Eric", "John", "Michael"])
        queue.append("Terry")           # Terry arrives
        queue.append("Graham")          # Graham arrives
        self.assertEqual(queue.popleft(),"Eric")             # The first to arrive now leaves
        self.assertEqual(queue.popleft(),"John")                # The second to arrive now leaves
        self.assertEqual(queue,deque(['Michael', 'Terry', 'Graham'])) # Remaining queue in order of arrival

    # 列表推导式
    def test_tuidao(self):
        squares = []
        for x in range(10):
            squares.append(x**2)
        # 这里x仍然可以被访问
        self.assertEqual(x,9)
        target = squares
        # 用map创建
        squares = list(map(lambda x: x**2, range(10)))
        self.assertEqual(squares, target)
        # 用列表推导式
        squares = [ x**2 for x in range(10)]
        self.assertEqual(squares, target)
        # 两个列表笛卡尔积
        print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
        from math import pi
        print([str(round(pi, i)) for i in range(1, 6)]   )

    # del 语句
    def test_del(self):
        a = 1
        del a
        with self.assertRaises(UnboundLocalError):
            # 变量已经被删除
            print(a)
        a = [1,2,3]
        del a[0]
        self.assertEqual(a,[2,3])
        del a[:]
        self.assertEqual(a,[])
    
    # 集合 
    ## 集合是由不重复元素组成的无序的集
    def test_set(self):
        # 初始化集合
        a = set()
        a = {1,2,3,4,5,5}
        # 元素会被去重
        self.assertEqual(a, {1,2,3,4,5})
        # 差集运算
        b = a - {3,4,5}
        self.assertEqual(b,{1,2})
        # 差集
        a - b
        # 联合
        a | b 
        # 交集
        a & b
        # 对称查分
        a ^ b
        # 支持字典推导式
        { x for x in a if x >3}
    
    # 字典
    ## 字典的key为不可变对象 字符串 数字 和元组
    def test_dict(self):
        # 初始化字典
        tel = {}
        # 带变量初始化
        tel = {'jack': 4098, 'sape': 4139}
        # 新增键复制
        tel['guido'] = 4127
        # 删除键值对
        del tel['sape']
        # 转换为列表 所有的键转为列表
        list(tel)
        # 排序并转为列表
        sorted(tel)
        # 判断元素是否在字典
        self.assertTrue('guido' in tel)
        # 直接从键值对元组创建字典
        dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
        # 推导式创建字典
        {x: x**2 for x in (2, 4, 6)}
        # 当关键字是简单字符串时，有时直接通过关键字参数来指定键值对更方便
        dict(sape=4139, guido=4127, jack=4098)
    
    # 循环的技巧
    def test_for(self):
        # breakpoint()
        knights = {'gallahad': 'the pure', 'robin': 'the brave'}
        for k, v in knights.items():
            print(k, v)
        # enumerate() 取索引和关键字
        for k, v in enumerate(knights):
            print (k, v)
        # 当同时在两个或更多序列中循环时，可以用 zip() 函数将其内元素一一匹配。
        questions = ['name', 'quest', 'favorite color']
        answers = ['lancelot', 'the holy grail', 'blue']
        for q, a in zip(questions, answers):
            print('What is your {0}?  It is {1}.'.format(q, a))
        for i in reversed(range(1, 10, 2)):
            print(i)