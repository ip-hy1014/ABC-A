"""
問題文
トラックが 1 台あります。このトラックには合計で N キログラム以下の荷物を載せることができます。
このトラックに、1 個 W キログラムのレンガを最大でいくつ載せることができますか？
"""

n, w = map(int, input().split())
print(n//w)

"""
小数点切り捨て除算は//演算子を使用する。除算の結果（商）は 整数 となる。
"""