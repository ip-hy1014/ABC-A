"""
問題文
1 以上 K 以下の正の整数から、偶数と奇数ひとつずつの組を選ぶ方法の個数を求めてください。なお、選ぶ順番は考慮しません。
"""

k = int(input())
if k % 2 == 0:
  print((k//2)*(k//2))
else:
  print(((k+1)//2)*(k//2))

#別解
print(int(input())**2//4)