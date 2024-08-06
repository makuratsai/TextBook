import pandas as pd

def analyze_dataframe_新鳳鳴T棉_v5():
    file_name = 'import_file.xls'
    sheet_names = pd.ExcelFile(file_name).sheet_names
    combined_data = []

    for sheet in sheet_names:
        df = pd.read_excel(file_name, sheet_name=sheet)
        row, col = None, None
        
        # 尋找'序号'所在的位置
        for r in range(df.shape[0]):
            for c in range(df.shape[1]):
                if df.iat[r, c] == '序号':
                    row, col = r, c
                    break
            if row is not None:
                break
        
        # 取得68x7的範圍資料
        if row is not None and col is not None:
            data_range = df.iloc[row:row + 68, col:col + 7]
            combined_data.append(data_range)

    # 合併所有資料
    result = pd.concat(combined_data, ignore_index=True)
    print(result)

analyze_dataframe_新鳳鳴T棉_v5()