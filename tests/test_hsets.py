import sys
import unittest
import time
from random import randint

sys.path.insert(0, '../codeforce')
import teamscode_summer_21_H as app

LIM = 1000000

class Test_Task_H(unittest.TestCase):

    def test_calc(self):
        td1 = [1, 9, 2, 3, 3, 2, 5, 2, 9]
        res1 = 24
        self.assertEqual(res1, app.calc(td1))
        self.assertEqual(res1, app.calc_reference_solution(td1))

        td2 = [1, 9, 2, 3, 3, 2, 5, 2, 9, 1]
        res2 = 48
        self.assertEqual(res2, app.calc(td2))
        self.assertEqual(res2, app.calc_reference_solution(td2))

        
    def test_time(self):
        test_data = [randint(1, 10000) for x in range(LIM)]
        start = time.perf_counter()
        res = app.calc(test_data)
        stop = time.perf_counter()
        exec_time = stop - start
        print(f'\n\tTest with MP took {exec_time} sec')
        start = time.perf_counter()
        res = app.calc_reference_solution(test_data)
        stop = time.perf_counter()
        exec_time = stop - start
        print(f'\n\tReference solution took {exec_time} sec')
        


if __name__ == '__main__':
    unittest.main()
