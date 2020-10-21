# Implementaton in Tiny YoloV3 based on Darknet

Object detection of single or multiple objects using Tiny YoloV3 and inferencing it on Google colab. Since Colab provides free GPUs such as Nvidia P100/K80, we can instantly use these resources for training and testing the deep learning models. Here are the step for implementing this model for detecting cars.

1. Create custom dataset of cars(~400) and annotate them using tools such as VGG image annotator or LabelImg

2. Divide the dataset into train test format

3. Calculation on anchor boxes according to dataset

4. Zip the prepared data and upload it to Google Colab

5. Load the datset and train the model

6. Inference the model as the final step


https://www.youtube.com/watch?v=DS6Qe0tiIq8&list=PLzbdvw99SKOcjhFFVQRR5gBcfcFDOydJf


![](Ferrari.gif)
