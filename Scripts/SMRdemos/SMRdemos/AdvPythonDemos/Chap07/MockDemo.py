from unittest.mock import MagicMock, Mock, call
from unittest import TestCase

tester = TestCase()  # used for asserts


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):  # try removing the args ... :-)
        pass


# mock method Something

real = ProductionClass()
real.something = MagicMock(name="ProductionClass.something")
real.method()
real.something.assert_called_once_with(1, 2, 3)


# mock method parameter

class ProductionClass2:
    def closer(self, something):
        something.close()


real = ProductionClass2()
mock = Mock()
real.closer(mock)  # pass in mock object for something. Note no close() method

mock.close.assert_called_with()  # check that close() was called

# history of calls

mock = MagicMock()
mock.method1()
mock.method2(10, x=42)
expected = [call.method1(), call.method2(10, x=42)]
tester.assertTrue(mock.mock_calls == expected)

# set up simple return values and attributes

mock = Mock()
mock.x = 42
mock.y = 96
mock.return_value = "abc"
mock.method1.return_value = "def"

print("mock.x", mock.x)
print("mock.y", mock.y)
print("mock returns", mock())
print("mock.method1() returns", mock.method1())

# a more nested example

mock = Mock()
cursor = mock.connection.cursor.return_value
cursor.execute.return_value = ['foo']

# test call
result = mock.connection.cursor().execute("SELECT 1")
print(result)

expected = call.connection.cursor().execute("SELECT 1").call_list()
print(expected)
tester.assertSequenceEqual(mock.mock_calls, expected)

# now read the rest of the documentation!!