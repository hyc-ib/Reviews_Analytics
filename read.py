data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成！總共有', len(data), '筆評論')

word_count = {}
for comment in data:
	words = comment.split(' ')
	for word in words:
		if word in word_count:
			wc[word] += 1
		else:
			wc[word] = 1
for word in word_count:
	if word_count[word] > 100:
		print(word, word_count[word])

while True:
	word = input('請輸入想搜尋的字: ')
	print(word, '出現過的次數為: ', word_count[word], '次')

sum_len = 0
for d in data:
	sum_len += len(d)
print('評論的平均長度為:', sum_len/len(data), '個字')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
# new = [d for d in data if len(d) < 100]
print('總共有', len(new), '筆評論長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
# good = [d for d in data if 'good' in d]
print('總共有', len(good), '筆評論提到good')
print(good[0])
print(good[1])