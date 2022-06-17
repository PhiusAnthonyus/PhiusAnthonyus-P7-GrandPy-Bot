from project import lists
import random
import requests
import configparser

# Utilise configparser pour parser le fichier config
configParser = configparser.RawConfigParser()
configFile = r'config.cfg'
configParser.read(configFile)
api_key = str(configParser.get('Default', 'api-key'))


class ApiWikipedia:
    def __init__(self, keyword) -> None:
        self.api_wikipedia_keyword = keyword
        self.api_wikipedia_url = f"https://fr.wikipedia.org/w/api.php?format=json&action=query&prop" \
                                 f"=extracts&exintro=&explaintext=&titles={self.api_wikipedia_keyword}"
        self.api_wikipedia_content = self.get_content()

    def get_content(self):
        """Récupère et récupère le contenu désiré à partir de l'API."""
        error_text = f"Je ne sais pas où se trouve {self.api_wikipedia_keyword} mon poussin, pourrais-tu " \
                     f"m'en dire plus ?"
        if self.api_wikipedia_keyword != "":
            result = requests.get(self.api_wikipedia_url)
            if result.status_code == 200:
                content = result.json()
                pageid = str(content["query"]["pages"])
                pageid = pageid.split("{")[1][1:-3]
                if int(pageid) != -1:
                    content = str(content["query"]["pages"][pageid]["extract"])
                    if content != "":
                        content = str(content.split(".")[0:2])[2:-2]  # Nb de phrases voulues.
                        return f"{random.choice(lists.grandpy_wiki_desc)}{content}"
                    else:
                        return error_text
                else:
                    return error_text
        else:
            return "Je n'ai pas compris ce que tu m'as dit mon poussin"


class ApiGoogleMaps:
    def __init__(self, keyword: str):
        self.api_googlemaps_keyword = keyword
        self.api_googlemaps_url = f"https://maps.googleapis.com/maps/api/geocode/json?address" \
                                  f"={self.api_googlemaps_keyword}&key={api_key}&region=fr"
        self.api_googlemaps_content = self.get_content()
        self.api_googlemaps_image = self.get_map()

    def get_content(self):
        """Récupère et récupère le contenu désiré à partir de l'API."""
        if self.api_googlemaps_keyword != "":
            result = requests.get(self.api_googlemaps_url)
            if result.status_code == 200:
                content = result.json()
                print(self.api_googlemaps_url)
                error_text = f"Je ne sais pas où se trouve {self.api_googlemaps_keyword} mon poussin, pourrais-tu " \
                             f"m'en dire plus ?"
                if content['results']:
                    content = content["results"][0]['formatted_address']
                    print(content)
                    return f"{random.choice(lists.grandpy_map_desc)}{content}"
                else:
                    return error_text
        else:
            return "Je n'ai pas compris ce que tu m'as dit mon poussin"

    def get_map(self):
        """Génère la carte statique du lieu recherché."""
        address = self.api_googlemaps_content
        error_text = f"Je ne sais pas où se trouve {self.api_googlemaps_keyword} mon poussin, pourrais-tu " \
                     f"m'en dire plus ?"
        print(address)
        if address != error_text:
            address = address.replace(" ", "+")
            image = f"https://maps.googleapis.com/maps/api/staticmap?center={address}&zoom=13&" \
                f"size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147," \
                f"-74.015794&markers=color:green%7Clabel:G%7C40.711614," \
                f"-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key={api_key}"
            print(image)
            return image
        else:
            return "static/image.png"


if __name__ == "__main__":
    test = ApiWikipedia("Foix")
    test2 = ApiGoogleMaps("Foix")
    print(test.api_wikipedia_url)
    print(test.api_wikipedia_content)
    print(test2.api_googlemaps_url)
    print(test2.api_googlemaps_content)
