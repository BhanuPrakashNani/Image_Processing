[![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/) [![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/Naereen/StrapDown.js)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Live Hand Gesture Detection  

## Introduction  
Live Gesture Recognition is an application that captures and interprets human gestures as numbers. Gesture here, can refer to any physical movement, large or small of the fingers. This project has been built using OpenCV and Python. It is based on the concepts of object segmentation. It segments one foreground obeject which in this case is our hand, from a live video sequence.

## Working  

The two essential parts of this project are 
1. Segmentation of hand region from the video sequence
2. Counting the number of fingers from segmented region

### 1. Segmentation of the Hand Region  
One of the efficient methods to separate foreground from background is using the concept of running averages. More about running averages can be found over [here](http://opencvpython.blogspot.com/2012/07/background-extraction-using-running.html). The system looks over a particular number of frames of the background and runs the average of those. The background is figured out with this average.  

When the hand is brought inside the frame after the calibration(once the application starts, it takes 30 sec to calibrate itself according to the background), absolute difference between the background model and the current frame is obtained resulting in a single foreground object - the hand. This method so far as a whole, is known as Background subtraction.

Getting the foreground object does not suffice, there is a need to threshold the difference image to make the hand region visible making all other regions black. To detect the motion of the fingers, contours are of great help. Contours of the difference image are taken and the contour with the largest area is assumed to be the hand.   

### 2. Counting the number of fingers from segmented region
The process of counting the fingers has five intermediate steps
  + Finding the convex hull of the segmented hand region.
  + Computing the most extreme points in the convex hull
  + Finding the center of the palm using t he extreme points.
  + Constructing a cricle around the hand with centre of the palm as origin.
  + Bitwise AND between the thresholded hand image and the circle(also known as ROI - Region Of Interest) 
  ![Steps](https://github.com/abhishekbvs/Gesture-Detection/blob/master/static/image1.png)

## Installation

### Pre-requisites
  + OpenCV
  + Python3
  + Flask

### Installation Instructions
1. Install Python3 and pip
2. Install `virtualenv` and add it to your terminal path.
3. Clone the repository and create the virtual environment
    ```
      $ git clone https://github.com/abhishekbvs/Gesture-Detection.git
      $ cd Gesture-Detection
    ```
4. Create a python 3 virtualenv, and activate the environment.
    ```
      $ virtualenv -p python3 .
      $ source bin/activate
    ```
5. Install the dependencies from `requirements.txt`
    ```
      $ pip install -r requirements.txt
    ```
6. Run the Flask application
    ```
      $ python app.py
    ```

## Team

  + [Bhanu Prakash](https://github.com/BhanuPrakashNani/)
  + [Abhishek BVS](https://github.com/abhishekbvs/)
  + [Bala Sai Praneeth](https://github.com/PraneethVankayala)

## Future Scope  
This project can be extended to understand the gestures and execute commands based on the gestures.

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/abhishekbvs/Gesture-Detection) 