import socket

host = 'localhost'
port = 8080
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)


while True:
	req = server.recvfrom(1024)
	print('Variant - {0}. From {1}'.format(req[0].decode('utf-8'), req[1]))
	if req[0].decode('utf-8') == '1':
		server.sendto('Please enter 2 numbers\n'.encode('utf-8'), req[1])
		data = server.recvfrom(1024)
		nums = data[0].decode('utf-8').split(' ')
		print(f'Received numbers: {nums}')
		summ = 0
		for i in nums:
			summ += int(i)
		ans = f'Your answer is {summ}\n'
		server.sendto(ans.encode('utf-8'), data[1])
	elif req[0].decode('utf-8') == '2':
		server.sendto('Please enter 2 numbers\n'.encode('utf-8'), req[1])
		data = server.recvfrom(1024)
		nums = data[0].decode('utf-8').split(' ')
		print(f'Received numbers: {nums}')
		mul = 1
		for i in nums:
			mul *= int(i)
		ans = f'Your answer is {mul}\n'
		server.sendto(ans.encode('utf-8'), data[1])
	elif req[0].decode('utf-8') == '3':
		server.sendto('Please enter 1 number\n'.encode('utf-8'), req[1])
		data = server.recvfrom(1024)
		num = int(data[0].decode('utf-8'))
		print(f'Received number: {num}')
		num += 1
		ans = f'Your answer is {num}\n'
		server.sendto(ans.encode('utf-8'), data[1])
	elif req[0].decode('utf-8') == 'shutdown':
		break
server.close()
'''while True:
	if input('If u want to exit print y: ') == 'y':
		break
	print('Enter your name: ')
	data = server.recvfrom(1024)
	if data[0] == '-1':
		break
	else:
		name = data[0].decode('utf-8')
		print(f'Hello, {name}!')
		server.sendto('Name received!'.encode('utf-8'), data[1])
server.close()'''
