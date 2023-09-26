import requests
import json


def get_race_results():
    allRaces = {}
    driver_names = set()
    for race_Num in range(1, 17):
        api_url = f"http://ergast.com/api/f1/2023/{race_Num}/results.json"
        test = requests.get(api_url)
        data = test.json()
        race_results = data["MRData"]["RaceTable"]["Races"][0]["Results"]
        singlerace = {}

        for result in race_results:
            driver = result["Driver"]["driverId"]
            driver_names.add(driver)
            pts = result["points"]
            singlerace[driver] = int(pts)

        allRaces[f"Race{race_Num}"] = singlerace
    return allRaces, driver_names

def get_driver_results(driver_names, allRaces):
    allPoints = {driver: [] for driver in driver_names}
    for race_num in range(1, 17):
        race_results = allRaces[f"Race{race_num}"]
        for driver in driver_names:
            if driver in race_results:
                allPoints[driver].append(race_results[driver])
            else:
                allPoints[driver].append(0)
    return allPoints
        

def save_Json(json_file, path):
    with open(path, "w") as f:
        json.dump(json_file, f)

def main():
    allRaces, driver_names = get_race_results()
    allPoints = get_driver_results(driver_names, allRaces)
    save_Json(allRaces, "pleasefuckingwork.json")
    save_Json(allPoints, "holygod.json")
    print(allPoints)

if __name__ == "__main__":
    main()




