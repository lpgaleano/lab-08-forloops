myData = {"effective top tube length": 515, "seat tube length": 500, "seat tube angle": 74.4, "head tube angle": 70.5, "stack": 513, "reach": 367, "standover height": 755}
for k, v in myData.items():
    print("key:", k, ", value:", v)
keysList = list(myData.keys())
valuesList = list(myData.values())
print("ALL KEYS:", keysList)
print("ALL VALUES:", valuesList)
