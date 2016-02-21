from Crypto.Cipher import AES


class MyAES():
	'''
	Simple AES encrpytion
	'''
	def __init__(self, pwd):
		self.key = ((pwd+pwd.lower()) * 8)[:16]
		self.iv = (pwd * 16)[:16]

	def encrypt(self, msg):
		'''
		msg - String message
		returns encrypted data in bytes
		'''
		obj = AES.new(self.key, AES.MODE_CFB, self.iv)
		return obj.encrypt(msg)

	def decrypt(self, msg):
		'''
		msg - Encrypted byte-string / List of integers / String representation of list of integers like [93, 43]
		returns string in utf-8
		'''
		obj = AES.new(self.key, AES.MODE_CFB, self.iv)
		return obj.decrypt( self.getBytesFromStringList(msg).decode(encoding='utf-8') )

	def getBytesFromStringList(self, msg):
		if str(type(msg)).lower().find('bytes') > -1: # is bytes
			return msg
		if str(type(msg)).lower().find('list') > -1: # is list of ints
			return bytes(msg)
		msg = msg[1:-1]
		ls = list( msg.split(',') )
		return bytes([int(i) for i in ls])


def run():
	print('Enter the password')
	print('> ', end='')
	pwd = input()

	print('Enter the message')
	print('> ', end='')
	msg = input()

	print('What you want to do ? e - encrypt, d - decrypt')
	print('> ', end='')
	what = input()

	if what.lower() == 'e':
		print( list(MyAES(pwd).encrypt(msg)) )
	else:
		print( MyAES(pwd).decrypt(msg) )


if __name__ == '__main__':
	run()