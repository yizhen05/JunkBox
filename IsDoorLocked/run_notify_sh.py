import serial
import requests
import json

# WebフックURLを設定
WEBHOOK_URL = "https://kosenjp.webhook.office.com/webhookb2/8aaa7a61-f810-441c-a4fe-faa644a1204c@72fe835d-5e95-4512-8ae0-a7b38af25fc8/IncomingWebhook/a8ee212863534604ba3ba6fc9976a77c/101ee8dd-06c6-445c-aa21-c4293aebba40"

# ESP32とのシリアルポートを開く
ser = serial.Serial("/dev/ttyUSB0", 9600)  # '/dev/ttyUSB0'は適切なポートに置き換える

while True:
    # ESP32からのデータを読み取る
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print("Received:", data)

        # 受信したデータが指定された命令ならば、WebフックにPOSTリクエストを送信
        if data == "the key was Locked!!":
            payload = {"text": "the key was locked!!"}
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                WEBHOOK_URL, headers=headers, data=json.dumps(payload)
            )
            print("Response status code:", response.status_code)
            print("Response body:", response.text)
