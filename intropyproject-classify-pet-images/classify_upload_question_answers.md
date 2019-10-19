# Questions to Answer regarding Uploaded Image Classification:

Once the program stops running and the results files appear in the workspace, open and review each of the three to answer the following questions:

### 1. Did the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed? If not, report the differences in the classifications.

 >>> All three model architectures classified the breed correctly.

### 2. Did each of the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed of dog as that model architecture classified Dog_02.jpg? If not, report the differences in the classifications.

 >>> No, there are some differences in the classification. `Alexnet` classified `Dog_01.jpg` breed as `airedale, airedale terrier`, but classified `Dog_02.jpg` breed as `chow, chow chow`

### 3. Did the three model architectures correctly classify Animal_Name_01.jpg and Object_Name_01.jpg to not be dogs? If not, report the misclassifications.

>>> All three model architectures classified correctly to not to be dog

### 4. Based upon your answers for questions 1. - 3. above, select the model architecture that you feel did the best at classifying the four uploaded images. Describe why you selected that model architecture as the best on uploaded image classification.

>>> If I have to select base my answer on questions 1. - 3. above, then I will say both `VGG` and `resnet` did well. They both classfified the verious images the same; However, if I have to consider the total elapsed runtime for these two models, then I will chose `resnet` as it took shorter time (0:0:0) to classifiy than `VGG` which took (0:0:3).