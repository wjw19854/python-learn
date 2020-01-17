"""
执行本脚本命令行:
python -m unittest  unittest_play.testMock -v
"""
import unittest
from unittest.mock import MagicMock, patch, call
import datetime


class ProductionClass:
    attribute_a = 0
    def method(self):
        return self.something(1, 2, 3)

    def something(self, a, b, c):
        pass

    def closer(self, something):
        something.close()

    def read_from_data_base(self):
        return [[1,2,3],[2,3,4]]

class MockClass:
    attribute_b = -1


class TestMock(unittest.TestCase):
    def test_simple_mock(self):
        a = ProductionClass()
        a.something = MagicMock()
        # 设定返回值
        a.something.return_value = 'aaa'
        b = a.method()
        # 判断是否被正确调用
        a.something.assert_called_once_with(1, 2, 3)
        # 返回值被模拟
        self.assertEqual(b, 'aaa')

    # 对象方法调用的mock
    def test_class_method_mock(self):
        real = ProductionClass()
        mock = MagicMock()
        real.closer(mock)
        # 验证了方法的调用
        mock.close.assert_called_with()


    # 模拟类 patch
    def test_calss_mock(self):
        mock_date = datetime.date(2009,1,17)
        with patch('datetime.datetime') as mock:
            mock.today.return_value = mock_date
            # 注意这里ProductionClass 已经被patch过了.所以下面的方法行为被替换了 --- 回到10年前
            result = datetime.datetime.today()
            self.assertEqual(result, mock_date)
    
    # mock命名
    def test_mock_name(self):
        mock = MagicMock(name='foo')
        print(mock )
        print(mock.dosomething())

    # 跟踪所有调用
    def test_track_call(self):
        mock = MagicMock()
        mock.method()
        mock.attribute.method(10, x=53)
        print(mock.mock_calls)
        # 预期调用序列
        expected = [call.method(), call.attribute.method(10, x=53)]
        self.assertEqual(expected, mock.mock_calls)

        # 注意可以跟踪子目录参数,但是不能跟踪上级方法调用参数
        mock.factory(important=True).deliver()
        expected = call.factory(important=False).deliver()
        self.assertEqual(expected, mock.mock_calls[-1]) # True 和False 无法判断是否相同


    # 设置返回值和属性
    def test_return_value_and_attribute(self):
        mock = MagicMock()
        mock.return_value = 3
        self.assertEqual(mock(), 3)
        mock1 = MagicMock()
        mock1 = MagicMock(return_value=4)
        self.assertEqual(mock1(), 4)
        

    # 用mock引发Exception
    def test_mock_raise_exception(self):
        mock = MagicMock(side_effect=Exception('模拟异常'))
        with self.assertRaises(Exception):
            mock()

    # 可迭代调用模拟
    def test_side_effect_functions_and_iterables(self):
        mock = MagicMock(side_effect=[0,1,2])
        for i in range(0,2):
            re = mock()
            self.assertEqual(re, i)

    # 模拟条件返回
    def test_mock_return_value_by_param(self):
        vals = {(1,2):1,(2,3):2}
        def side_effect(*args):
            return vals[args]
        mock = MagicMock(side_effect=side_effect)
        r1 = mock(1,2)
        r2 = mock(2,3)
        self.assertEqual(r1, 1)
        self.assertEqual(r2, 2)

    # 从已有类创建mock
    def test_create_mock_from_class(self):
        mock = MagicMock(spec=ProductionClass)
        with self.assertRaises(AttributeError):
            # 不存在的行为会报错
            mock.method_not_exists()


    # 从已有方法穿件mock
    def test_crate_mock_from_function(self):
        def f(a, b, c): pass
        mock = MagicMock(spec=f)
        mock(1,2,3)
        mock.assert_called_with(a=1,b=2,c=3)

    # Patch装饰器
    ## 装饰属性 作用域只在被装饰对象内
    @patch.object(ProductionClass, 'attribute_a', MockClass.attribute_b)
    def test_patch_decorators(self):
        self.assertIs(MockClass.attribute_b, ProductionClass.attribute_a)

    ## 装饰非当前命名空间下的
    @patch('sys.path',MockClass.attribute_b)
    def test_patch_decorators_2(self):
        import sys
        self.assertIs(MockClass.attribute_b, sys.path)

    ## patch 局部替换字典
    def test_patch_restore(self):
        a = {'key': 'value'}
        orgin = a.copy()
        with patch.dict(a, {'newkey': 'newvalue'}, clear=True):
            self.assertEqual(a, {'newkey': 'newvalue'})
        self.assertEqual(a, orgin)