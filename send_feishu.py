import os
import requests


FEISHU_WEBHOOK = os.environ["FEISHU_WEBHOOK"]


def send_message(text):

    payload = {
        "msg_type": "text",
        "content": {
            "text": text
        }
    }


    r = requests.post(
        FEISHU_WEBHOOK,
        json=payload,
        timeout=10
    )

    r.raise_for_status()


if __name__ == "__main__":
    send_message(
        "每天喜欢pp自动提醒中"
    )