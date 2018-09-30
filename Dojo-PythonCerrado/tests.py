import unittest
from main import Brainfuck

class BrainfuckTests(unittest.TestCase):

  def setUp(self):
        self.bf = Brainfuck()

  def test_ret_inc_cell(self):
    program = '+'
    result = self.bf.brainfuck_program(program)
    self.assertEqual(result,1)


if __name__ == '__main__':
    unittest.main()
