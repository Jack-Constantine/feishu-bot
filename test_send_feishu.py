import os
import unittest

import requests

os.environ.setdefault("FEISHU_WEBHOOK", "https://example.invalid/webhook")

import send_feishu


class StopLoop(Exception):
    pass


class SendForeverTests(unittest.TestCase):
    def test_run_forever_sends_again_after_each_60_second_wait(self):
        sent_messages = []
        waits = []

        def send(text):
            sent_messages.append(text)

        def sleep(seconds):
            waits.append(seconds)
            if len(waits) == 2:
                raise StopLoop

        with self.assertRaises(StopLoop):
            send_feishu.run_forever("提醒消息", send=send, sleep=sleep)

        self.assertEqual(sent_messages, ["提醒消息", "提醒消息"])
        self.assertEqual(waits, [60, 60])

    def test_run_forever_retries_after_a_request_failure(self):
        attempts = []
        waits = []

        def send(text):
            attempts.append(text)
            if len(attempts) == 1:
                raise requests.RequestException("network unavailable")

        def sleep(seconds):
            waits.append(seconds)
            if len(waits) == 2:
                raise StopLoop

        with self.assertRaises(StopLoop):
            send_feishu.run_forever("提醒消息", send=send, sleep=sleep)

        self.assertEqual(attempts, ["提醒消息", "提醒消息"])
        self.assertEqual(waits, [60, 60])


if __name__ == "__main__":
    unittest.main()
