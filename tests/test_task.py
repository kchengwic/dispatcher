import unittest
from dispatcher.task import *
from mock import *

class TestTask(unittest.TestCase):
    def test_init(self):
        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=1D', 'time=09:45', 'description=invalid time']
        task = Task(task_attr)
        self.assertEqual(task.basename(), 'dummy_task2.py')
        self.assertEqual(task.frequency, str('1D').lower())
        self.assertEqual(task.filename, 'C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py')
        self.assertEqual(task.time, '09:45')
        self.assertTrue(task.is_good())

    def test_init_bad_invalid_filename(self):
        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\sadfsda.py',
                     'frequency=1D', 'time=09:45', 'description=invalid filename']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

        task_attr = ['filename=',
                     'frequency=1D', 'time=09:45', 'description=invalid filename']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

    def test_init_bad_invalid_time(self):
        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=1D', 'time=0ssss9:45', 'description=invalid time']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=1D', 'time=09:45:924355435', 'description=invalid time']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=1D', 'time=09924355435', 'description=invalid time']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

    def test_init_good_empty_time(self):
        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=1D', 'time=', 'description=']
        task = Task(task_attr)
        self.assertTrue(task.is_good())

    def test_init_bad_invalid_frequency(self):
        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=1Dhhhh', 'time=', 'description=invalid frequency']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=D', 'time=', 'description=invalid frequency']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=2S', 'time=', 'description=invalid frequency']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=', 'time=', 'description=invalid frequency']
        task = Task(task_attr)
        self.assertFalse(task.is_good())

    def test_init_good_zero_frequency(self):
        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=0minute', 'time=', 'description=invalid frequency']
        task = Task(task_attr)
        self.assertTrue(task.is_good())

if __name__ == '__main__':
    unittest.main()