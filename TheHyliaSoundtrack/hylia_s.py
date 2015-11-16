from bs4 import BeautifulSoup
from urllib.request import urlopen
from platform import subprocess


# if genlist = 0, then this script downloads the files, the cmd_downloader variable comes into play
# if genlist = 1, then this script generates a list.txt file containing direct links in the working directory
# the list.txt can be imported in any download managers like IDM , FDM etc to download all files at once with full speed
genlist = 1
cmd_downloader = 'aria2c -x 8 -s 8 -k 3M'



def run():
	url = input('url of soundtrack album \n> ')
	response = urlopen(url)
	data = response.read()
	soup = BeautifulSoup(data, 'lxml') # HTML.parser fails, smart technique hylia
	# open('list.html', 'w').write(data.decode())
	getsongs( soup.body.find_all('a') )


def getsongs( tds ):

	downlist = ''
	cur = 1

	for i in tds:
		link = i['href']
		if not ismp3(link):
			continue
		# download song
		response = urlopen(link)
		songdata = response.read()
		songsoup = BeautifulSoup(songdata, 'lxml')
		links = songsoup.body.find_all('a')
		for dlink in links:
			if not ismp3(dlink['href']):
				continue
			print('Downloading song #' + str(cur))
			if genlist:
				downlist += dlink['href'] + '\n'
			else:
				subprocess.call(cmd_downloader + ' ' + dlink['href'])
			break # ehh

		cur += 1

	if genlist:
		open('list.txt', 'w').write(downlist)



def ismp3(link):
	if len(link) < 5:
		return False
	if link[-4:] != '.mp3':
		return False
	return True


if __name__ == '__main__':
	run()