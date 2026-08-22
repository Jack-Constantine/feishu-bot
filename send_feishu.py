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
        "每隔1分钟自动喜欢pp提醒中"
    )