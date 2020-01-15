## 最基础用法 参考testSimple.py

```
# 调用文件测试
python -m unittest unittest_play/testSimple.py -v
# 调用模块测试
python -m unittest unittest_play.testSimple
# 调用类名测试
python -m unittest  unittest_play.testSimple.TestStringMethods
# 调用具体测试方法
python -m unittest  unittest_play.testSimple.TestStringMethods.test_upper
```

其中simple.py中的
```
if __name__ == '__main__':
    unittest.main()
```
不是必须的

## 探索测试

```
cd project_directory
python -m unittest discover
```

discover 有以下选项：

-v, --verbose

    更详细地输出结果。

-s, --start-directory directory

    开始进行搜索的目录(默认值为当前目录 . )。

-p, --pattern pattern

    用于匹配测试文件的模式（默认为 test*.py ）。

-t, --top-level-directory directory

    指定项目的最上层目录（通常为开始时所在目录）。

## 断言列表

Method

Checks that

New in

assertEqual(a, b)

a == b

assertNotEqual(a, b)

a != b

assertTrue(x)

bool(x) is True

assertFalse(x)

bool(x) is False

assertIs(a, b)

a is b

3.1

assertIsNot(a, b)

a is not b

3.1

assertIsNone(x)

x is None

3.1

assertIsNotNone(x)

x is not None

3.1

assertIn(a, b)

a in b

3.1

assertNotIn(a, b)

a not in b

3.1

assertIsInstance(a, b)

isinstance(a, b)

3.2

assertNotIsInstance(a, b)

not isinstance(a, b)

3.2

>所有assert方法都接受一个msg参数，如果指定该参数，该参数将用作失败时的错误消息（另请参见longMessage）。请注意，仅当将msg关键字参数用作上下文管理器时，才可以将它们传递给assertRaises（）


也可以使用以下方法检查异常，警告和日志消息的产生：
Method

Checks that

New in


assertRaises(exc, fun, *args, **kwds)

fun(*args, **kwds) raises exc

assertRaisesRegex(exc, r, fun, *args, **kwds)

fun(*args, **kwds) raises exc and the message matches regex r

3.1

assertWarns(warn, fun, *args, **kwds)

fun(*args, **kwds) raises warn

3.2

assertWarnsRegex(warn, r, fun, *args, **kwds)

fun(*args, **kwds) raises warn and the message matches regex r

3.2

assertLogs(logger, level)

The with block logs on logger with minimum level

3.4

```
with self.assertLogs('foo', level='INFO') as cm:
   logging.getLogger('foo').info('first message')
   logging.getLogger('foo.bar').error('second message')
self.assertEqual(cm.output, ['INFO:foo:first message',
                             'ERROR:foo.bar:second message'])
```
还有其他用于执行更具体检查的方法，例如：

assertAlmostEqual(a, b)

round(a-b, 7) == 0

assertNotAlmostEqual(a, b)

round(a-b, 7) != 0

assertGreater(a, b)

a > b

3.1

assertGreaterEqual(a, b)

a >= b

3.1

assertLess(a, b)

a < b

3.1

assertLessEqual(a, b)

a <= b

3.1

assertRegex(s, r)

r.search(s)

3.1

assertNotRegex(s, r)

not r.search(s)

3.2

assertCountEqual(a, b)

a and b have the same elements in the same number, regardless of their order. a和b元素顺序可以不同,但是各个元素的个数必须相同

3.2

