import socket

host = 'localhost'
port = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('This program can count sum/multiplicaton for two numbers or increment one number!\n')
while True:
	print('1. Count sum of two numbers\n'
		  '2. Count multiplicaton of two numbers\n' 
		  '3. Increment one number\n'
		  'To exit print: "exit"\n')

	var = input('Choose variant: ')
	if var == 'exit':
		client.sendto('shutdown'.encode('utf-8'), (host, port))
		break

	client.sendto(var.encode('utf-8'), (host, port))
	resp = client.recvfrom(1024)
	print(resp[0].decode('utf-8'))
	data = input()
	client.sendto(data.encode('utf-8'), (host, port))
	print(client.recvfrom(1024)[0].decode('utf-8'))
client.close()
'''name = input('Enter your name to send: ')

client.sendto(name.encode('utf-8'),(host,port))
receive = client.recvfrom(1024)

print(receive[0].decode('utf-8'))

client.close()'''
