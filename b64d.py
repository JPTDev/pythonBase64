from base64 import b64decode

while True:
	code = input("Base64 code (or close)  :  ")
	if code == 'close':
		break
	else:
		output = b64decode(code).decode('utf-8')
		print("\n\t", output, "\n")