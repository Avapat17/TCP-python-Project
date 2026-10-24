import socket
import threading
import sys
#! TO BE DONE- ADD IT SO YOU CAN QUIT WITH THE QUIT COMMAND
#! ADD READ ME
#! DOUBLE CHECK THE THINGS YOU WERE READING WAS FOR PYTHON 3 SINCE YOU'VE RARELY CODED IN PYTHON
name=input("Chose your Name: ")

HOST= '127.0.0.1'
PORT= 33333 

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

def receivemsgs():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message=='NICK_PROMPT':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
                print(" disconecting")
                client.close()
                break
def writemesg():
    while True:
        try:
            userinput = input("")
            if userinput.lower() in ['quit', 'exit']:
                try:
                    client.send(f'{name}:{userinput}'.encode('utf-8'))
                except:
                    pass
                client.close()
                sys.exit()
            
            message = f'{name}:{userinput}'
            client.send(message.encode('utf-8'))
        except:
            client.close()
            break
receive_thread = threading.Thread(target=receivemsgs)
receive_thread.start()

write_thread = threading.Thread(target=writemesg)
write_thread.start()

