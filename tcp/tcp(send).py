import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.0.25', 12348))  # 접속할 서버의 IP주소와 포트번호를 입력.
sock.send('Hello'.encode())  # 내가 전송할 데이터를 보냄.

try:
    while True:
        data = sock.recv(1024)  # 서버로부터 데이터를 받음.
        if not data:  # 만약 데이터가 없다면(연결이 끊어졌다면) break.
            break
        print("Received message: ", data.decode())  # 받은 데이터를 출력.
except KeyboardInterrupt:  # Ctrl+C를 눌렀을 때 예외를 처리함.
    print("Interrupted.")
finally:
    sock.close()  # 소켓을 닫음.
