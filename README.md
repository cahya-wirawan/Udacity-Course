# Udacity-Course

## 102flower_testcopy.py

The script copies 819 images from the original 102 flower dataset that don't exist in 
flower dataset provided by Udacity and put it in Udacity flower_data/test folder.
 
The original 102 flower dataset can be downloaded from 
http://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz
including its labels: http://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat
The file 102flowers.tgz should be untared on "root_dir"
and imagelabels.mat should be copied in "root_dir"
and just change the "root_dir" appropriately.

The 102 flower dataset from Udacity can be downloaded from
https://s3.amazonaws.com/content.udacity-data.com/courses/nd188/flower_data.zip
This file should be also unziped to "root_dir"

## flower_test.tgz

Test folder with 819 images created by the script.

## Possible Mislabeled Images
After reviewing the result of the predictions, it seems there are 2 mislabeled 
images in valid dataset and also 2 mislabeled images in test dataset. Following is the 
[review of the images](https://github.com/cahya-wirawan/Udacity-Course/blob/master/possible_mislabeled_images.md).