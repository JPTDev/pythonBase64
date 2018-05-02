from base64 import b64decode, b64encode

while True:
	code = input("encode, decode or close  :  ")
	if code == 'close':
		break
	elif code == "encode":
		while True:
			encode_code = input("String to encode (or close)  : ")
			if encode_code == 'close':
				break
			else :
				output = b64encode(bytes(encode_code, 'utf-8'))
				decoded = output.decode("utf-8")
				print("\n\t", decoded, "\n")
	elif code == "decode":
		while True:
			decode_code = input("Base64 code to decode (or close)  :  ")
			if decode_code == 'close':
				break
			else:
				output = b64decode(decode_code).decode('utf-8')
				print("\n\t", output, "\n")
	else:
		print("Not a valid input : \n\t encode, decode or close")