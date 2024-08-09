
# pip install openai
from openai import OpenAI
import my_config


api_key = my_config.section['OPEN_AI']

class MyGPT:

    __model__ = "gpt-4o-mini"
    __advanced_model__ = "gpt-4o"

    def __init__(self):
        self.openai = OpenAI(api_key=api_key)

    def __extract_text_between_markers(self, text, start_marker, end_marker):
        start_index = text.find(start_marker)
        end_index = text.find(end_marker, start_index)

        if start_index != -1 and end_index != -1:
            start_index += len(start_marker)
            return text[start_index:end_index].strip()
        else:
            return "Markers not found in the text."

    def AskGPT(self, msg) -> str:
        completion = self.openai.chat.completions.create(
            model=self.__model__,
            frequency_penalty=0.5,
            messages=[
                {"role": "user", "content": f"{msg}"}
            ]
        )
        return completion.choices[0].message.content
    
    def PromptHelperWithoutExecuteForCode(self, issue, file_name) -> str:
        return f'{issue} 並將其存為一個方法名稱為{file_name},且不需要執行'
    
    def PromptHelperForCode(self, issue, file_name) -> str:
        return f'{issue} 並將其存為一個方法名稱為{file_name},並顯示結果'
    
    def PromptHelperForAnalysisExcelCode(self, issue, file_name, output_file_name) -> str:
        return f'資料來源檔案為{file_name}, {issue}, 並將其儲存為另一個檔案{output_file_name}'

    def CodeGPT(self, issue) -> str:
        completion = self.openai.chat.completions.create(
            model=self.__model__,
            frequency_penalty=2,
            messages=[
                {"role": "system", "content": "你是一個程式碼產生器,依據提示產生Python程式碼,且不使用try...except語句,並將程式碼以<<<<與>>>>包住"},
                {"role": "user", "content": f"{issue}"}
            ]
        )
        text = completion.choices[0].message.content
        return self.__extract_text_between_markers(text, "<<<<", ">>>>")
    
    def FixCodeGPT(self, code, errMessage) -> str:
        completion = self.openai.chat.completions.create(
            model=self.__model__,
            frequency_penalty=2,
            messages=[
                {"role": "system", "content": "你是一個程式碼修復機,收到有錯誤的程式碼後會修復程式碼,且不使用try...except語句,並將程式碼以<<<<與>>>>包住"},
                {"role": "user", "content": f"執行有問題的程式碼:{code} "},
                {"role": "user", "content": f"錯誤訊息如下:{errMessage} "}
            ]
        )
        text = completion.choices[0].message.content
        return self.__extract_text_between_markers(text, "<<<<", ">>>>")
    
    def PipGPT(self, msg) -> str:
        completion = self.openai.chat.completions.create(
            model=self.__model__,
            frequency_penalty=0.5,
            messages=[
                {"role": "system", "content": "pip指令產生器,依據訊息產生對應所需的pip安裝指令,並將指令以<<<<與>>>>包住"},
                {"role": "user", "content": f"{msg}"}
            ]
        )
        text = completion.choices[0].message.content
        return self.__extract_text_between_markers(text, "<<<<", ">>>>")

    def TranslateGPT(self, msg) -> str:
        completion = self.openai.chat.completions.create(
            model=self.__model__,
            frequency_penalty=0.5,
            messages=[
                {"role": "system", "content": "你是一個中文與英文的翻譯機,收到中文後會翻譯成英文,收到英文後會翻譯成中文"},
                {"role": "user", "content": f"{msg}"}
            ]
        )
        return completion.choices[0].message.content