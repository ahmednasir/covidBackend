import os
import json

root_dir = os.getcwd()
path = os.path.join(root_dir,"results.json")


class FAQController:

    def get_faq(self):
        try:
            with open(path) as f:
                data = json.load(f)
            return data
        except Exception as ex:
            print(ex)
            return {}