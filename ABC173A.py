"""
問題文
お店で N 円の商品を買います。
1000 円札のみを使って支払いを行う時、お釣りはいくらになりますか？
ただし、必要最小限の枚数の 1000 円札で支払いを行うものとします。
"""

N = int(input())
print(0 if N % 1000 == 0 else 1000-(N%1000))