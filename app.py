import socket
import json
import client.utils as ut

name = ''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 50097)
sock.connect(server_address)

while True:
	name = input("Enter a nickname to start chatting : ")
	name_obj = ut.dict_to_bytes({'type': 'username', 'name': name})
	sock.sendall(str.encode(name_obj))
	
	response = sock.recv(4096)
	
	print("Response : ", response)
	response = json.loads(response)
	if response["status"] == 'success':
		name = response["name"]
		break
	else:
		print("Username already exists, please choose something else :(")

try:
	while True:
		msg = input(">> ")
		
		if msg == "quit()": raise KeyboardInterrupt
		
		ut.dict_to_bytes({'type': "message", "msg": msg})
		# msg = str.encode(json.dumps({'type': "message", "msg": msg}))
		# print('Sending {!r}'.format(msg))
		# sock.sendall(msg)
		
		data = ut.recvall(sock)
		print("Received Data : ", data)
		# amount_received = 0
		# amount_expected = len(msg)
	
		# while amount_received < amount_expected:
		# 	data = sock.recv(1024)
		# 	amount_received += len(data)
		# 	print('Received {!r}'.format(data))

except KeyboardInterrupt as ki:
	print("\nQuitting...\n")
	sock.close()

except socket.error as se:
	print("Socket Error Occured : ",se)
	sock.close()

except Exception as e:
	print("An Exception occured : ", e)
	sock.close()
