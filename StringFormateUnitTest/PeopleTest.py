import unittest
import OutputString

class PeopleTest(unittest.TestCase):


    def test_something(self):
        people = OutputString.People()
        self.assertEqual('kang.pang', people.name)


if __name__ == '__main__':
    peo =PeopleTest
    peo.test_something()

