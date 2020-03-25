import requests, json
from config import resuts
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/"

class GetRecentData:

    def scrap(self):
        try:
            model = resuts.prev_results()
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')

            table = soup.find_all("table")[0]

            table_body = table.find("tbody")
            table_rows = table_body.find_all("tr")

            for i in range(0, len(table_rows)):
                row_i = table_rows[i].find_all("td")
                country = row_i[0].text.strip()
                TotalCases = int(row_i[1].text.strip().replace(",", ""))
                NewCases = row_i[2].text.strip().replace("+", "").replace(",", "")
                TotalDeath = row_i[3].text.strip().replace("+", "").replace(",", "")
                if NewCases:
                    NewCases = int(NewCases)

                if country in model:
                    model[country]["TotalCases"]  = TotalCases
                    model[country]["NewCases"] = NewCases
                    model[country]["TotalDeaths"] = TotalDeath
                # else:
                #     print(country)
            f = open("results.json", 'w')
            f.write(json.dumps(model))
            f.close()
            return "200"
        except Exception as ex:
            print(ex)
            return {}