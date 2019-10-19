# Image Classification for a City Dog Show
---------

## Project Goal
Improving your programming skills using Python
In this project you will use a created image classifier to identify dog breeds. We ask you to focus on Python and not on the actual classifier (We will focus on building a classifier ourselves later in the program).

## Description:
Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information.

Some people are planning on registering pets that aren’t actual dogs.

You need to use an already developed Python classifier to make sure the participants are dogs.

>>> Note, you DO NOT need to create the classifier. It will be provided to you. You will need to apply the Python tools you just learned to USE the classifier.

## Your Tasks:
- Using your Python skills, you will determine which image classification algorithm works the "best" on classifying images as "dogs" or "not dogs".
- Determine how well the "best" classification algorithm works on correctly identifying a dog's breed. If you are confused by the term image classifier look at it simply as a tool that has an input and an output. The Input is an image. The output determines what the image depicts. (for example: a dog). Be mindful of the fact that image classifiers do not always categorize the images correctly. (We will get to all those details much later on the program).
- Time how long each algorithm takes to solve the classification problem. With computational tasks, there is often a trade-off between accuracy and runtime. The more accurate an algorithm, the higher the likelihood that it will take more time to run and use more computational resources to run.

# My solution
-------------
## Part A: Questions to Answer regarding Uploaded Image Classification:

Once the program stops running and the results files appear in the workspace, open and review each of the three to answer the following questions:
>>> Refer the files 
- vgg_uploaded-images.txt
- resnet_uploaded-images.txt
- alexnet_uploaded-images.txt

### 1. Did the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed? If not, report the differences in the classifications.

 All three model architectures classified the breed correctly.

### 2. Did each of the three model architectures classify the breed of dog in Dog_01.jpg to be the same breed of dog as that model architecture classified Dog_02.jpg? If not, report the differences in the classifications.

 No, there are some differences in the classification. `Alexnet` classified `Dog_01.jpg` breed as `airedale, airedale terrier`, but classified `Dog_02.jpg` breed as `chow, chow chow`

### 3. Did the three model architectures correctly classify Animal_Name_01.jpg and Object_Name_01.jpg to not be dogs? If not, report the misclassifications.

All three model architectures classified correctly to not to be dog

### 4. Based upon your answers for questions 1. - 3. above, select the model architecture that you feel did the best at classifying the four uploaded images. Describe why you selected that model architecture as the best on uploaded image classification.

If I have to select base my answer on questions 1. - 3. above, then I will say both `VGG` and `resnet` did well. They both classfified the verious images the same; However, if I have to consider the total elapsed runtime for these two models, then I will chose `resnet` as it took shorter time (0:0:0) to classifiy than `VGG` which took (0:0:3).

## Part B: Final Results


| # Total Images     | 40 |
|--------------------|----|
| # Dog Images       | 30 |
| # Not-a-Dog Images | 10 |


** Summary Statistics (percentages) on Models run **
 
| CNN Model Architecture |  % Not-a-Dog Correct |  % Dogs Correct |  % Breeds Correct |  Total Elapsed  Runtime (seconds) |
|------------------------|----------------------|-----------------|-------------------|-----------------------------------|
| RestNet                | 90.0%                | 100.0%          | 90.0%             | 5 s                               |
| AlexNet                | 100.0%               | 100.0%          | 80.0%             | 3 s                               |
| VGG                    | 100.0%               | 100.0%          | 93.3%             | 35 s                              |

### Project Result

Given our results, the "best" model architecture is `VGG`. It out performed both of the other architectures when considering both objectives 1 and 2. We will notice that ResNet did classify dog breeds better than `AlexNet`, but only `VGG` and `AlexNet` were able to classify "dogs" and "not-a-dog" at 100% accuracy. The model `VGG` was the one that was able to classify "dogs" and "not-a-dog" with 100% accuracy and had the best performance regarding breed classification with 93.3% accuracy.

It is weath mentioning that `VGG` despit its best performances, it is the poorest when it comes to runtime duration. We see that `AlexNet` is the fastest of them all.