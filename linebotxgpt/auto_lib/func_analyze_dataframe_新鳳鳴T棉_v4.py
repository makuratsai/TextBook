# issue = "讀取檔名為import_file.xls這份檔案裡面的資料,裡面有三個分頁,然後從每一個分頁裡面找出哪一格的值是[序号],然後從那一格開始向右向下68x7的範圍,把這個範圍的資料印出來,再把這三個分頁印出的資料合併成一次印出來"


import pandas as pd

def analyze_dataframe_新鳳鳴T棉_v4():
    # 讀取Excel檔案
    xls = pd.ExcelFile('import_file.xls')
    combined_data = []

    # 遍歷每一個分頁
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        
        # 找到「序号」的儲存格位置
        row_index, col_index = None, None
        for r in range(df.shape[0]):
            for c in range(df.shape[1]):
                if df.iat[r, c] == '序号':
                    row_index, col_index = r, c
                    break
            if row_index is not None:
                break

        # 從「序号」的儲存格開始印出68x7範圍的資料
        if row_index is not None and col_index is not None:
            range_data = df.iloc[row_index:row_index + 68, col_index:col_index + 7]
            combined_data.append(range_data)

    # 合併所有分頁的資料並印出
    final_data = pd.concat(combined_data, ignore_index=True)
    print(final_data)

# 執行方法
analyze_dataframe_新鳳鳴T棉_v4()