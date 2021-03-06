# Assignment 1B

What are Channels and Kernels (according to EVA)?

A kernel/weight matrix/filter/feature extractor is used to extratct features from the input image to store in channels or feature maps and the values of kernels can also change to notify that it is learning to extract specific features. Kernels convolve on top of images or any input data and only similar features are stored and separate channels has to be maintained for separate features. For out convinience we compute all input images using 3x3 kernel

Here is the example for 3x3 convolution
![](https://i.imgur.com/CVZbSKY.png)

In the above image we can see that when an image of 5x5 with three channels are convolved with a 3x3 kernel, produces a 3x3 resultant image and the kernel should consists as much channels as of input image to interact with it. If omre number of features needed from input image then more numbers of kernels has to be added after each convolution.'

# Feature maps
Feature maps/channels/Activation maps are the resultants obtained after convolving kernel on top of input image and conditions required to extract specific feature from input image are set or trained inside filters. If the balues present in the filters are matched with input image then dot product is performed to obtain values For e.g if we want to represent image representing arrow mark, then values of the kernel are adjusted to extract similar features out of input image as shown in figure below
![](https://i.imgur.com/fO55FnJ.png)
here the dot product and summation will be (10x10)+(10x10)+(10x10)=300

Why should we use 3x3 kernels?

Using 3x3 kernel is computation friendly. For e.g if we have the input image of resolution 9x9 and if the kernel of 9x9 is used, then it the network requires 9x9=81 parameters to map the pixels of i/p image and kernels but if the same network is configured using 4(3x3) kernels to convolve over 9x9 image then it requires only 36 parameters to produce same output. Another reason for using 3x3 kernel is the GPUs are well optimized for them.

we need to perform 99 3x3 convolution operation to reach 1x1 from 199x199

(199x199)(3x3)=>(197x197)(3x3)=>(195x195)(3x3)=>(193x193)(3x3)=>(191x191)(3x3)=>(189x189)(3x3)=>(187x187)(3x3)=>(185x185)(3x3)=>(183x183)(3x3)=>(181x181)(3x3)=>(179x179)(3x3)=>(177x177)(3x3)=>(175x175)(3x3)=>(173x173)(3x3)=>(171x171)(3x3)=>(169x169)(3x3)=>(167x167)(3x3)=>(165x165)(3x3)=>(163x163)(3x3)=>(161x161)(3x3)=>(159x159)(3x3)=>(157x157)(3x3)=>(155x155)(3x3)=>(153x153)(3x3)=>(151x151)(3x3)=>(149x149)(3x3)=>(147x147)(3x3)=>(145x145)(3x3)=>(143x143)(3x3)=>(141x141)(3x3)=>(139x139)(3x3)=>(137x137)(3x3)=>(135x135)(3x3)=>(133x133)(3x3)=>(131x131)(3x3)=>(129x129)(3x3)=>(127x127)(3x3)=>(125x125)(3x3)=>(123x123)(3x3)=>(121x121)(3x3)=>(119x119)(3x3)=>(117x117)(3x3)=>(115x115)(3x3)=>(113x113)(3x3)=>(111x111)(3x3)=>(109x109)(3x3)=>(107x107)(3x3)=>(105x105)(3x3)=>(103x103)(3x3)=>(101x101)(3x3)=>(99x99)(3x3)=>(97x97)(3x3)=>(95x95)(3x3)=>(93x93)(3x3)=>(91x91)(3x3)=>(89x89)(3x3)=>(87x87)(3x3)=>(85x85)(3x3)=>(83x83)(3x3)=>(81x81)(3x3)=>(79x79)(3x3)=>(77x77)(3x3)=>(75x75)(3x3)=>(73x73)(3x3)=>(71x71)(3x3)=>(69x69)(3x3)=>(67x67)(3x3)=>(65x65)(3x3)=>(63x63)(3x3)=>(61x61)(3x3)=>(59x59)(3x3)=>(57x57)(3x3)=>(55x55)(3x3)=>(53x53)(3x3)=>(51x51)(3x3)=>(49x49)(3x3)=>(47x47)(3x3)=>(45x45)(3x3)=>(43x43)(3x3)=>(41x41)(3x3)=>(39x39)(3x3)=>(37x37)(3x3)=>(35x35)(3x3)=>(33x33)(3x3)=>(31x31)(3x3)=>(29x29)(3x3)=>(27x27)(3x3)=>(25x25)(3x3)=>(23x23)(3x3)=>(21x21)(3x3)=>(19x19)(3x3)=>(17x17)(3x3)=>(15x15)(3x3)=>(13x13)(3x3)=>(11x11)(3x3)=>(9x9)(3x3)=>(7x7)(3x3)=>(5x5)(3x3)=>(3x3)(3x3)=>(1x1)
