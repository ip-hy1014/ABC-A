"""
問題文
高橋君は，いつも頭の中に整数を 1 つ思い浮かべています．
はじめ，高橋君が思い浮かべている整数は 0 です．
これから，高橋君は + または - の記号を，あわせて 4 つ食べようとしています．
高橋君が + を食べると，思い浮かべている整数は 1 大きくなります．
一方，高橋君が - を食べると，思い浮かべている整数は 1 小さくなります．
高橋君が食べようとしている記号は，文字列 S で与えられます． S の i 文字目は，高橋君が i 番目に食べる記号です．
すべての記号を食べ終わった後，高橋君が思い浮かべている整数を求めてください．
"""

s = input()
print(s.count("+")-s.count("-"))

#別解
s = input()
ans = 0
for i in range(4):
  if s[i] == "+":
    ans += 1
  else:
    ans -= 1
print(ans)