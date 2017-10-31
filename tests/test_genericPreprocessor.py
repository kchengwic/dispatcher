import unittest
from dispatcher.genericPreprocessor import *
import threading, time

class TestGenericPreprocessor(unittest.TestCase):
    genericPreprocessor = GenericPreprocessor()

    def test_preprocess(self):
        tasks_file = '..\\tasks_file.txt'
        good_tasks, invalid_tasks = self.genericPreprocessor.preprocess(tasks_file)
        self.assertEqual(2, len(good_tasks))

    def test_preprocess_invalid_tasks(self):
        tasks_file = '..\\tasks_file.txt'
        good_tasks, invalid_tasks = self.genericPreprocessor.preprocess(tasks_file)
        self.assertEqual(3, len(invalid_tasks))

    def test_preprocess_exception_invalid_input_file(self):
        tasks_file = 'usdhafuhsadih'
        self.assertRaises(IOError, self.genericPreprocessor.preprocess, tasks_file)

if __name__ == '__main__':
    unittest.main()