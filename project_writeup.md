#**Traffic Sign Recognition** 

##Writeup


---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./writeup/train_classes_hist.png "Train classes distribution"
[image2]: ./writeup/data_samples.png "Sample traffic signs"
[image4]: ./images/013.png "Traffic Sign 1"
[image5]: ./images/024.png "Traffic Sign 2"
[image6]: ./images/028.png "Traffic Sign 3"
[image7]: ./images/001.png "Traffic Sign 4"
[image8]: ./images/003.png "Traffic Sign 5"

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
###Writeup / README

You're reading it! and here is a link to my [project code](https://github.com/AlbertSadovnikov/CarND-Traffic-Sign-Classifier-Project/blob/master/Traffic_Sign_Classifier.ipynb)

###Data Set Summary & Exploration

####1. Provide a basic summary of the data set and identify where in your code the summary was done. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.


I used the pandas library to calculate summary statistics of the traffic
signs data set:

* The size of training set is 34799
* The size of test set is 12630
* The shape of a traffic sign image is 32x32x3 
* The number of unique classes/labels in the data set is 43

####2. Include an exploratory visualization of the dataset and identify where the code is in your code file.


Here is an exploratory visualization of the data set. 
![alt text][image2]

It is a bar chart showing how many representatives of each class 
are in the training set.

![alt text][image1]

###Design and Test a Model Architecture

####1. Describe how, and identify where in your code, you preprocessed the image data. What tecniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc.

The code for this step is contained in the fourth code cell of the IPython notebook.

As a first step, I decided to convert the images to grayscale to try how it works. 
Then I though that the grayscale info has the information regarding the luminance only and doesn't take into account 
sign colors, which is quite useful information. 
Then I tried feeding into the network raw color images, without any preprocessing - the results have improved a bit.

And as a last step, I thought that in order to reduce overall image luminance and contrast effect (due to the different lighting)
I should normalize the images. This step I have included directly in the model (tensorflow).

####2. Describe how, and identify where in your code, you set up training, validation and testing data. How much data was in each set? Explain what techniques were used to split the data into these sets. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, identify where in your code, and provide example images of the additional data)

Training, testing and validation sets were given in the dataset provided, so I didn't change anything there.

I didn't use any augumentation, though when testing on my custom set, I thought it might be a good idea to have a zoom factor as an augumentation parameter,
i.e. scale traffic signs a little (0.8x - 1.2x, perhaps). 

####3. Describe, and identify where in your code, what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

I have actually taken a LeNet as it is, just updated the input layer to accept rgb images and output layer to have the desired number of classes.

####4. Describe how, and identify where in your code, you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

Al the parameters were taken from LeNet, except for I have used a larger number of epochs - 50.

####5. Describe the approach taken for finding a solution. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.


My final model results were:
* training set accuracy of 1.00
* validation set accuracy of 0.946 
* test set accuracy of 0.937

If a well known architecture was chosen:
* What architecture was chosen? - LeNet
* Why did you believe it would be relevant to the traffic sign application? 
It was a suggested template and appeared to work reasonably well
* How does the final model's accuracy on the training, validation and test set provide evidence that the model is working well?
93.7 percents performance on a testing set seem to be relatively good (given the number of classes). 
Though it might not be actually good for the real application.
 

###Test a Model on New Images

####1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are 5 of 27 German traffic signs that I found on the web:

![alt text][image4] 
This image looks easy to detect, though it may present some difficulties, since background is blue (main color on other signs). Also it is not scaled and centered properly.

![alt text][image5] 
This image could be also difficult, since there were no signs of this type (electronic) in the data set, and bg color is black.

![alt text][image6] 
This image seems to be easily detected, or it can be mistaken with a similar background one.

![alt text][image7] 
This one is distorted and taken with a low resolution, so it might also be tricky.

![alt text][image8]
This one looks quite clear.

####2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. Identify where in your code predictions were made. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

Here are the results of the prediction:

001.png: correctly identified "Stop"    // image 4 in the previous section

002.png: correctly identified "Speed limit (70km/h)"

003.png: correctly identified "Speed limit (70km/h)" // image 5 in the previous section

004.png: correctly identified "Stop"

005.png: correctly identified "Stop"

006.png: correctly identified "Stop"

007.png: correctly identified "Stop"

008.png: correctly identified "Children crossing"

009.png: correctly identified "Children crossing"

010.png: correctly identified "Children crossing"

011.png: correctly identified "Children crossing"

012.png: ERROR detected "Wild animals crossing", actual "Speed limit (30km/h)"

013.png: ERROR detected "Priority road", actual "Yield" // image one in the previous section

014.png: correctly identified "General caution"

015.png: correctly identified "Speed limit (30km/h)"

016.png: correctly identified "Stop"

018.png: ERROR detected "Road work", actual "Stop"

020.png: correctly identified "Speed limit (100km/h)"

021.png: ERROR detected "Yield", actual "No vehicles"

022.png: ERROR detected "Speed limit (60km/h)", actual "Speed limit (80km/h)"

023.png: ERROR detected "No entry", actual "Vehicles over 3.5 metric tons prohibited"

024.png: ERROR detected "Right-of-way at the next intersection", actual "General caution" // image 2 in the previous section

025.png: ERROR detected "Speed limit (60km/h)", actual "Speed limit (100km/h)"

026.png: ERROR detected "Speed limit (50km/h)", actual "Speed limit (80km/h)"

028.png: ERROR detected "Children crossing", actual "Keep left" // image 3 in the previous section

029.png: correctly identified "Keep left"

032.png: correctly identified "Stop"


The model was able to correctly guess 17 of the 28 traffic signs, which gives an accuracy of 63%. 
This is actually way lower than I would expected, though I attempted to select a hard dataset.

####3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction and identify where in your code softmax probabilities were outputted. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The softmax probabilities seem to be quite skewed, i.e. model is almost always sure, even making incorrect predictions. 

1. Yield

  1.00000 Priority road
  0.00000 No passing for vehicles over 3.5 metric tons
  0.00000 Yield
  0.00000 Beware of ice/snow
  0.00000 Keep right


2. General caution

  0.99469 Right-of-way at the next intersection
  0.00261 Wild animals crossing
  0.00200 Bicycles crossing
  0.00064 Speed limit (60km/h)
  0.00003 End of speed limit (80km/h)
  
3. Keep left

  0.67124 Children crossing
  0.20496 Turn left ahead
  0.10234 Go straight or left
  0.01990 Roundabout mandatory
  0.00122 Keep right  

4. Stop

  1.00000 Stop
  0.00000 Yield
  0.00000 Keep right
  0.00000 Bicycles crossing
  0.00000 Road work
  
5. Speed limit (70km/h)

  1.00000 Speed limit (70km/h)
  0.00000 Speed limit (20km/h)
  0.00000 Speed limit (30km/h)
  0.00000 Speed limit (80km/h)
  0.00000 General caution
