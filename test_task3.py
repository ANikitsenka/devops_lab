from unittest import TestCase
import task3


class TestTask(TestCase):

    def test_convert(self):
        self.assertEqual(task3.convert(4, 1), ('100', '1'))

    def test_length(self):
        self.assertEqual(task3.length('100', '1'), (3, 1))

    def test_justice(self):
        self.assertEqual(task3.justice(3, 1, '100', '1'), ('100', '001'))

    def test_destination(self):
        self.assertEqual(task3.destination(4, 1, '100', '001'), 2)
