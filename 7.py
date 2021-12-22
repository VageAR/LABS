str1 = input()
str2 = input()
if not str1 or not str2:
	quit()
if  len(str1) > 10000 or  len(str2) > 10000:
	quit()
sdvig = 0
for i in range(len(str1)):
	if str2!=str1:
		str1 = str1[-1] +str1[:-1]
		sdvig += 1
if str1 == str2:
	print(sdvig)
else:
	print("-1")        
