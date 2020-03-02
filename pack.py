import pickle
from os import walk

tree = walk('itysk')

data = {}
with open('itysk' + '.pkl', 'wb') as to:
	line_list = []
	for tup in tree:
		for address, dirs, files in tup:
				if '.' in adress:
						continue
				for file in files:
						path = adress + '/' + file
						print(path)
						with open(path, 'r') as cur:
								for line in cur:
										line_list.append(line)
						data[path] = line_list
	pickle.dump(data, to)
