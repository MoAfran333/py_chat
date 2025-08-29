import json

# This function converts the data to be sent into bytes and finds the length.
# It returns a Tuple with first value being the length and the second being the data in bytes.
def dict_to_bytes(dict1):
    data = str.encode(json.dumps(dict1))
    data_len = len(data).to_bytes(4, 'big')
    return (data_len, data)

def bytes_to_dict():
    pass
    # return 


# This method should be invoked to call send data.
# It should get raw dictionary data and call the dict_to_bytes function and 
# send both the data and data_length...
def send_data(sock, data):
    data_len, bytes_data = dict_to_bytes(data)
    sock.sendall(data_len)
    sock.sendall(bytes_data)


# This function receives the first four bytes of data which has the length of the incoming message
# Then we loop until we get that set length of data
def recvall(sock):
    data_len = sock.recv(4, "big")

    amount_received = 0

    while amount_received < data_len:
        res = sock.recv(1024)
        amount_received += len(res)
        data += res
        # print('Received {!r}'.format(data))
    return data