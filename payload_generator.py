import pathlib
import json
from utils.ExcelUtils import *

path = pathlib.Path(__file__).parent / "utils/a.xlsx"
# print(path)

key = singlerow(path, "userdata", 1, getColCount(path, "userdata"))
value = singlerow(path, "userdata", 2, getColCount(path, "userdata"))
# print(key,value)
d = dict(zip(key, value))
# print(d)
json_object = json.dumps(d, indent=4)
# print(json_object)

payloadlist = []
for i in range(1, getColCount(path, "userdata")):
    key = singlerow(path, "userdata", 1, getColCount(path, "userdata"))
    value = singlerow(path, "userdata", 2, getColCount(path, "userdata"))
    d = dict(zip(key, value))
    json_object = json.dumps(d, indent=4)
    payloadlist.append(json_object)
print(*payloadlist, sep="\n")

# payloadlistjson = json.dumps(payloadlist, indent=2)
# print(payloadlistjson)
