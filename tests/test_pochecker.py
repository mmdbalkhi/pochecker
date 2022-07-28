from unittest import TestCase

from src.my_package import add2


class Add2Tests(TestCase):
    def test_it_works(self):
        """
        add2(1) should return 3.
        """
        self.assertEqual(add2(1), 3)
