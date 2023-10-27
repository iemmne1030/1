from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

class ActionGetEventInfo(Action):
    def name(self) -> Text:
        return "ask_name_month_year"

    def required(tracker: Tracker) -> List[Text]:
        return ["name","month", "year"]

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        event_month = tracker.get_slot("month")
        event_year = tracker.get_slot("year")

        if not event_month or not event_year:
            response = "Xin lỗi, tôi không thể tìm thông tin với tháng và năm bạn đã cung cấp."
        else:
            with open("cttn.json", "r") as json_file:
                data = json.load(json_file)

            response = self.ask_name_month_year(data, event_month, event_year)

        dispatcher.utter_message(text=response)

        return []

    def ask_name_month_year(self, data: List[Dict[str, Any]], month: int, year: int) -> str:
        matching_events = []

        for event in data:
            if event["month"] == month and event["year"] == year:
                matching_events.append(event["name"])
                event_list = ", ".join(matching_events)
                return f"Các công trình trong tháng {month} năm {year}: {event_list}"
            else:
                return f"Không có sự kiện nào trong tháng {month} năm {year}."

        # if matching_events:
        #     event_list = ", ".join(matching_events)
        #     return f"Các công trình trong tháng {month} năm {year}: {event_list}"
        # else:
        #     return f"Không có sự kiện nào trong tháng {month} năm {year}."