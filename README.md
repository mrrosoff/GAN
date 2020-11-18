# GAN

### Usage and Implementation of Generative Adversarial Networks

## About

The repository is a host of both GAN implemenations used to complete varying tasks as well as an image dataset for said implemenations. The following is a list of current GAN projects in the repository.

1. Image Generatation

This project follows three implementations of Generative Adversarial Networks to create images based on three datasets. In the notebook, we run three unique GANs each with three datasets, and report on the effectiveness of the network to produce images that resemble the training set. In addition, we extrapolate our results to larger images.

2. Image Colorization

This project follows implemenation of a Generative Adversarial Network to colorize greyscale images.

## Installation

Begin by cloning the repository. Then, create a virtualenv.

```bash
git clone --depth=1 https://github.com/mrrosoff/GAN/
sudo apt-get install python3
sudo apt-get install virtualenv
```

Next, activate the virtualenv and install the neccessary packages.

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To view the jupyter-notebooks, then run `jupyter-notebook` in your terminal. This will open a window where you will be able to view and select from the GANs in the repo. 
