import matplotlib.pyplot

truc = [[],[],[],[]]
machin = [[],[],[],[]]
t = 0

with open("datasets/dataset_train.csv", "r") as f:
	data = f.readlines()
for line in data:
	x = line.split(',')
	if t == 1 and x[13] and x[14]:
			if x[1] == "Gryffindor":
				truc[0].append(float(x[13]))
				machin[0].append(float(x[14]))
			elif x[1] == "Ravenclaw":
				truc[1].append(float(x[13]))
				machin[1].append(float(x[14]))
			elif x[1] == "Hufflepuff":
				truc[2].append(float(x[13]))
				machin[2].append(float(x[14]))
			elif x[1] == "Slytherin":
				truc[3].append(float(x[13]))
				machin[3].append(float(x[14]))
	else:
		t = 1
matplotlib.pyplot.scatter(truc[0], machin[0], alpha=0.2)
matplotlib.pyplot.scatter(truc[1], machin[1], alpha=0.2)
matplotlib.pyplot.scatter(truc[2], machin[2], alpha=0.2)
matplotlib.pyplot.scatter(truc[3], machin[3], alpha=0.2)
matplotlib.pyplot.legend(['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin'])
matplotlib.pyplot.show()
