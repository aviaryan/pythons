#!/usr/bin/env python3

import hashlib
from sys import argv

# FOR MD5, use inbuilt OS tool called md5sum


def run(file):
	if str(type(file)).find('list') > -1:
		for i in file:
			printHash(i)
	else:
		printHash(file)


def printHash(file):
	with open(file, "rb") as readfile:
		data = readfile.read()
		print(hashlib.sha256(data).hexdigest(), '*', file)


if __name__ == '__main__':
	if len(argv) > 1:
		run(argv[1:])
	else:
		print('File Name > ', end='')
		file = input()
		run(file)