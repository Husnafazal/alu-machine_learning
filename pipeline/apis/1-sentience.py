#!/usr/bin/env python3
"""
Create a method that returns the list 



def sentientPlanets():
    """
    Returns the list of names of the home planets 
    """
    url = "https://swapi-api.hbtn.io/api/species/"
    r = requests.get(url)
    json = r.json()
    results = json["results"]
    planets = []
    while json["next"]:
        for res in results:
            specie = res["designation"]
            homeworld = res["homeworld"]
            if (specie == "sentient" or res["classification"]) and homeworld:
                url_p = homeworld
                r_p = requests.get(url_p)
                json_p = r_p.json()
                planets.append(json_p["name"])
        url = json["next"]
        r = requests.get(url)
        json = r.json()
        results = json["results"]
    for res in results:
        specie = res["designation"]
        homeworld = res["homeworld"]
        if (specie == "sentient" or res["classification"]) and homeworld:
            url_p = homeworld
            r_p = requests.get(url_p)
            json_p = r_p.json()
            planets.append(json_p["name"])
    return planets