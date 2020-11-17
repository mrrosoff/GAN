import os
import sys

from tqdm import tqdm


def main(target_dir):

    for folder in tqdm(os.listdir(target_dir)):

        if os.path.isdir(target_dir + "/" + folder):

            for file in os.listdir(target_dir + "/" + folder):

                try:

                    os.rename(target_dir + "/" + folder + "/" + file, target_dir + "/" + file)

                except Exception as e:

                    print('Image {} Failed: {}'.format(file, str(e)))

            os.rmdir(target_dir + "/" + folder)


if __name__ == '__main__':

    if len(sys.argv) < 2:

        print('Usage: python3 {} [Target Directory]'.format(sys.argv[0]))

    else:

        main(sys.argv[1])
