import math

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mean = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
house = []
birthday = []
best_hand = []
arithmancy = []
astronomy = []
herbology = []
defense_against_the_dark_arts = []
divination = []
muggle_studies = []
ancient_runes = []
history_of_magic = []
transfiguration = []
potions = []
care_of_magical_creatures = []
charms = []
flying = []
line1 = 0

with open("datasets/dataset_train.csv", "r") as f:
	data = f.readlines()
print("		", end='')
for line in data:
	x = line.split(',')
	if line1 == 0:
		line1 = 1
		for i in range(len(x)):
			if i > 5:
				print("			" + x[i], end='')
	else:
		if x[1]:
			house.append(x[1])
			count[0] += 1
		if x[4]:
			birthday.append(x[4])
			count[1] += 1
		if x[5]:
			best_hand.append(x[5])
			count[2] += 1
		if x[6]:
			arithmancy.append(x[6])
			count[3] += 1
		if x[7]:
			astronomy.append(x[7])
			count[4] += 1
		if x[8]:
			herbology.append(x[8])
			count[5] += 1
		if x[9]:
			defense_against_the_dark_arts.append(x[9])
			count[6] += 1
		if x[10]:
			divination.append(x[10])
			count[7] += 1
		if x[11]:
			muggle_studies.append(x[11])
			count[8] += 1
		if x[12]:
			ancient_runes.append(x[12])
			count[9] += 1
		if x[13]:
			history_of_magic.append(x[13])
			count[10] += 1
		if x[14]:
			transfiguration.append(x[14])
			count[11] += 1
		if x[15]:
			potions.append(x[15])
			count[12] += 1
		if x[16]:
			care_of_magical_creatures.append(x[16])
			count[13] += 1
		if x[17]:
			charms.append(x[17])
			count[14] += 1
		if x[18]:
			flying.append(x[18])
			count[15] += 1
print("Count", end='')
for i in range(len(count)):
	if i > 2:
		print("				" + str(count[i]), end='')
print()
print("Mean		", end='')
for i in arithmancy:
	mean[0] += float(i)
mean[0] /= count[3]
print("		" + str(mean[0]), end='')
for i in astronomy:
	mean[1] += float(i)
mean[1] /= count[4]
print("		" + str(mean[1]), end='')
for i in herbology:
	mean[2] += float(i)
mean[2] /= count[5]
print("		" + str(mean[2]), end='')
for i in defense_against_the_dark_arts:
	mean[3] += float(i)
mean[3] /= count[6]
print("		" + str(mean[3]), end='')
for i in divination:
	mean[4] += float(i)
mean[4] /= count[7]
print("		" + str(mean[4]), end='')
for i in muggle_studies:
	mean[5] += float(i)
mean[5] /= count[8]
print("		" + str(mean[5]), end='')
for i in ancient_runes:
	mean[6] += float(i)
mean[6] /= count[9]
print("		" + str(mean[6]), end='')
for i in history_of_magic:
	mean[7] += float(i)
mean[7] /= count[10]
print("		" + str(mean[7]), end='')
for i in transfiguration:
	mean[8] += float(i)
mean[8] /= count[11]
print("		" + str(mean[8]), end='')
for i in potions:
	mean[9] += float(i)
mean[9] /= count[12]
print("		" + str(mean[9]), end='')
for i in care_of_magical_creatures:
	mean[10] += float(i)
mean[10] /= count[13]
print("		" + str(mean[10]), end='')
for i in charms:
	mean[11] += float(i)
mean[11] /= count[14]
print("		" + str(mean[11]), end='')
for i in flying:
	mean[12] += float(i)
mean[12] /= count[15]
print("		" + str(mean[12]))
print("Std			", end='')
std = 0
for i in arithmancy:
	std += (float(i) - mean[0]) * (float(i) - mean[0])
std /= count[3]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in astronomy:
	std += (float(i) - mean[1]) * (float(i) - mean[1])
std /= count[4]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in herbology:
	std += (float(i) - mean[2]) * (float(i) - mean[2])
std /= count[5]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in defense_against_the_dark_arts:
	std += (float(i) - mean[3]) * (float(i) - mean[3])
std /= count[6]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in divination:
	std += (float(i) - mean[4]) * (float(i) - mean[4])
std /= count[7]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in muggle_studies:
	std += (float(i) - mean[5]) * (float(i) - mean[5])
std /= count[8]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in ancient_runes:
	std += (float(i) - mean[6]) * (float(i) - mean[6])
std /= count[9]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in history_of_magic:
	std += (float(i) - mean[7]) * (float(i) - mean[7])
std /= count[10]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in transfiguration:
	std += (float(i) - mean[8]) * (float(i) - mean[8])
std /= count[11]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in potions:
	std += (float(i) - mean[9]) * (float(i) - mean[9])
std /= count[12]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in care_of_magical_creatures:
	std += (float(i) - mean[10]) * (float(i) - mean[10])
std /= count[13]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in charms:
	std += (float(i) - mean[11]) * (float(i) - mean[11])
std /= count[14]
print("		" + str(math.sqrt(std)), end='')
std = 0
for i in flying:
	std += (float(i) - mean[12]) * (float(i) - mean[12])
std /= count[15]
print("		" + str(math.sqrt(std)))
print("Min		", end='')
tmp = [eval(i) for i in arithmancy]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in astronomy]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in herbology]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in defense_against_the_dark_arts]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in divination]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in muggle_studies]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in ancient_runes]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in history_of_magic]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in transfiguration]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in potions]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in care_of_magical_creatures]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in charms]
tmp.sort()
print("			" + str(tmp[0]), end='')
tmp = [eval(i) for i in flying]
tmp.sort()
print("			" + str(tmp[0]))
print("25%		", end='')
tmp = [eval(i) for i in arithmancy]
tmp.sort()
print("			" + str(tmp[int(count[3] / 4 - 1)]), end='')
tmp = [eval(i) for i in astronomy]
tmp.sort()
print("			" + str(tmp[int(count[4] / 4 - 1)]), end='')
tmp = [eval(i) for i in herbology]
tmp.sort()
print("			" + str(tmp[int(count[5] / 4 - 1)]), end='')
tmp = [eval(i) for i in defense_against_the_dark_arts]
tmp.sort()
print("			" + str(tmp[int(count[6] / 4 - 1)]), end='')
tmp = [eval(i) for i in divination]
tmp.sort()
print("			" + str(tmp[int(count[7] / 4 - 1)]), end='')
tmp = [eval(i) for i in muggle_studies]
tmp.sort()
print("			" + str(tmp[int(count[8] / 4 - 1)]), end='')
tmp = [eval(i) for i in ancient_runes]
tmp.sort()
print("			" + str(tmp[int(count[9] / 4 - 1)]), end='')
tmp = [eval(i) for i in history_of_magic]
tmp.sort()
print("			" + str(tmp[int(count[10] / 4 - 1)]), end='')
tmp = [eval(i) for i in transfiguration]
tmp.sort()
print("			" + str(tmp[int(count[11] / 4 - 1)]), end='')
tmp = [eval(i) for i in potions]
tmp.sort()
print("			" + str(tmp[int(count[12] / 4 - 1)]), end='')
tmp = [eval(i) for i in care_of_magical_creatures]
tmp.sort()
print("			" + str(tmp[int(count[13] / 4 - 1)]), end='')
tmp = [eval(i) for i in charms]
tmp.sort()
print("			" + str(tmp[int(count[14] / 4 - 1)]), end='')
tmp = [eval(i) for i in flying]
tmp.sort()
print("			" + str(tmp[int(count[15] / 4 - 1)]))
print("50%		", end='')
tmp = [eval(i) for i in arithmancy]
tmp.sort()
print("			" + str(tmp[int(count[3] / 2 - 1)]), end='')
tmp = [eval(i) for i in astronomy]
tmp.sort()
print("			" + str(tmp[int(count[4] / 2 - 1)]), end='')
tmp = [eval(i) for i in herbology]
tmp.sort()
print("			" + str(tmp[int(count[5] / 2 - 1)]), end='')
tmp = [eval(i) for i in defense_against_the_dark_arts]
tmp.sort()
print("			" + str(tmp[int(count[6] / 2 - 1)]), end='')
tmp = [eval(i) for i in divination]
tmp.sort()
print("			" + str(tmp[int(count[7] / 2 - 1)]), end='')
tmp = [eval(i) for i in muggle_studies]
tmp.sort()
print("			" + str(tmp[int(count[8] / 2 - 1)]), end='')
tmp = [eval(i) for i in ancient_runes]
tmp.sort()
print("			" + str(tmp[int(count[9] / 2 - 1)]), end='')
tmp = [eval(i) for i in history_of_magic]
tmp.sort()
print("			" + str(tmp[int(count[10] / 2 - 1)]), end='')
tmp = [eval(i) for i in transfiguration]
tmp.sort()
print("			" + str(tmp[int(count[11] / 2 - 1)]), end='')
tmp = [eval(i) for i in potions]
tmp.sort()
print("			" + str(tmp[int(count[12] / 2 - 1)]), end='')
tmp = [eval(i) for i in care_of_magical_creatures]
tmp.sort()
print("			" + str(tmp[int(count[13] / 2 - 1)]), end='')
tmp = [eval(i) for i in charms]
tmp.sort()
print("			" + str(tmp[int(count[14] / 2 - 1)]), end='')
tmp = [eval(i) for i in flying]
tmp.sort()
print("			" + str(tmp[int(count[15] / 2 - 1)]))
print("75%		", end='')
tmp = [eval(i) for i in arithmancy]
tmp.sort()
print("			" + str(tmp[int(count[3] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in astronomy]
tmp.sort()
print("			" + str(tmp[int(count[4] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in herbology]
tmp.sort()
print("			" + str(tmp[int(count[5] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in defense_against_the_dark_arts]
tmp.sort()
print("			" + str(tmp[int(count[6] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in divination]
tmp.sort()
print("			" + str(tmp[int(count[7] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in muggle_studies]
tmp.sort()
print("			" + str(tmp[int(count[8] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in ancient_runes]
tmp.sort()
print("			" + str(tmp[int(count[9] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in history_of_magic]
tmp.sort()
print("			" + str(tmp[int(count[10] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in transfiguration]
tmp.sort()
print("			" + str(tmp[int(count[11] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in potions]
tmp.sort()
print("			" + str(tmp[int(count[12] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in care_of_magical_creatures]
tmp.sort()
print("			" + str(tmp[int(count[13] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in charms]
tmp.sort()
print("			" + str(tmp[int(count[14] * 3 / 4 - 1)]), end='')
tmp = [eval(i) for i in flying]
tmp.sort()
print("			" + str(tmp[int(count[15] * 3 / 4 - 1)]))
print("Max		", end='')
tmp = [eval(i) for i in arithmancy]
tmp.sort()
print("			" + str(tmp[count[3] - 1]), end='')
tmp = [eval(i) for i in astronomy]
tmp.sort()
print("			" + str(tmp[count[4] - 1]), end='')
tmp = [eval(i) for i in herbology]
tmp.sort()
print("			" + str(tmp[count[5] - 1]), end='')
tmp = [eval(i) for i in defense_against_the_dark_arts]
tmp.sort()
print("			" + str(tmp[count[6] - 1]), end='')
tmp = [eval(i) for i in divination]
tmp.sort()
print("			" + str(tmp[count[7] - 1]), end='')
tmp = [eval(i) for i in muggle_studies]
tmp.sort()
print("			" + str(tmp[count[8] - 1]), end='')
tmp = [eval(i) for i in ancient_runes]
tmp.sort()
print("			" + str(tmp[count[9] - 1]), end='')
tmp = [eval(i) for i in history_of_magic]
tmp.sort()
print("			" + str(tmp[count[10] - 1]), end='')
tmp = [eval(i) for i in transfiguration]
tmp.sort()
print("			" + str(tmp[count[11] - 1]), end='')
tmp = [eval(i) for i in potions]
tmp.sort()
print("			" + str(tmp[count[12] - 1]), end='')
tmp = [eval(i) for i in care_of_magical_creatures]
tmp.sort()
print("			" + str(tmp[count[13] - 1]), end='')
tmp = [eval(i) for i in charms]
tmp.sort()
print("			" + str(tmp[count[14] - 1]), end='')
tmp = [eval(i) for i in flying]
tmp.sort()
print("			" + str(tmp[count[15] - 1]))
