import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("server", 5000))

    city = input("都市入力：")
    client.send(city.encode("utf-8"))

    response = client.recv(1024).decode("utf-8")
    print("応答：", response)

    client.close()

if __name__ == "__main__":
    main()