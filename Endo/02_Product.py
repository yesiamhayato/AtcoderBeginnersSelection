#スペース区切りの整数入力
a, b = map(int, input().split())

if (a*b)%2 == 0:
	print("Even")
else:
	print("Odd")
