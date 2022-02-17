import json
import sys

#load file in cmd args
if __name__ == '__main__':
    try:
        namespace1 = sys.argv[1]
        namespace2 = sys.argv[2]

        my_file1 = open(f"{namespace1}")
        text = json.load(my_file1)

        my_file2 = open(f"{namespace2}")
        values_json = json.load(my_file2)
        values_dict = dict()
        for index in range(len(values_json['values'])):
            values_dict.update({values_json['values'][index].values()})

    except IndexError:
        print("Opps. Open cmd: >python task3.py tests.json values.json")
        exit()

#initialize func for inner list
def inner_dicts(dicts):
    if isinstance(dicts, list):
        for i in dicts:
            list_dict(i)

#initialize main func
def list_dict(dicts):
    for k,v in dicts.items():
        try:
            if k == 'value':
                new_values = values_dict.get(tuple(dicts.items())[0][-1])
                dicts.update({'value': new_values})
            inner_dicts(v)
        except AttributeError:
            pass


#call func
list_dict(text)

#save
js = json.dumps(text, indent=2, sort_keys=True)
with open('report.json', 'w') as f:
    f.write(js)
