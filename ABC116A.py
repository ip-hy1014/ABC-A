"""
問題文
直角三角形 ABC があります。
∠ABC=90° です。
三角形 ABC の三辺の長さである |AB|,|BC|,|CA| が与えられるので、直角三角形 ABC の面積を求めて下さい。
ただし、三角形 ABC の面積は整数となることが保証されています。
"""

a,b,c = map(int, input().split())
print(a*b//2)