import pandas as pd

def analyze_dataframe_新鳳鳴T棉_v3():
    # 讀取 Excel 檔案
    xls = pd.ExcelFile('import_file.xls')
    
    # 儲存所有分頁的資料
    result_data = []

    # 遍歷所有分頁
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)

        # 找到 '序号' 欄位的索引
        row_num, col_num = None, None
        for i in range(len(df)):
            if '序号' in df.iloc[i, :].values:
                row_num = i
                col_num = df.columns.get_loc(df.iloc[i, :][df.iloc[i, :]== '序号'].index[0])
                break
        
        # 檢查是否找到 '序号'
        if row_num is not None and col_num is not None:
            # 取得 68x7 的範圍
            data_range = df.iloc[row_num:row_num + 69, col_num:col_num + 7]
            result_data.append(data_range)
    
    # 印出結果
    for data in result_data:
        print(data)

# 呼叫方法以顯示結果
analyze_dataframe_新鳳鳴T棉_v3()