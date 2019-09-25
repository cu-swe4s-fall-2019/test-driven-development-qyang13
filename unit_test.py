import math_lib as ml
import data_viz as dv
import get_data as gd
import viz
import os
import random
import unittest
import statistics as stats

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
        self.assertRaises(ValueError, ml.list_mean, [1,2,"NA"])

    def test_list_mean_const_int(self):
        ary = [1,2,3,4,5]
        self.assertEqual(ml.list_mean(ary),stats.mean(ary))

    def test_list_mean_const_float(self):
        ary = [1.0,2.1,3.1,4.5,5.9]
        self.assertEqual(ml.list_mean(ary),stats.mean(ary))

    def test_list_mean_const_mix(self):
        ary = [1,2.1,3,4.5,5.9]
        self.assertAlmostEqual(ml.list_mean(ary),stats.mean(ary))

    def test_list_mean_rand(self):
        rand_ary = []
        for i in range(100):
            rand_ary.append(random.random())
        self.assertAlmostEqual(ml.list_mean(rand_ary),stats.mean(rand_ary))

    # Tests for list_stdev
    def test_list_stdev_none(self):
        self.assertRaises(ValueError, ml.list_stdev, None)

    def test_list_stdev_empty(self):
        self.assertRaises(ValueError, ml.list_stdev, [])

    def test_list_stdev_invalid_element(self):
        self.assertRaises(ValueError, ml.list_stdev, [1,2,"NA"])

    def test_list_stdev_const_int(self):
        ary = [1,2,3,4,5]
        self.assertAlmostEqual(ml.list_stdev(ary),stats.stdev(ary), places=0)

    def test_list_stdev_const_float(self):
        ary = [1.0,2.1,3.1,4.5,5.9]
        self.assertAlmostEqual(ml.list_stdev(ary),stats.stdev(ary), places=0)

    def test_list_stdev_const_mix(self):
        ary = [1,2.1,3,4.5,5.9]
        self.assertAlmostEqual(ml.list_stdev(ary),stats.stdev(ary), places=0)

    def test_list_stdev_rand(self):
        rand_ary = []
        for i in range(100):
            rand_ary.append(random.random())
        self.assertAlmostEqual(ml.list_stdev(rand_ary),stats.stdev(rand_ary), places=0)


if __name__ == '__main__':
    unittest.main()
