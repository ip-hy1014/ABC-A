"""
問題文
3 行 3 列の正方形状のマス目があり、各マスには英小文字が書かれています。 上から i 行目、左から j 列目のマスに書かれた文字は、cij です。
マス目の左上と右下を結ぶような対角線上のマス目に書かれた文字を、左上から順に読んでできる 3 文字の文字列を出力してください。
"""

a,b,c = [input() for _ in range(3)]
print(a[0]+b[1]+c[2])