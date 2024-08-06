import pandas as pd

# issue = "用pandas的dataframe讀取excel,檔名為import_file.xls這份檔案裡面的資料,然後找出哪一個欄位裡面的值是[序號],然後從那個欄位開始向右向下68x7的範圍,把這個範圍的資料印出來"

def analyze_dataframe_新鳳鳴T棉():
    # 讀取Excel檔案
    df = pd.read_excel('import_file.xls')

    # 找到'物料号'欄位的索引
    material_column = df.columns[df.isin(['序号']).any()]

    if not material_column.empty:
        column_index = material_column[0]

        # 取出從'物料号'欄位向右向下7x68的範圍
        start_row = df.index[df[column_index] == '序号'][0]
        data_range = df.iloc[start_row:start_row + 69, df.columns.get_loc(column_index):df.columns.get_loc(column_index) + 7]

        # 印出範圍的資料
        print(data_range)
    
analyze_dataframe_新鳳鳴T棉()