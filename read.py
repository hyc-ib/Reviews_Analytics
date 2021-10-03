data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完成！總共有', len(data), '筆評論')

sum_len = 0
for d in data:
	sum_len += len(d)
print('評論的平均長度為:', sum_len/len(data), '個字')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆評論長度小於100')
print(new[0])
print(new[1])