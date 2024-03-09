#!/usr/bin/env python3

"""
This module contains a function that
uses Swapi API to get the list of names of
all sentinent species in the Star Wars universe"""

import requests


def sentientPlanets():
    """return list of names of all sentient species"""
    url = "https://swapi-api.alx-tools.com/api/species/"
    response = requests.get(url)
    data = response.json()
    species = []
    for result in data['results']:
        if result['designation'] == "sentient":
            species.append(result['name'])
    return species
