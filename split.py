import pandas as pd

# ✅ Corrected path
input_file = r"E:\vedant\DA-intern-task--main\output\phase6_statistical_analysis\merged_trader_sentiment.csv"

chunksize = 40000  # adjust if needed
for i, chunk in enumerate(pd.read_csv(input_file, chunksize=chunksize)):
    chunk.to_csv(f"split_part_{i+1}.csv", index=False)
    print(f"Created split_part_{i+1}.csv with {len(chunk)} rows")
