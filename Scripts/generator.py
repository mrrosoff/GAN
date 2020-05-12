import sys
import json
import requests
import math
from tqdm import tqdm


CLIENT_ID = 'WLq6UZfDRr3WvIMzSNrVLqdBjxH6-qZN5nyOiL7T04M'

def main(col, filename):
    urls = []
    url = 'https://api.unsplash.com/collections/{}?client_id='.format(col) + CLIENT_ID
    r = requests.get(url)
    if r.status_code == 200:
        data = json.loads(r.content)
        num = int(data['total_photos'])
    else:
        print("Couldn't load collection: {}, {}".format(r.status_code, r.content.decode()))
        sys.exit(1)

    page_size = 30
    pages = math.ceil(num / page_size)
    print('Collection has {} images, downloading {} pages'.format(num, pages))

    for n in tqdm(range(pages)):
        # &orientation=landscape if you want...
        url = 'https://api.unsplash.com/collections/{}/photos/?id={}&page={}&per_page={}&client_id='.format(col, col, n+1, page_size) + CLIENT_ID
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            data = json.loads(r.content)
            page_urls = [data[i]['urls']['small'] for i in range(len(data))]
            urls += page_urls
        else:
            print('Uh oh! #{} failed'.format(n+1))
            print('Continue (will still save successful urls)? [Y/n] ', end='')
            d = input()
            if d.lower() != 'y':
                break
    print('Saving {} image urls'.format(len(urls)))

    with open(filename, 'w', encoding='utf-8') as f:
        for url in urls:
            f.write(url + '\n')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 {} [collection ID] [output filename]'.format(sys.argv[0]))
    else:
        main(int(sys.argv[1]), sys.argv[2])
