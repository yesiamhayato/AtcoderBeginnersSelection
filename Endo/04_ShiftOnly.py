# 整数の入力
a = int(input())
# スペース区切りでリストに入れる
num_list = list(map(int, input().split()))
# 出力用カウンター
cnt = 0
# 無限ループ脱出用変数
judge = 0
while True:
	# リストの中身を一つずつ見ていき、偶数ではない場合for文をbreakし、無限ループ脱出用変数をいじる
	for num in num_list:
		if num % 2 == 1:
			judge = 1
			break
	if judge == 1:
		break
	cnt+=1
	# リストの中身を全て2で割る
	num_list = list(map(lambda x: x/2, num_list))
print(cnt)