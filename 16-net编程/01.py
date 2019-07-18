
import socket
def  serverFunc():
    # 1建立socket
    sock  =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr = ("127.0.1.1",7852)
    sock.bind( addr)


    data ,addr =sock.recvfrom(500)
    print(data)
    print(type(data))
    text =data.decode()
    print(type(text))
    print(text)
if __name__=="__main__":
    print("Starting server.....")
    serverFunc()
    print("Ending server.....")