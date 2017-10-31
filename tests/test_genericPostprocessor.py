import unittest
from dispatcher.genericPostprocessor import *
from mock import *

class TestGenericPostprocessor(unittest.TestCase):
    genericPostprocessor = GenericPostprocessor()

    @patch('dispatcher.genericPostprocessor.MetricManager')
    def test_postprocess(self, mock_metric_manager):
        good_tasks, invalid_tasks = [], []

        self.genericPostprocessor.metricManager = mock_metric_manager
        self.genericPostprocessor.postprocess(good_tasks, invalid_tasks)

        mock_metric_manager.register.assert_called_with(good_tasks)
        mock_metric_manager.monitor_all.assert_called()

if __name__ == '__main__':
    unittest.main()