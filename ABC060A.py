"""
問題文
文字列 A, B, C が与えられます。これがしりとりになっているか判定してください。
つまり、A の最後の文字と B の最初の文字が同じ
B の最後の文字と C の最初の文字が同じ
この 2 つが正しいか判定してください。

両方とも正しいならば YES、そうでないならば NO を出力してください。
"""

a,b,c = input().split()
print("YES" if a[-1]==b[0] and b[-1]==c[0] else "NO")