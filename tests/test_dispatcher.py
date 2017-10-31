import unittest
from dispatcher.dispatcher import *

class TestDispatcher(unittest.TestCase):

    # def test_run(self):
    #     self.assertTrue(self.dispatcher.run())

    def test_run_exception_wrong_task_file(self):
        tasks_file = 'wrongfile.txt'
        dispatcher = Dispatcher(tasks_file)
        self.assertRaises(Exception, dispatcher.run)

    def test_run_exception_null_preprocessor(self):
        tasks_file = '..\\tasks_file.txt'
        dispatcher = Dispatcher(tasks_file)
        dispatcher.preprocessor = None
        self.assertRaises(Exception, dispatcher.run)

if __name__ == '__main__':
    unittest.main()