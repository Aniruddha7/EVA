##ORDER OF CONCEPTS

How many layers

3x3 Convolutions

Kernels and how do we decide the number of kernels

Receptive Field

MaxPooling

Position of MaxPooling

The distance of MaxPooling from Prediction

Concept of Transition Layers

Position of Transition Layer

When do we stop convolutions and go ahead with a larger kernel or some other alternative (which we have not yet covered)

1x1 Convolutions

SoftMax

Adam vs SGD

Number of Epochs and when to increase them

How do we know our network is not going well, comparatively, very early

When to add validation checks

Batch Size, and effects of batch size

Image Normalization

Batch Normalization

The distance of Batch Normalization from Prediction

When do we introduce DropOut, or when do we know we have some overfitting

DropOut

Learning Rate

LR schedule and concept behind it  


The intuition behind this order is that we have to decide how should be the network before getting optimum accuracy.According to that first
we need to decide 1)How many layers should be there in the network i.e do we need a larger network with lager parameters or smaller one. 
After that I would think about adding 2) 3x3 Convolution layers and 3) No. of kernels that are needed to reach 4) required Receptive field
also we need to think of implementing 5) Maxpooling which is helpful in reducing the number of convolution layers required. The 6) Position
of MaxPooling is also very important since it 7)should note be applied before prediction. In resnet and other architectures we use 
8)Transition layers followed by 5 convolution layers 9) For transition layers the same condition applies here as of Maxpooling layers as
it can not be used just before prediction. 10) After Maxpooling if we end up Even sized kernels,then we can use other alternatives like 4x4
or even larger than that. 11) After 3x3 convolution, Maxpooling,Transition layers we would be using 1x1 kernels to reduce the depth of the 
channels. 12) SoftMax fucnction is then used to get a probability like result of the predicted output 13)Optimizers like either Adam or SGD
(Stochastic Gradient Descent) can be used to train network 14) During training we need to mention the number of epochs under model.fit
function. If the accuracy is not reached withing the mentioned number of epochs then we can think of extending it but it would not be the 
only solution to increase test accuracy 15) We can detect if the nework is good or not during the first epoch. If the first epoch is not
good then we need to tweak the code again 16) We need to add validation checks after each epoch to check validation accuracy 17) Batch
size can be increased during training which also helps in increasing accuracy 18) Based on the validation accuracy of the network, we can
use Image normalization or 19) batch normalization where the intensity of the kernel pixel values are increased. This helps in predicting
gradients and textures. 20) The distance of Batch normalization does not affect the prediction 21) If the train accuracy of the network
is not inceasing and it is saturated then we introducec Dropouts. 22) Dropouts randomly turns off the redundant values on kernels which
helps new kernels to learn the paterns. 23) Learning rate is the method of defining at what speed the network has to learn after each 
epoch to avoid overshooting. 24) LR scheduling is used to increase netowrk performance and reduce training time. The learning rate has
should be decreased during gradient descent to achieve local minima and the formula for it is LR = LR*1/(1+decay*epoch)









