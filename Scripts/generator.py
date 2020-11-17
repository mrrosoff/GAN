import sys
import math

import json
import requests

from tqdm import tqdm

CLIENT_ID = 'WLq6UZfDRr3WvIMzSNrVLqdBjxH6-qZN5nyOiL7T04M'


def main(col, filename):

    url = 'https://api.unsplash.com/collections/{}?client_id='.format(col) + CLIENT_ID
    r = requests.get(url)

    if r.status_code == 200:

        data = json.loads(r.content)
        num = int(data['total_photos'])

    else:

        print("Couldn't Load Collection: {}, {}".format(r.status_code, r.content.decode()))
        return 1

    page_size = 30
    pages = math.ceil(num / page_size)
    print('Saving {} Images Using {} Pages'.format(num, pages))

    with open(filename, 'w', encoding='utf-8') as f:

        for n in tqdm(range(pages)):

            # &orientation=landscape if you want...
            url = 'https://api.unsplash.com/collections/{}/photos/?id={}&page={}&per_page={}&client_id='.format(col, col, n + 1, page_size) + CLIENT_ID
            r = requests.get(url, stream=True)

            if r.status_code == 200:

                data = json.loads(r.content)
                page_urls = [data[i]['urls']['small'] for i in range(len(data))]

                for urls in page_urls:

                    f.write(urls + '\n')

            else:

                print('#{} Failed'.format(n+1))


if __name__ == '__main__':

    if len(sys.argv) < 3:

        print('Usage: python3 {} [Collection ID] [Output File]'.format(sys.argv[0]))

    else:

        main(int(sys.argv[1]), sys.argv[2])
