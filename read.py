data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print("finished reading,", len(data), "reviews in total")

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print(sum_len/len(data), "words per review in average")

new = []
for d in data:
	if len(d) > 500:
		new.append(d)
print(len(new), "reviews longer than 500 words")

good = []
for d in data:
	if "good" in d:
		good.append(d)
print(len(good), "reviews mentioned good")













