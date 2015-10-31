from platform import subprocess
import os

##############################################
################### CONFIG ###################

# Identifier are substrings without which name of video file is same as name of audio file. It doesn't matter if there extensions are different.
# Example
# [WebM 480p] Some Video Series Ep 1.webm
# [WebM Audio] Some Video Series Ep 1.webm
video_identifier = '[WebM 480p]'
audio_identifier = '[WebM Audio]'

# The extension of the merged file
output_ext = 'mkv'

#############################################
#############################################


path = input('Path to the folder :\n> ')
dic = {}

for i in os.listdir(path):
	ti = i[0:i.rfind('.')] # remove extension
	reduced = ''
	if ti.find(video_identifier) != -1:
		reduced = ti.replace(video_identifier, '')
	if ti.find(audio_identifier) != -1:
		reduced = ti.replace(audio_identifier, '')
	if reduced == '': # if different file
		continue
	if not reduced in dic:
		dic[reduced] = []
	dic[reduced].append(i)

# got the pairs, now merge them

for i in dic:
	if len(dic[i]) == 2:
		subprocess.call([
			'ffmpeg',
			'-i', dic[i][0],
			'-i', dic[i][1],
			'-c:v', 'copy',
			'-c:a', 'copy',
			i.strip() + '.' + output_ext
			], cwd=path)

# done
# now delete source files

confirm = input('#################\nDelete source files (y/n) ?').lower()

if confirm == 'y':
	for i in dic:
		if len(dic[i]) == 2:
			os.remove(path + '/' + dic[i][0])
			os.remove(path + '/' + dic[i][1])