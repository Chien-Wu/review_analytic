data = []
with open("reviews.txt") as f:
	for line in f:
		data.append(line)

wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] >= 1000000:
		print(word, wc[word])

while True:
	word = input("enter the word you want to search:")
	if word == "q":
		break
	elif word in wc:
		print("there are", wc[word], word, "in these reviews" )
	else:
		print("there is no", word, "in these reviews")



