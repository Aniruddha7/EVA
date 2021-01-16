# Cattle detection using Tiny Yolo_V3 based on DarkNet

In this project, we use Yolo_v3 object detection model to detect cattle of Herd size 11, i.e cattles of 11 different classes, and try to predict the sample image to detect the class and localize the cattle object. We follow the below mentioned steps before training the model.
 
 1. Create custom cattle dataset either by downloading the images or by manually taking photos and annotate them by using LabelImg tool
 
 2. Divide the dataset into train test format
 
 3. Calculate the anchor boxes for the dataset and edit the configuraton file according to number of classes, anchor box values
 
 4. Zip the prepared data such as training data, cfg file, obj.names, obj.data text files of train and test data. Upload them to Google Colab and train the model
 
 5. Inference the model on a sample test image and calculate mAP (mean average precision) for all the classes as the final step
 


### Step1:
