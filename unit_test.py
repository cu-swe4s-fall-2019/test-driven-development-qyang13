import math_lib as ml
import data_viz as dv
import get_data as gd
import sys
import os
import random
import unittest
import statistics as stats
from io import StringIO


class Test_Math_Lib(unittest.TestCase):
    '''
    Unit tests for library math_lib
    '''
    # Tests for list_mean
    def test_list_mean_none(self):
        self.assertRaises(ValueError, ml.list_mean, None)

    def test_list_mean_empty(self):
        self.assertRaises(ValueError, ml.list_mean, [])

    def test_list_mean_invalid_element(self):
        self.assertRaises(ValueError, ml.list_mean, [1, 2, "NA"])

    def test_list_mean_const_int(self):
        ary = [1, 2, 3, 4, 5]
        self.assertEqual(ml.list_mean(ary), stats.mean(ary))

    def test_list_mean_const_float(self):
        ary = [1.0, 2.1, 3.1, 4.5, 5.9]
        self.assertEqual(ml.list_mean(ary), stats.mean(ary))

    def test_list_mean_const_mix(self):
        ary = [1, 2.1, 3, 4.5, 5.9]
        self.assertAlmostEqual(ml.list_mean(ary), stats.mean(ary))

    def test_list_mean_rand(self):
        rand_ary = []
        for i in range(100):
            rand_ary.append(random.random())
        self.assertAlmostEqual(ml.list_mean(rand_ary), stats.mean(rand_ary))

    # Tests for list_stdev
    def test_list_stdev_none(self):
        self.assertRaises(ValueError, ml.list_stdev, None)

    def test_list_stdev_empty(self):
        self.assertRaises(ValueError, ml.list_stdev, [])

    def test_list_stdev_invalid_element(self):
        self.assertRaises(ValueError, ml.list_stdev, [1, 2, "NA"])

    def test_list_stdev_const_int(self):
        ary = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(ml.list_stdev(ary), stats.stdev(ary), places=0)

    def test_list_stdev_const_float(self):
        ary = [1.0, 2.1, 3.1, 4.5, 5.9]
        self.assertAlmostEqual(ml.list_stdev(ary), stats.stdev(ary), places=0)

    def test_list_stdev_const_mix(self):
        ary = [1, 2.1, 3, 4.5, 5.9]
        self.assertAlmostEqual(ml.list_stdev(ary), stats.stdev(ary), places=0)

    def test_list_stdev_rand(self):
        rand_ary = []
        for i in range(100):
            rand_ary.append(random.random())
        self.assertAlmostEqual(ml.list_stdev(rand_ary),
                               stats.stdev(rand_ary), places=0)


class Test_Get_Data(unittest.TestCase):
    '''
    Unit tests for get_data
    '''
    def test_read_stdin_col_no_input(self):
        sys.stdin = None
        self.assertRaises(ValueError, gd.read_stdin_col, 0)

    def test_read_stdin_col_invalid_column(self):
        sys.stdin = StringIO('1\t2\n3\t4\n5\t6\n')
        self.assertRaises(IndexError, gd.read_stdin_col, 2)

    def test_read_stdin_col_const(self):
        sys.stdin = StringIO('1\t2\n3\t4\n5\t6\n')
        self.assertEqual(gd.read_stdin_col(1), [2, 4, 6])


class Test_Data_Viz(unittest.TestCase):
    '''
    Unit tests for library data_viz
    '''
    def test_boxplot(self):
        A = []
        for i in range(1000):
            A.append(random.randint(1, 500))
        dv.boxplot(A, 'boxplot.png')
        self.assertTrue(os.path.exists('boxplot.png'))

    def test_histgram(self):
        A = []
        for i in range(1000):
            A.append(random.randint(1, 500))
        dv.histogram(A, 'histogram.png')
        self.assertTrue(os.path.exists('histogram.png'))

    def test_combo(self):
        A = []
        for i in range(1000):
            A.append(random.randint(1, 500))
        dv.combo(A, 'combo.png')
        self.assertTrue(os.path.exists('combo.png'))


if __name__ == '__main__':
    unittest.main()
