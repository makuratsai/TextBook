from lib.gpt_helper import MyGPT
from lib.package_helper import install_package
import traceback

def exec_code(code, additional_globals=None):
    if additional_globals is None:
        additional_globals = {}
    exec_globals = globals().copy()
    exec_globals.update(additional_globals)
    exec(code, exec_globals)

def auto_generate_code(prompt):
        
    helper = MyGPT()

    code = helper.CodeGPT(prompt)

    condition = True
    counter = 0
    while condition:
        counter = counter + 1
        print(f"Counter: {counter}")
        try:
            exec_code(code)
            condition = False

        except Exception as e:
            print(e)
            traceback.print_exc()  # 打印完整的錯誤訊息
            if counter > 9:
                raise Exception("Counter is over 9 times, please check the code.")
                

            errorMessage = str(e) + traceback.format_exc()
            print(errorMessage)

            code = helper.FixCodeGPT(code, str(e))
                

