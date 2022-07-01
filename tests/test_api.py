import requests
from project import api, lists

api_wk = api.ApiWikipedia("Toulouse")
api_gm = api.ApiGoogleMaps("OpenClassrooms Paris")


def test_api_wikipedia(monkeypatch):
    results = "<Response [200]>"

    def mock_api_wikipedia():
        return results

    monkeypatch.setattr(requests, 'get', mock_api_wikipedia)
    assert api_wk.api_wikipedia_keyword == "Toulouse"
    assert api_wk.api_wikipedia_url == "https://fr.wikipedia.org/w/api.php?format=json&action=query&prop=extracts" \
                                       "&exintro=&explaintext=&titles=Toulouse"


def test_api_googlemaps(monkeypatch):
    results = "<Response [200]>"

    def mock_api_googlemaps():
        return results

    monkeypatch.setattr(requests, 'get', mock_api_googlemaps)
    assert api_gm.api_googlemaps_keyword == "OpenClassrooms Paris"
    assert api_gm.api_googlemaps_url == "https://maps.googleapis.com/maps/api/geocode/json?address" \
                                        "=OpenClassrooms Paris&key=AIzaSyAkmHpMq2iqx_Em1tP0P6tmA-wS3ePNaWM&region=fr"
    assert api_gm.api_googlemaps_content == "10 Quai de la Charente, 75019 Paris, France"
    assert api_gm.api_googlemaps_image == "https://maps.googleapis.com/maps/api/staticmap?center=10+Quai+de+la" \
                                          "+Charente,+75019+Paris," \
                                          "+France&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S" \
                                          "%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614," \
                                          "-74.012318&markers=color:red%7Clabel:C%7C40.718217," \
                                          "-73.998284&key=AIzaSyAkmHpMq2iqx_Em1tP0P6tmA-wS3ePNaWM"
