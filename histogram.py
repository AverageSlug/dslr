import matplotlib.pyplot

truc = [[],[],[],[]]
t = 0

with open("datasets/dataset_train.csv", "r") as f:
	data = f.readlines()
for line in data:
	x = line.split(',')
	if t == 1 and x[8]:
		if x[1] == "Gryffindor":
			truc[0].append(float(x[8]))
		elif x[1] == "Ravenclaw":
			truc[1].append(float(x[8]))
		elif x[1] == "Hufflepuff":
			truc[2].append(float(x[8]))
		elif x[1] == "Slytherin":
			truc[3].append(float(x[8]))
	else:
		t = 1
matplotlib.pyplot.hist(truc, bins=7)
matplotlib.pyplot.legend(['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin'])
matplotlib.pyplot.show()
