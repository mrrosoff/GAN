# GAN

### Usage and Implementation of Generative Adversarial Networks

## About Project

This project follows three implementations of Generative Adversarial Networks to create images based on three datasets. In the notebook, we run three unique GANs with each dataset, and report on the effectiveness of the network to produce images that resemble the training set.

Our training image sets are:

1. Mountains
2. Dogs
3. Faces

## Installation

Begin by cloning the repository. Then, create a virtualenv.

```bash
sudo apt-get install python3
sudo apt-get install virtualenv
```

Next, activate the virtualenv and install the neccessary packages.

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To view the jupyter-notebooks, then run `jupyter-notebook` in your terminal. This will open a window where you will be able to view and select from the three GANs that we have created. 
