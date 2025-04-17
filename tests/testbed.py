import json
import boto3

class Test:
    def __init__(self):
        pass
        # Load the TXT file
    def convert_slurs_to_json(self):
        with open('data/slurs.txt', 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]
            words = {i+1:word for i,word in enumerate(words)}
            with open('data/slurs.json', 'w') as json_file:
                json.dump(words,json_file, indent=4)

    def convert_animals_to_json(self):
        with open('data/animals.txt', 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]
            words = {int(line.split(": ")[0]): line.split(': ')[1] for line in words}
            with open('data/animals.json', 'w') as json_file:
                json.dump(words, json_file, indent=4)

    def configure_for_dynamo_db(self):
        sample = {
        "id": { "N": "1" },
        "data": {
            "L": [
            { "S": "abbo" },
            { "S": "camel" }
            ]
        }
        }

        with open('data/slurs.json', 'r') as slurs, open('data/animals.json', 'r') as animals:
            slurs_dict = json.load(slurs)
            animals_dict = json.load(animals)

            final = []
            for key, value in slurs_dict.items():
                print(key, value)
                final.append({"id": {"N": key},
                              "data": {
                                  "L": [
                                      {'S': value},
                                      {'S': animals_dict[key]}
                                  ]
                              }})
            print(final)



        # dynamo_db = {
        # "slur": {
        #     "M":{key:{"S": value} for key, value in slurs_dict.items()}
        #     },
        # "animal": {
        #     "M": {key:{"S": value} for key, value in animals_dict.items()}
        #     }
        # }




if __name__ == "__main__":
    test = Test()
    test.configure_for_dynamo_db()