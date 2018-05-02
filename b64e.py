from base64 import b64encode

while True:
	code = input("String to encode (or close)  :  ")
	if code == 'close':
		break
	else:
		output = b64encode(bytes(code, 'utf-8'))
		decoded = output.decode("utf-8")
		print("\n\t", decoded, "\n")