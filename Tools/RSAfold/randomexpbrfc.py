import socket

def receive_until(sock, delimiter):
    data = b""
    while not data.endswith(delimiter):
        data += sock.recv(1)
    return data

def main():
    # Подключение к серверу
    host = "challenge.nahamcon.com"
    port = 31458
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Получение приветственного сообщения и выбор опции 2
    receive_until(s, b"> ")
    s.sendall(b'2\n')

    # Получение значения n
    receive_until(s, b"> ")
    n = int(receive_until(s, b"\n").decode().strip())

    # Получение зашифрованного сообщения
    receive_until(s, b"> ")
    enc = receive_until(s, b"\n").decode().strip()
    enc = [int(c) for c in enc[1:-1].split(", ")]

    # Поиск значения e
    for i in range(500, 1001):
        if (pow(ord("f"), i, n) == enc[0]):
            e = i
            print(f"Found e: {e}")
            break

    # Расшифровка сообщения
    flag = ""
    for c in enc:
        for i in range(20, 128):
            if (pow(i, e, n) == c):
                flag += chr(i)
                print(f"Found char: {chr(i)}")
                break

    print(f"Recovered flag: {flag}")

    # Закрытие соединения
    s.close()

if __name__ == "__main__":
    main()
