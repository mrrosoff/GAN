import os
import sys
import numpy as np

from tqdm import tqdm

from PIL import Image


def main(target_dir, output_dir):

    for filename in tqdm(os.listdir(target_dir)):

        try:

            im = np.array(Image.open(target_dir + '/' + filename))
            im = np.fliplr(im)
            new_name = filename.split('.')[0] + '_mirror.jpg'
            new_name = ''.join(new_name)
            Image.fromarray(im).save(output_dir + '/' + new_name)

        except Exception as e:

            print('Image {} Failed: {}'.format(filename, str(e)))


if __name__ == '__main__':

    if len(sys.argv) < 3:

        print('Usage: python3 {} [Input Directory] [Output Directory]'.format(sys.argv[0]))

    else:

        main(sys.argv[1], sys.argv[2])
