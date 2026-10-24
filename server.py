import socket
import threading

# Server
HOST= '127.0.0.1'
PORT= 33333 

server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

#tracking nicknames and # of clients
clients=[]
names=[]

def sendingmessages(message):
    for client in list(clients):
        try:
            client.send(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            names.remove(name)
def handle_client(client):
    while True:
        try:
            message=client.recv(1024)
            if not message:
                raise Exception("Discontected")
            sendingmessages(message)
        except:
       if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                name=names[index]
                sendingmessages(f'{name} left the chat.'.encode('utf-8'))
                names.remove(name)
            break
def receive_con():
    print(f"server is running and listening on {HOST}:{PORT}")
    while True:
        client,address=server.accept()
        client.send('NICK_PROMPT'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)
        print(f'Nickname of user is {name}')
        sendingmessages(f"{name} joined the chat!".encode('utf-8'))
        client.send("Connected to the server successfully.\n".encode('utf-8'))
        thread=threading.Thread(target=handle_client,args=(client, ))
        thread.start()

if __name__=="__main__":
    receive_con()
        
