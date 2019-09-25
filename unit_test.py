import math_lib as ml
import data_viz as dv
import get_data as gd
import viz
import sys
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
    def test_read_stdin_col_invalid_file(self):
        sys.stdin = 'daa.txt'
        self.assertRaises(FileNotFoundError, gd.read_stdin_col, 3)

    def test_read_stdin_col_invalid_index(self):
        sys.stdin = 'data.txt'
        f = open("data.txt", "w")
        f.write("1\t2\t3\n2\t3\t4\n5\t6\t7\n")
        f.close()
        self.assertRaises(IndexError, gd.read_stdin_col, 6)

    def test_read_stdin_col_const(self):
        sys.stdin = 'data.txt'
        f = open("data.txt", "w")
        f.write("1\t2\t3\n2\t3\t4\n5\t6\t7\n")
        f.close()
        self.assertEqual(gd.read_stdin_col(0), [1, 2, 5])

    def test_read_stdin_col_rand(self):
        sys.stdin = 'data.txt'
        A = []
        for i in range(9):
            A.append(str(random.randint(1, 10)))
        f = open("data.txt", "w")
        f.write(A[0]+'\t'+A[1]+'\t'+A[2]+'\n')
        f.write(A[3]+'\t'+A[4]+'\t'+A[5]+'\n')
        f.write(A[6]+'\t'+A[7]+'\t'+A[8]+'\n')
        f.close()
        self.assertEqual(gd.read_stdin_col(0),
                         [int(A[0]), int(A[3]), int(A[6])])


class Test_Data_Viz(unittest.TestCase):
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
