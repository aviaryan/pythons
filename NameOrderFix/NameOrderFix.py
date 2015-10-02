import os
import re

############# CONFIG ##############

# the nth number in the filename to pad
match_index = 0
# the padding you want to add. For 3, 1 becomes 001 and 99 becomes 099
pad_zeros = 3

###################################


path = input('Enter the full path of the folder whose contents order you want to have fixed: \n> ')
print()
fstr = '{:0' + str(pad_zeros) + 'd}'
store = {}
pattern = re.compile('(\d+)')

for i in os.listdir(path):
	j = 0
	s,e = -1,-1
	for m in pattern.finditer(i):
		if j == match_index:
			item = m.group()
			s = m.start()
			e = m.end()
			break
		j+=1

	if s != -1:
		newname = i[:s] + fstr.format(int(item)) + i[e:]
		print(i, '>>', newname)
		store[i] = newname


opt = input('\nProceed with renaming (y/n) ?\n> ')
if opt.lower() == 'y':
	for i in store:
		os.rename(path + '/' + i, path + '/' + store[i])
	print('Renamed')