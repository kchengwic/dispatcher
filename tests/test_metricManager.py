import unittest, sys, subprocess, datetime
from dispatcher.metricManager import *
from dispatcher.executor import *
from mock import *

class TestMetricManager(unittest.TestCase):

    def test_register(self):
        mock_task = Mock()
        metricManager = MetricManager()
        metricManager.register([mock_task])
        mock_task.basename.assert_called()

    def test_monitor(self):
        mock_task = Mock()
        metricManager = MetricManager()
        command = [sys.executable, '..\\dummy_task1.py']
        proc = subprocess.Popen(command)
        pid = proc.pid
        mock_task.pid.return_value = pid
        mock_task.basename.return_value = 'dummy_task1.py'
        mock_task.filename.return_value = '..\\dummy_task1.py'
        mock_task.execution_time.return_value = datetime.datetime.now()
        mock_task.is_running.side_effect = [True, False]
        mock_task.get_down_time.return_value = 1
        metricManager.register([mock_task])
        metricManager.monitor(mock_task)

    def test_monitor_exception_without_register(self):
        mock_task = Mock()
        metricManager = MetricManager()
        command = [sys.executable, '..\\dummy_task2.py']
        proc = subprocess.Popen(command)
        pid = proc.pid
        mock_task.pid.return_value = pid
        mock_task.basename.return_value = 'dummy_task2.py'
        mock_task.filename.return_value = '..\\dummy_task2.py'
        mock_task.execution_time.return_value = datetime.datetime.now()
        mock_task.is_running.side_effect = [True, False]
        mock_task.get_down_time.return_value = 1
        self.assertRaises(KeyError, metricManager.monitor, mock_task)

    def test_get_usage(self):
        mock_task = Mock()
        metricManager = MetricManager()
        command = [sys.executable, '..\\dummy_task1.py']
        proc = subprocess.Popen(command)
        pid = proc.pid
        mock_task.pid.return_value = pid
        mock_task.basename.return_value = 'dummy_task1.py'
        mock_task.filename.return_value = '..\\dummy_task1.py'
        timestamp = datetime.datetime.now()
        mock_task.execution_time.return_value = timestamp
        mock_task.is_running.side_effect = [True, False]
        mock_task.get_down_time.return_value = 1
        metricManager.register([mock_task])
        metricManager.monitor(mock_task)
        usage_dict = metricManager.get_usage(mock_task)
        self.assertEqual(len(usage_dict), 1)
        self.assertEqual(usage_dict.keys()[0], timestamp)

if __name__ == '__main__':
    unittest.main()