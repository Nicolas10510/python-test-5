import unittest
from solution import *


# Place your tests here

class Test_Programmer(unittest.TestCase):

  def setUp(self):
    self.programmer = Programmer('Ivan', Positions.JUNIOR.value)


  def test_work(self):
    self.assertEqual(self.programmer.work(10), None)

  def test_rise(self):
    self.assertEqual(self.programmer.rise(), None)

  def test___give_salary(self):
    self.assertEqual(self.programmer.__give_salary(), None)


if __name__ == '__main__':
  unittest.main()
