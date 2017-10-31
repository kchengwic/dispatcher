import unittest
from mock import *
from dispatcher.notifier import *

class TestNotifier(unittest.TestCase):
    sp = SlackProxy()
    notifier = Notifier()

    def test_slack_proxy_rasie_wrong_token(self):
        self.assertRaises(Exception, SlackProxy, ('sdafhuayksdghfyaug',))

    def test_slack_proxy_get_channels(self):
        # the number of channels is 24 to date
        self.assertEqual(len(self.sp.get_channels()), 24)

    def test_slack_proxy_get_users(self):
        # the number of channels is 55 to date
        self.assertEqual(len(self.sp.get_users()), 55)

    def test_slack_proxy_get_single_user(self):
        self.assertEqual(self.sp.get_user_id_by_displayname('kcheng'), 'U7KV9V6FQ')

    def test_slack_proxy_get_single_channel(self):
        self.assertEqual(self.sp.get_channel_id_by_name('risk'), 'C0V76MRSN')

    def test_slack_proxy_post_message(self):
        text = 'Unit-test Testing'
        channel = 'U7KV9V6FQ'
        username = 'Dispatcher Unit Test'
        res = self.sp.post_message(text, channel, username)
        self.assertTrue(res['ok'])

    def test_notifier_notify_slack(self):
        text = 'Unit-test Testing'
        res = self.notifier.notify_slack(text, username='ke')
        self.assertTrue(res['ok'])

if __name__ == '__main__':
    unittest.main()