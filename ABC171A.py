"""
問題文
英大文字か英小文字のいずれか 1 文字 α が入力されます。
α が英大文字なら A、英小文字なら a と出力してください。
"""

α = input()
print("A" if α == α.upper() else "a")