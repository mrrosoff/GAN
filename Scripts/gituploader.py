import os
import sys

from tqdm import tqdm

from git import Repo


def main(target_dir):

    repo = Repo("../GAN").git

    for index, filename in tqdm(enumerate(os.listdir(target_dir))):

        try:

            repo.add(target_dir + "/" + filename)

            if index != 0 and index % 50 == 0:

                repo.commit("-m", "Add Images {}".format(index // 50))
                repo.push("origin", "master")

        except Exception as e:

            print('Image {} Failed: {}'.format(filename, str(e)))


if __name__ == '__main__':

    if len(sys.argv) < 2:

        print('Usage: python3 {} [Upload Directory]'.format(sys.argv[0]))

    else:

        main(sys.argv[1])
