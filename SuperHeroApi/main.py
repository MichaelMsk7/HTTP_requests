# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import requests
import json



URL = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(URL).json()
data = response

dict = {}
final_dict ={}
for stat in data:
    name = stat['name']
    intellegance = stat['powerstats']['intelligence']
    dict[name] = intellegance
print(dict)
print("---")
for key,value in dict.items():
    if key == "Thanos" or key == "Hulk" or key == "Captain America":
        final_dict[key] = value
print(final_dict)
print("---")
for key, value in final_dict.items():
    mav_val = max(final_dict.values())
print(f"{key}:{mav_val}")
print("---")















