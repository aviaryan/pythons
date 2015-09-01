import http.server
import socketserver
from subprocess import call
from platform import system
from sys import exit as sysexit


######## CONFIG

if system() == 'Windows':
	browser = ''
elif system() == 'Linux':
	browser = 'xdg-open'
elif system() == 'darwin':
	browser = 'open'
else:
	print('What OS ? Please add the browser manually')
	sysexit()

PORT = 8001

######## PROGRAM

def main():
	Handler = http.server.SimpleHTTPRequestHandler

	httpd = socketserver.TCPServer(("", PORT), Handler)
	qStr = browser + " http://localhost:" + str(PORT)

	if system() == 'Windows':
		call("start " + qStr , shell=True)
	elif system() == 'Linux':
		call(qStr)
	elif system() == 'darwin':
		call(qStr)
	else:
		call(qStr)

	print("serving at port", PORT)
	print("Use ^C to exit")
	httpd.serve_forever()


if __name__ == "__main__":
	main()