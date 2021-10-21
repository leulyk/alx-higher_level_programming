#!/usr/bin/python3

""" Module to test rectangle.py """

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests the Rectangle class """
    def test_init(self):
        """ tests the constructor """
        self.assertEqual(Rectangle(5, 8).width, 5)
        self.assertEqual(Rectangle(5, 10).height, 10)
        self.assertEqual(Rectangle(1, 2, 3).x, 3)
        self.assertEqual(Rectangle(1, 2, 3, 4).y, 4)
        with self.assertRaises(TypeError):
            Rectangle('hello', 2)
        with self.assertRaises(TypeError):
            Rectangle(2, 'hello')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 'hello')
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 'hello')
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, -1)
        with self.assertRaises(ValueError):
            Rectangle(5, 5, -2)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 3, -4)

    def test_area(self):
        """ test the area method """
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_str(self):
        """ test the __str__ magic method """
        rect = Rectangle(5, 5, 1, 2)
        output = '[Rectangle] ({}) 1/2 - 5/5'.format(rect.id)
        self.assertEqual(rect.__str__(), output)

    def test_display(self):
        """ tests the display method """
        output1 = "##\n##\n##\n##"
