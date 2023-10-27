import os.path
import json

lt_name = "Vành đai xanh"
print(lt_name)
print(type(lt_name))

        #đọc dữ liệu
file_path = os.path.join(os.path.dirname(__file__), r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
with open(file_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)

for event in json_data:
    name = json_data("name")
    member = json_data("member")
    # event = []
    # for data in json_data:
    #     name = data["name"]
    #     member = data["member"]
    #     # event.append(name)

    ans = "không tìm thấy"
    if lt_name.lower() in name.lower() :
        ans =  "Có " + str(member)
        # break
    print(ans)
