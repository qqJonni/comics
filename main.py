import requests


def download_image():
    filename = 'comics_image.png'
    url = 'https://imgs.xkcd.com/comics/typical_seating_chart.png'
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    download_image()
