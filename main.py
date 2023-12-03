import requests
import json


def download_image():
    filename = 'comics_image.png'
    url = 'https://imgs.xkcd.com/comics/typical_seating_chart.png'
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def get_comment():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    json_response = json.loads(response.text)
    comment = json_response.get('alt')
    print(comment)


if __name__ == '__main__':
    download_image()
    get_comment()
