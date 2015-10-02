import os
import re

############# CONFIG ##############

# the nth number in filename to pad
match_index = 0
# the padding you want to add. For 3, 1 becomes 001 and 99 becomes 099
pad_zeros = 3

###################################


path = input('Enter the full path of the folder whose contents you want to fix order: \n> ')
print()
fstr = '{:0' + str(pad_zeros) + 'd}'
store = {}

for i in os.listdir(path):
	nums = re.findall('\d+', i, re.DOTALL)
	newname = i.replace(nums[match_index], fstr.format( int(nums[match_index]) ), 1)
	print(i, '>>' , newname)
	store[i] = newname

opt = input('\nProceed with renaming (y/n) ?\n> ')
if opt.lower() == 'y':
	for i in store:
		os.rename(path + '/' + i, path + '/' + store[i])
	print('Renamed')