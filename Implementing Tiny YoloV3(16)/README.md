# Implementaton in Tiny YoloV3 based on Darknet

Object detection of single or multiple objects using Tiny YoloV3 and inferencing it on Google colab. Since Colab provides free GPUs such as Nvidia P100/K80, we can instantly use these resources for training and testing the deep learning models. Here are the steps for implementing this model for detecting cars.

1. Create custom dataset of cars(~400) and annotate them using tools such as VGG image annotator or LabelImg

2. Divide the dataset into train test format

3. Calculation of anchor boxes according to dataset

4. Zip the prepared data and upload it to Google Colab

5. Load the datset and train the model

6. Inference the model as the final step

### Step1: 
Here the downloaded images are annotated using VGG annotator tool and are put under data the folder in .zip. As we annotate each images, we get the corresponding .txt file that has 
respective annotations. The number of classes required are mentioned in class_list file and is put under data conversion folder

### Step2:
In this step we split the data into train and test images. Run, process.py file and it will split the data and create two txt files, train and test in train-test conversion folder

### Step3:
We need to calculate anchor boxes, hence run the anchor.py file in anchor calulation folder. It calculates anchor boxes using K-means clustering and saves it as a txt file

### Step4:
In colabdata11 folder we edit the Yolov3_configuration.cfg file according to calculated anchor boxes and edit the number of filters required according to no. of classes based on the 
formula (n+5)*3. Here the no. of classes are 11, hence the number 48. Copy the train and test file from train-test conversion folder and put it under colabdata11 and edit the path 
according to path in Google colab. For e.g /content/darknet/cattle/cattle11/data/DSC00640.JPG. Create obj. data and obj.names files as mentioned in colabdata11 folder along with data,
train and test txt files and zip it and upload it to Google drive. 

Open Colab and mount the Google drive and start training the model. After every 1000 epochs it will automatically saves the .weights files under backup folder in the runtime
One the training is done for 3000-4000 epochs, we can stop it and inference on the sample image and calculate mean average precision(mAP) to calculate the performance of the model.



https://www.youtube.com/watch?v=ZbgP71gRFDU&t=35s


![](Ferrari.gif)
