"""
問題文
高橋君と青木君が野球をしています。高橋君はピッチャー、青木君はバッターです。
高橋君は消える魔球を投げることができます。高橋君が投げる消える魔球は、速さ Vm/s で等速直線運動をし、
投げた瞬間から T 秒後から S 秒後まで (両端を含む) 消えています。消えている間もボールは移動を続けます。
ボールが高橋君のもとからちょうど Dm 離れたときにボールが消えていないならば、青木君はボールを打つことができます。
消えているなら打つことはできません。
青木君は高橋君のボールを打つことができますか?

出力
青木君がボールを打つことができるなら Yes を、できないなら No を出力せよ。
"""

V, T, S, D = map(int, input().split())
print("No" if V*T <= D <= V*S else "Yes")

"""
ちょうど Dm 時点でボールが消えているか・いないかを判定する問題
ボールが消えるのは T秒後から S秒後まで、距離にすると V×Tm から V×Sm の間消えていて、それ以外では消えていない．
"""