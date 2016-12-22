import unittest
import OutputString

class MyTestCase(unittest.TestCase):
    def test_something(self):
        per=OutputString.People();

        self.assertEqual(True, per.age == 20)


if __name__ == '__main__':
    myte =MyTestCase
    myte.test_something()
    unittest.main()
