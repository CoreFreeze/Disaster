import json

def loadSettings():
    file = open('settings.json', encoding='UTF8')
    data = json.load(file)
    
    if "IP" in data:
        return data['IP']
    else:
        return None


def saveSettings(Info):
    file = open('settings.json', encoding='UTF8')

    saveInfo = {}
    saveInfo["IP"] = str(Info)

    with open('settings.json', 'w', encoding='UTF8') as outfile:
        json.dump(saveInfo, outfile, ensure_ascii=False, indent=4)
