# Possible mislabeled Flowers

Following is the list of flowers in valid and test set that my model wrongly predicted according to its label. 
For this purpose I use a model with valid accuracy of 99.39 (5 wrong predictions from 818 images) and test accuracy 
of 98.79 (10 wrong predictions from 819 images). Each wrongly predicted images (the top left) is compared to 3 other 
images with the same label (first row) and 4 other images from the predicted label (second row). With this 
comparison we can check visually whether the image is correctly labeled by the team from the University of 
Oxford or not.

## Valid Set Images
1. The first image image_07303.jpg is clearly misclassified, labelled as Ball moss (93), but it should be 
Foxglove (94)
![01_image_07303.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/valid/01_image_07303.png)
2. I think the second image image_07677.jpg is also misclassified as Camelia (96), which should be Mallow (97)
![02_image_07677.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/valid/02_image_07677.png)
3. Image is correct labeled, I wrongly predicted
![03_image_03693.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/valid/03_image_03693.png)
4. Image is Correct labeled, I wrongly predicted
![04_image_04333.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/valid/04_image_04333.png)
5. Image is Correct labeled, I wrongly predicted
![05_image_04927.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/valid/05_image_04927.png)

## Test Set Images
1. I think the first image image_07683.jpg is  misclassified, labelled as Camelia (96), 
but it should be Mallow (97)
![01_image_07683.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/01_image_07683.png)
2. The second image image_07676.jpg is probably also misclassified, labelled as Camelia (96), 
but it should be Mallow (97)
![02_image_07676.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/02_image_07676.png)
3. Image is correct labeled, I wrongly predicted
![03_image_02412.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/03_image_02412.png)
4. Image is correct labeled, I wrongly predicted
![04_image_04012.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/04_image_04012.png)
5. Image is correct labeled, I wrongly predicted
![05_image_07672.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/05_image_07672.png)
6. Image is correct labeled, I wrongly predicted
![06_image_05653.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/06_image_05653.png)
7. Image is correct labeled, I wrongly predicted
![07_image_04568.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/07_image_04568.png)
8. Image is correct labeled, I wrongly predicted
![08_image_04938.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/08_image_04938.png)
9. Image is correct labeled, I wrongly predicted
![09_image_05678.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/09_image_05678.png)
10. Image is correct labeled, I wrongly predicted
![11_image_07536.png](https://github.com/cahya-wirawan/Udacity-Course/raw/master/images/test/11_image_07536.png)

# Conclusion
In my opinion, there are 2 mislabeled images (image_07303.jpg and image_07677.jpg) in valid dataset 
and also 2 mislabeled images (image_07683.jpg and image_07676.jpg) in test dataset. That means 
no one will be able to achieve 100% accuracy on this Oxford flower classification by Udacity 
Pytorch Challenge