"""
問題文
あなたは、X 円を持ってケーキとドーナツを買いに出かけました。
あなたはまずケーキ屋で 1 個 A 円のケーキを 1 個買いました。 次に、ドーナツ屋で 1 個 B 円のドーナツをできるだけたくさん買いました。
これらの買い物のあと手元に残っている金額は何円ですか。
"""

x,a,b = [int(input()) for _ in range(3)]
print((x-a)%b)