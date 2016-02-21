from Crypto.Cipher import AES
import base64


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
		return base64.b64encode(obj.encrypt(msg))

	def decrypt(self, msg):
		'''
		msg - Encrypted string
		returns decrypted string in bytes
		'''
		obj = AES.new(self.key, AES.MODE_CFB, self.iv)
		return obj.decrypt(base64.b64decode(msg))


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
		print( MyAES(pwd).encrypt(msg).decode(encoding='utf-8', errors='ignore') )
	else:
		print( MyAES(pwd).decrypt(msg).decode(encoding='utf-8', errors='ignore') )


if __name__ == '__main__':
	run()