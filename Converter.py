import opencc

# 初始化 OpenCC 轉換器，設置為簡體轉繁體模式
converter = opencc.OpenCC('s2t')  # 's2t' 是簡體到繁體的轉換模式

# 簡體中文文本
simplified_text = "这是一个示例的简体中文文本。"

# 轉換為繁體中文
traditional_text = converter.convert(simplified_text)

print("繁體中文文本:", traditional_text)