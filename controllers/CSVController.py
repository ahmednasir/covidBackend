import csv, json
from config import resuts

class CSVController:

    def main_method(self, raw_text):
        model = resuts.prev_results()

        f = open('/home/ubuntu/covidBackend/csvfile.csv', 'w')
        f.write(raw_text)
        f.close()

        with open('/home/ubuntu/covidBackend/csvfile.csv', 'r') as file:
            reader = csv.reader(file)
            counter = 0
            for row in reader:
                if counter > 0 and row[1] in model:
                    if row[len(row)-1]:
                        model[row[1]]["TotalCases"]  += int(row[len(row)-1])
                        model[row[1]]["NewCases"] += int(row[len(row) - 1]) - int(row[len(row) - 2])
                    # country_dict[row[1]]["TotalCases"] += int(row[len(row)-1])
                    # country_dict[row[1]]["Newcases"]+= int(row[len(row) - 1]) - int(row[len(row) - 2])
                counter +=1


        f = open("/home/ubuntu/covidBackend/results.json", 'w')
        f.write(json.dumps(model))
        f.close()
        return model
