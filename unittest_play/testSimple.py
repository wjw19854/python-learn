"""
执行本脚本命令行:
python -m unittest  unittest_play.testSimple -v
"""
import unittest

class TestStringMethods(unittest.TestCase):

    def setUpClass():
        """类里面只执行一次"""
        print('setUpclass!===============')

    def tearDownClass():
        print('tearDownClass!===============')

    def setUp(self):
        """每个测试方法的前置,执行每个测试方法的时候都会执行
        若 setUp() 成功运行，无论测试方法是否成功，都会运行 tearDown() 。
        """
        print('setup!!!')

    def tearDown(self):
        """同setUP"""
        print('tearDown!!!')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @unittest.expectedFailure #预期失败
    def test_split_error(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world', 1])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    # def test_even(self):
    #     """
    #     Test that numbers between 0 and 5 are all even.
    #     """
    #     for i in range(0, 6):
    #         with self.subTest(i=i):  # subtest 可以执行每个小测试,而不是遇到第一个失败停下来
    #             self.assertEqual(i % 2, 0)


    @unittest.expectedFailure #预期失败
    def test_assertCountEqual(self):
        self.longMessage=True
        self.assertCountEqual('abc','bcd',"元素个数不同") # 这里a和d两个字母个数不同

    @unittest.expectedFailure
    def test_mast_fail(self):
        self.fail(msg="肯定失败")

    # 预期抛出指定异常
    def test_assert_excetprion(self):
        with self.assertRaises(ImportError) as cm:
            raise ImportError

if __name__ == '__main__':
    unittest.main()