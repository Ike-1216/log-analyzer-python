import pandas as pd

# ログCSVを読み込む
df = pd.read_csv("logs.csv")

# レベル別件数を集計
level_counts = df["level"].value_counts()

print("ログレベル別件数")
print(level_counts)

# CSVに出力
level_counts.to_csv("result.csv", header=["count"])
