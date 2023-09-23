import requests
race_Num= 0 

test_dic = {}

for race_Num in range(0, 16):
        api_url = f"http://ergast.com/api/f1/2023/{race_Num}/results.json"
        test = requests.get(api_url)
        data = test.json()
        race_results = data["MRData"]['RaceTable']['Races'][0]['Results']

        for result in race_results:
                testA =result['Driver']['driverId']
                testB =result['points']
                #test_dic[testA] = testB
                print(testA)
                print(testB)

                
#for result in race_results:
    #testA =result['Driver']['driverId']
    #testB =result['points']
    #test_dic[testA] = testB

#print(test_dic)
