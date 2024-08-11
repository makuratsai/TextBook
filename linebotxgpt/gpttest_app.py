from code_gpt_engine_helper import auto_generate_code


def test_auto_generate_code(issue):
    auto_generate_code(issue)

if __name__ == "__main__":
    issue = '請幫我產生一個猜數字的遊戲,0~9之間,猜對即結束,答案是7'
    test_auto_generate_code(issue)