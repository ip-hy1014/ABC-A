"""
問題文
縦 A ヤード、横 B ヤードの畑がある.
農夫ジョンは, 畑の内部に, 畑の上端と下端を結ぶ縦方向の幅 1 ヤードの道, 畑の左端と畑の右端を結ぶ横方向の幅 1 ヤードの道を作った. 畑は下図のようになっている. (灰色の部分が道)
さて, 道を除いた畑の面積は, 何平方ヤードだろうか? 求めなさい.
"""

a,b = map(int, input().split())
print(a*b-a-b+1)