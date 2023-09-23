import requests
import json
race_Num= 0 


allRaces = {}

for race_Num in range(0, 16):
        api_url = f"http://ergast.com/api/f1/2023/{race_Num}/results.json"
        test = requests.get(api_url)
        data = test.json()
        race_results = data["MRData"]['RaceTable']['Races'][0]['Results']
        singlerace = {}
        for result in race_results:
                driver =result['Driver']['driverId']
                pts =result['points']
                singlerace[driver] = pts
                allRaces[f"Race{race_Num}"] = singlerace
 


with open('pleasefuckingwork.json', 'w') as f:
    json.dump(allRaces, f)



                




#for result in race_results:
    #testA =result['Driver']['driverId']
    #testB =result['points']
    #test_dic[testA] = testB