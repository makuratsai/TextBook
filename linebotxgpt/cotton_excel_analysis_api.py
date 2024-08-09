from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

from gptcycle_app import auto_generate_code

import pandas as pd

# def exec_code(code, additional_globals=None):
#     if additional_globals is None:
#         additional_globals = {}
#     exec_globals = globals().copy()
#     exec_globals.update(additional_globals)
#     exec(code, exec_globals)

def get_file_extension(file_name):
    # 使用 os.path.splitext 方法分離文件名和擴展名
    _, file_extension = os.path.splitext(file_name)
    return file_extension

def get_filename_without_extension(file_name):
    # 使用 os.path.splitext 方法分離文件名和擴展名
    file_name_without_extension = os.path.splitext(file_name)[0]
    return file_name_without_extension

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'json' not in request.form:
        return jsonify({"error": "Missing file or JSON data"}), 400
    
    file = request.files['file']
    json_data = request.form['json']

    # 將 JSON 字符串轉換為 Python 字典
    data = json.loads(json_data)

    # 取得json_data裡面的area_description_prompt的資料
    issue = data['area_description_prompt']

    supplier = data['supplier']
    
    # Save the uploaded file
    # file_path = os.path.join('uploads_temp', file.filename)
    # file_path = os.makedirs(os.path.dirname(file_path), exist_ok=True)
    temp_file_name = 'import_temp_excel' + get_file_extension(file.filename)
    file.save(temp_file_name)
    
    # Save the JSON data
    json_path = os.path.join('uploads_temp', 'data.json')
    with open(json_path, 'w') as json_file:
        json_file.write(json_data)
    
    # 檢查有沒有func_{supplier}.py這個檔案
    if os.path.exists(f'auto_lib/func_{supplier}.py'):
        return jsonify({"error": f"func_{supplier}.py already exists"}), 400

    try:
        auto_generate_code(issue, supplier, temp_file_name, 'output_file_name.csv')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "上傳成功"}), 200

if __name__ == '__main__':
    app.run(debug=True)
