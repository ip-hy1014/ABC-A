"""
問題文
あなたは、室温が 30 度以上のとき、またそのときに限り、冷房の電源を入れます。
今の室温は X 度です。冷房の電源を入れますか？

出力
冷房の電源を入れるならば Yes、入れないならば No を出力せよ。
"""

X = int(input())
print("Yes" if X >= 30 else "No")