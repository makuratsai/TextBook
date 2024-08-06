from lib.gpt_helper import MyGPT
from lib.file_helper import save_to_file, generate_random_filename_with_timestamp
from lib.package_helper import install_package

helper = MyGPT()


issue = "讀取檔名為import_file.xls這份檔案裡面的資料,裡面有三個分頁,然後從每一個分頁裡面找出哪一格的值是[序号],然後從那一格開始向右向下68x7的範圍,把這個範圍的資料印出來,再把這三個分頁印出的資料合併成一次印出來"
function_name = "analyze_dataframe_新鳳鳴T棉_v5"

prompt = helper.PromptHelperForCodeGPT(issue, function_name)

code = helper.CodeGPT(prompt)

file_name = generate_random_filename_with_timestamp()
save_to_file(f'generate_record/{file_name}', code)


condition = True
counter = 0
while condition:
    counter = counter + 1
    print(f"Counter: {counter}")
    try:
        exec(code)
        condition = False

        # Save the code to auto_lib
        save_to_file(f'auto_lib/func_{function_name}.py', code)

    except Exception as e:
        print(e)
        if counter > 9:
            print("Counter is greater than 9. Exiting the loop.")
            break

        errorMessage = str(e)

        if 'Missing optional dependency' in errorMessage:
            print("Missing optional dependency detected.")
            pip_command = helper.PipGPT(errorMessage)
            print(pip_command)
            install_package(pip_command)
        else:
            code = helper.FixCodeGPT(code, str(e))
            file_name = generate_random_filename_with_timestamp()
            save_to_file(f'generate_record/{file_name}', code)


