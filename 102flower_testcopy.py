import scipy.io as sio
from pathlib import Path
import os
from shutil import copy

# The original 102 flower dataset can be downloaded from
# http://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz
# including the labels:
# http://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat
# The file 102flowers.tgz should be untared on "root_dir"
# and imagelabels.mat should be copied in "root_dir"
# Just change the "root_dir" appropriately


root_dir = Path('/mnt/mldata/data/Udacity/combine')
original_dir = root_dir/'jpg'
labels_file = root_dir/'imagelabels.mat'
udacity_dir = root_dir/'flower_data'
udacity_train_dir = udacity_dir/'train'
udacity_valid_dir = udacity_dir/'valid'
udacity_test_dir = udacity_dir/'test'

labels=sio.loadmat(labels_file)['labels'][0]
(_, _, original_images) = next(os.walk(original_dir))
original_images = sorted(original_images)

image_to_label = {name: labels[i] for i, name in enumerate(original_images)}

udacity_images = []
for root, dirs, files in os.walk(udacity_dir):
    udacity_images.extend(files)

diff = set(original_images) - set(udacity_images)

udacity_test_dir.mkdir(parents=True, exist_ok=True)
for file in diff:
    dest_dir = udacity_test_dir/str(image_to_label[file])
    dest_dir.mkdir(parents=True, exist_ok=True)
    copy(original_dir/file, dest_dir)
