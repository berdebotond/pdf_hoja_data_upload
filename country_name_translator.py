import json

# read translations
with open("translation_country2.json") as f:
    countries_translataion = json.load(f)


def translate_countries_from_en_es(country):
    country_name = country.replace(" ", "_").lower()
    if country_name in countries_translataion.keys():
        return countries_translataion[country_name]
    else:
        return country


