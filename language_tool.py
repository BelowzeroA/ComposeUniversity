import json
import time
from urllib.request import Request, urlopen

class LanguageTool:

    def __init__(self):
        self.server_addr = "https://languagetool.org/api/v2/check"

    def compose_url(self):
        return self.server_addr

    def get_raw_result(self, text):
        try:
            url = self.compose_url()
            binary_data = ("text=" + text + "&language=en-US").encode('utf-8')
            request = Request(url, data=binary_data)
            raw_response = urlopen(request).read()
            return json.loads(raw_response.decode())
        except Exception as e:
            print(e)
            return None

    def get_check_summary(self, text):
        summary = {"spelling": 0, "grammar": 0, "style": 0}
        time.sleep(0.5)
        raw_result = self.get_raw_result(text)
        for match in raw_result["matches"]:
            msg = match["message"]
            if msg == "Possible spelling mistake found" or \
                msg.startswith("This word is normally"):
                summary["spelling"] += 1
            elif msg.startswith("Statistics suggests") or \
                msg.startswith("“Because” at the beginning") or \
                msg.startswith("Did you forget") or \
                msg.startswith("Use a comma before") or \
                "the third-person" in msg or \
                msg.startswith("Did you mean"):
                summary["grammar"] += 1
            elif msg.startswith("Three successive"):
                summary["style"] += 1
        return summary

    def get_check_summary_from_list(self, list_of_texts):
        result = []
        for text in list_of_texts:
            result.append(self.get_check_summary(text))
        return result

