"""
問題文
競プロ幼稚園にはN
人の子供がいます。えび先生は、子供たちを一列に並べ、一人目にはキャンディーを1個,二人目には2個,...,
N人目にはN個あげることにしました。必要なキャンディーの個数の合計は何個でしょう?
"""

n = int(input())
print(n*(n+1)//2)