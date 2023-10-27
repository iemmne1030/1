import os.path
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json

class action_name_month_year(Action):
    def name(self) -> Text:
        return "action_name_month_year"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        lt_month = int(tracker.get_slot("lt_month"))
        lt_year = int(tracker.get_slot("lt_year"))
        # lt_date = int(tracker.get_slot("lt_date"))

        print(lt_month)
        print(lt_year)

        # Lấy dữ liệu từ JSON hoặc nguồn dữ liệu khác
        file_path = os.path.join(os.path.dirname(__file__) , r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        filtered_events = []
        for event_data in json_data:
            month = event_data["month"]
            year = event_data["year"]
            # date = event_data["date"]

            if month == lt_month and year == lt_year:
                filtered_events.append(event_data)

        # Tiếp tục xử lý với danh sách sự kiện đã lọc
        if filtered_events:
            event_names = [event_data["name"] for event_data in filtered_events]
            ans = ", ".join(event_names)
            answer = "Trong tháng " + str(lt_month) + " năm " + str(lt_year) + " có công trình: " + ans
        else:
            answer = "Không có sự kiện nào trong tháng và năm được yêu cầu."

        dispatcher.utter_message(text=answer)

        return [SlotSet("lt_month", lt_month), SlotSet("lt_year", lt_year)]

class action_member_name(Action):
    def name(self) -> Text:
        return "action_member_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        lt_name = tracker.get_slot("lt_name")

        print(lt_name)
        print(type(lt_name))

        #đọc dữ liệu
        file_path = os.path.join(os.path.dirname(__file__), r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        filtered_events = []
        for event_data in json_data:
            name = event_data["id"]
            print(name)
            # year = event_data["year"]
            # date = event_data["date"]

            if lt_name == name:
                filtered_events.append(event_data)

        # Tiếp tục xử lý với danh sách sự kiện đã lọc
        if filtered_events:
            event_names = [event_data["member"] for event_data in filtered_events]
            ans = ", ".join(event_names)
            answer = "có bao nhiêu thành viên "  + ans

        else:
            answer = "Không có sự kiện nào trong tháng và năm được yêu cầu."

        dispatcher.utter_message(text=answer)

        return [SlotSet("lt_name", lt_name)]
