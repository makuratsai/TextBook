import pandas as pd

def analyze_dataframe_新鳳鳴T棉_v2():
    # 讀取Excel檔案
    df = pd.read_excel('import_file.xls')

    # 找到包含'序号'的欄位位置
    start_row, start_col = None, None
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            if df.iloc[row, col] == '序号':
                start_row, start_col = row, col
                break
        if start_row is not None:
            break

    # 取得68x7的範圍
    if start_row is not None and start_col is not None:
        data_range = df.iloc[start_row:start_row + 68, start_col:start_col + 7]
        print(data_range)
    else:
        print("未找到'序号'")

# 顯示結果
analyze_dataframe_新鳳鳴T棉_v2()