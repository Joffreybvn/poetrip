import unittest
from poetrip import PipFile


class TestPipfileMethods(unittest.TestCase):

    def test_instantiate_class(self):
        pipfile = PipFile()
        self.assertIsInstance(pipfile, PipFile)
