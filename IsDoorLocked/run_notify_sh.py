import serial
import subprocess

# ESP32とのシリアルポートを開く
ser = serial.Serial("/dev/ttyUSB0", 9600)  # '/dev/ttyUSB0'は適切なポートに置き換える

while True:
    # ESP32からのデータを読み取る
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        print("Received:", data)

        # 受信したデータが指定された命令ならば、シェルスクリプトを実行
        if data == "the key was Locked!!":
            subprocess.run(["./notice_post.sh"])
