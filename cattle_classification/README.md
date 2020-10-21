## Cattle classification using MobileNetV3 model:
In this project we will try classifying the cattle images belonging to Herd size of 14 i.e 14 categories of cattles. 

-> First we prepare dataset of total no. of 152 train images and 16 test images

-> We split the train dataset into train and valid images using K-Fold split of 5 folds which will randomly split data into 5 versions of train and valid data

-> Pass these images for training using MobileNetV3 model since it is a lightweight model (weights files only have ~6Mb) that is best suited for deploying on mobile phones or other low end devices

-> Train the model with 5 KFolds for 40 epochs separately and save the weights file for future reference. The reason behind implementing K-Fold is to get better accuracy and to avoid misclassification of images between different herds

-> If the use case is such that you capture new images for classification, then you can directly use this pretrained weight that has trianed for 40 epochs

-> In this project, it has been found that retraining of new images for 40 epochs was sufficient for getting better results in terms of both accuracy and misclassified images
