"""
問題文
高橋君はとあるWebサービスに会員登録しようとしています。
まずIDを S として登録しようとしました。しかし、このIDは既に他のユーザーによって使用されていました。
そこで、高橋君は S の末尾に 1 文字追加した文字列をIDとして登録することを考えました。
高橋君は新しくIDを T として登録しようとしています。これが前述の条件を満たすか判定してください。

出力
T が問の条件を満たすならば Yes と、そうでないならば No と出力せよ。
"""

s = input()
t = input()
print("Yes" if s == t[:-1] else "No")