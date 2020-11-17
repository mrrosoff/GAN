import sys

import requests

from tqdm import tqdm


def main(name, dir):

    with open(name) as f:

        urls = f.readlines()
        print('Downloading {} Images'.format(len(urls)))

        for index, url in tqdm(enumerate(urls)):

            try:

                r = requests.get(url, stream=True)

                if r.status_code == 200:

                    fn = url.split('?')[0].split('/')[-1].split('.')[0]

                    with open(dir + '/{}.jpg'.format(fn), 'wb') as img_file:

                        for chunk in r.iter_content(1024):

                            img_file.write(chunk)
                else:

                    raise Exception('status code: {}'.format(r.status_code))

            except Exception as e:

                print('Image {} Failed: {}'.format(index + 1, str(e)))


if __name__ == '__main__':

    if len(sys.argv) < 3:

        print('Usage: python3 {} [URL File] [Output Directory]'.format(sys.argv[0]))

    else:

        main(sys.argv[1], sys.argv[2])
