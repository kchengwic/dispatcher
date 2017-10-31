import unittest
from mock import *
from dispatcher.executor import *
from dispatcher.task import *

class TestExecutor(unittest.TestCase):
    tasks_file = '..\\tasks_file.txt'

    def test_execute_none(self):
        executor = Executor()
        tasks = None
        self.assertIsNone(executor.execute(tasks))

    def test_execute(self):
        executor = Executor()
        task_attr = ['filename=C:\\Users\\kcheng\\PycharmProjects\\first_project\\dummy_task2.py',
                     'frequency=1D', 'time=09:45', 'description=invalid time']
        mock_task = Task(task_attr)
        tasks = []
        tasks.append(mock_task)
        self.assertEqual(executor.execute(tasks=tasks), tasks)

    def test_execute_exception_none_task_list(self):
        executor = Executor()
        tasks = [1, 2, 3]
        self.assertRaises(AttributeError, executor.execute, tasks)

if __name__ == '__main__':
    unittest.main()