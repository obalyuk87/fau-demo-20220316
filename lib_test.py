from lib import say_hello
import unittest

class LibTestCase(unittest.TestCase):

    def test_say_hello_function(self):
        answer = say_hello("Bob")
        expectedAnswer = "hello Bob"
        self.assertEqual(answer, expectedAnswer, "ensure name matches")
