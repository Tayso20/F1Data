import requests

api_url = "http://ergast.com/api/f1/2023/1/results.json"
test = requests.get(api_url)
data = test.json()
test_dic = {}
race_results = data["MRData"]['RaceTable']['Races'][0]['Results']
for result in race_results:
    testA =result['Driver']['driverId']
    testB =result['points']

    #print(result['Driver']['driverId'],result['points'])

    test_dic[testA] = testB

print(test_dic)
print("uwu")