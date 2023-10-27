import pandas as pd
import json

excel_file ="cttn.xlsx"
df = pd.read_excel(excel_file)

# Chuyển đổi DataFrame sang định dạng JSON
json_data = df.to_json(orient="records", force_ascii=False, default_handler=str)

# Lưu dữ liệu JSON vào tệp
with open("cttn.json", "w", encoding="utf-8") as json_file:
    json_file.write(json_data)

output_file = "cttn.json"  # Tên tệp JSON sau khi được định dạng

# Đọc dữ liệu từ tệp JSON
with open("cttn.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

# Định dạng dữ liệu và lưu vào tệp mới
formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
with open(output_file, "w", encoding="utf-8") as json_output_file:
    json_output_file.write(formatted_json)

print("ok")