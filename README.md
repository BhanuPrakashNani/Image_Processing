# Image_Processing
Welcome aboard. With the growing technologies out in the world, we have seen how important Image Processing has become. This repository provides a complete understanding of practical implementation of all the concepts to be known for a developer to start their Image Processing journey. 

## Contents

1. [Basics with Images](https://github.com/BhanuPrakashNani/Image_Processing#1-basics-with-images---averaging-images)
2. [Successive Rotations](https://github.com/BhanuPrakashNani/Image_Processing#2-successive-rotations---code)
3. [Interpolations](https://github.com/BhanuPrakashNani/Image_Processing#3-interpolations---code)
4. [Interpolations-Inverse Mapping](https://github.com/BhanuPrakashNani/Image_Processing#4-interpolation-inverse-mapping---code)
5. [Basic Transformations](https://github.com/BhanuPrakashNani/Image_Processing#5-basic-transformations---code)
6. [Perspective Transofrmation](https://github.com/BhanuPrakashNani/Image_Processing#6-perspective-transformation)
7. [Estimating the Transformation](https://github.com/BhanuPrakashNani/Image_Processing#7-est-transformation)
8. [Log and Contrast Stretching](https://github.com/BhanuPrakashNani/Image_Processing#8-log-and-linear-transformation)
9. [Shading Correction](https://github.com/BhanuPrakashNani/Image_Processing#9-shading-correction)
10. [Laplacian](https://github.com/BhanuPrakashNani/Image_Processing#10-laplacian---code)
11. [Laplacian+Gaussian](https://github.com/BhanuPrakashNani/Image_Processing#11-laplaciangaussian---code)
12. [Laplacian, Sobel, CannyEdge](https://github.com/BhanuPrakashNani/Image_Processing#12-laplacian-sobel-cannyedge---code)
13. [Sobel-X and Y](https://github.com/BhanuPrakashNani/Image_Processing#13-sobel-x-and-y---code)
14. [Histogram Equalisation](https://github.com/BhanuPrakashNani/Image_Processing#14-histogram-equalisation---code)
15. [Normalize Histogram](https://github.com/BhanuPrakashNani/Image_Processing#15-normalize-histogram---code)
16. [Image Temperature](https://github.com/BhanuPrakashNani/Image_Processing#16-image-temperature---code)
17. [Box Filter](https://github.com/BhanuPrakashNani/Image_Processing#17-box-filter---code)
18. [GaussianFilter+Kernels](https://github.com/BhanuPrakashNani/Image_Processing#18-gaussianfilterkernels---code)
19. [Morphological Processing](https://github.com/BhanuPrakashNani/Image_Processing#19-morphological-processing--code)
20. [Morphological Text Processing](https://github.com/BhanuPrakashNani/Image_Processing#20-morphological-text-processing---code)
21. [Morphological Fingerprint Processing](https://github.com/BhanuPrakashNani/Image_Processing#21-morphological-fingerprint-processing---code)
22. [Morphological Outline](https://github.com/BhanuPrakashNani/Image_Processing#22-morphological-outline---code)
23. [Capture Video Frames](https://github.com/BhanuPrakashNani/Image_Processing#23-capture-video-frames---code)
24. [Video background Subtraction](https://github.com/BhanuPrakashNani/Image_Processing#24-video-background-subtraction---code)
25. [VideoCapture_GoogleColab](https://github.com/BhanuPrakashNani/Image_Processing#25-videocapture_googlecolab---code)
26. [Contours-OpenCV](https://github.com/BhanuPrakashNani/Image_Processing#26-contours-opencv---code)
27. [Fitting Polygons](https://github.com/BhanuPrakashNani/Image_Processing#27-fitting-polygons---code)
28. [Hough Lines](https://github.com/BhanuPrakashNani/Image_Processing#28-hough-lines---code)
29. [Adaptive+Gaussian Thresholding](https://github.com/BhanuPrakashNani/Image_Processing#29-adaptivegaussian-thresholding---code)
30. [OTSU Thresholding](https://github.com/BhanuPrakashNani/Image_Processing#30-otsu-thresholding---code)
31. [Grabcut](https://github.com/BhanuPrakashNani/Image_Processing#31-grabcut---code)
32. [Discrete Fourier Transformation](https://github.com/BhanuPrakashNani/Image_Processing#32-discrete-fourier-transformation---code)
33. [OpenCV KMeans](https://github.com/BhanuPrakashNani/Image_Processing#33-opencv-kmeans---code)
34. [Object Movement Tracking](https://github.com/BhanuPrakashNani/Image_Processing#34-object-movement-tracking---code)
35. [Live Hand Gesture Recognition](https://github.com/BhanuPrakashNani/Image_Processing#35-live-hand-gesture-recognition---code)

Before we jump into the concepts, let us once have a look at the definition of Image Processing.

## A Glance into Image Processing
Image processing is often viewed as arbitrarily manipulating an image to achieve an aesthetic standard or to support a preferred reality. However, image processing is more accurately defined as a means of translation between the human visual system and digital imaging devices. The human visual system does not perceive the world in the same manner as digital detectors, with display devices imposing additional noise and bandwidth restrictions. Salient differences between the human and digital detectors will be shown, along with some basic processing steps for achieving translation. Image processing must be approached in a manner consistent with the scientific method so that others may reproduce, and validate, one's results. This includes recording and reporting processing actions, and applying similar treatments to adequate control images.[Src](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3635309/)

There are two types of methods used for image processing namely, analogue and digital image processing. Analogue image processing can be used for the hard copies like printouts and photographs. Various fundamentals of interpretation are used by the Image Analysts along with the visual techniques. Digital image processing deals with manipulation of digital images through a digital computer. It is a subfield of signals and systems but focus particularly on images. The three general phases that all types of data have to undergo while using digital techniques are  
  * Pre-processing
  * Enhancement and Display
  * Information Extraction.
  
  ![Fundamental Steps in DIP](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/images/DIP.png)
   Fundamental Steps in Digital Image Processing - Rafael Gonzalez - 4th Edition [Src](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Digital_Image_Processing%2C_4th%20Edition-Rafael%20Gonzalez.pdf)

**Important point** to note while going through any concept is that the image is considered on a grey scale since color increases the complexity of the model. One may want to introduce an image processing tool using gray level images because of the format of gray level images because the inherent complexity of gray level images is lower than that of color images. In most cases. after presenting a gray-level image method, it can be be extended to color images.

Forgetting deeper insights into any of the concepts, I suggest you to go through [Digital Image Processing, Rafael C. Gonzalez • Richard E. Woods, 4th Edition](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Digital_Image_Processing%2C_4th%20Edition-Rafael%20Gonzalez.pdf) 

From here on I will be referring Digital Image Processing as DIP.
Disclaimer: I am not the original author of the images used. They have been taken from various Image Processing sites. I have mentioned all of the referenced sites. Pardon if I missed any.

The following is the order I suggest to look into the concepts.
### 1. Basics with Images - [Averaging Images](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Image%20Averaging)
Image averaging is a DIP technique that is used to enhance the images which are corrupted with random noise. The arithmetic mean of the intensity values for each pixel position is computed for a set of images of the same viewfield. The basic formula behind it is.  
![Image Averaging over set of N images](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/images/averaging.png)  

### 2. Successive Rotations - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Successive%20Rotations)
The images are rotated using the self-defined code for rotation instead of the OpenCV inbuilt function. When an image is rotated by 45 degrees for 8 times, it does not produce the same result as when it is rotated by 90 degrees for 4 times. This is because, when an image is rotated 45 degrees, during the rotation more number of pixels values for the new position of the pixels is to be calculated. And calculating these new pixel positions and their intensities uses interpolation which are basically approximation methods. So when an image is rotated by 90 degrees there is a smoother transition since less no of approximations are to be made for the new pixel positions and their intensities. 

A clear example is shown below

Rotated by 45 deg - 8 times |Rotated by 90 deg - 4 times  
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Successive%20Rotations/rotated45.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Successive%20Rotations/rotated90.jpg)

### 3. Interpolations - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Interpolations)
Interpolation is used in tasks such as zooming, shrinking, rotating, and geometrically correcting digital images. It is the process of using known data to estimate values at unknown locations. So for giving the chance to estimate values, we will do some transformation, here it is rotation by 45 degrees. The 3 interpolations we see here are:

Nearest Neighbour         |  Bilinear         |  Bicubic
:-------------------------:|:-------------------------:|:------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Interpolations/Nearest%20Neighbour.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Interpolations/Bilinear.jpg) | ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Interpolations/Bicubic.jpg)  

Here you can see a slight variation between the 3 images. The smoothness gets better from left to right. Since Bicubic interpolation uses a higher order equation it is able to capture features in depth.

### 4. Interpolation-Inverse Mapping - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Interpolation-Inverse%20Mapping)
As mentioned [here](https://www.cs.princeton.edu/courses/archive/fall00/cs426/papers/beier92.pdf), there are two methods of mapping, the first, called forward mapping, scans through the source image pixel by pixel, and copies them to the appropriate place in the destination image. The second, reverse mapping, goes through the destination image pixel by pixel, and samples the correct pixel from the source image. The most important feature of inverse mapping is that every pixel in the destination image gets set to something appropriate. In the forward mapping case, some pixels in the destination might not get painted, and would have to be interpolated. We calculate the image deformation as a reverse mapping.


Original | Nearest Neighbour - Inverse Mapping  
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Interpolation-Inverse%20Mapping/original.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Interpolation-Inverse%20Mapping/NearestNeighbour.jpg)


### 5. Basic Transformations - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Basic%20Transformations)
We have seen the basic transformations like rotation and scaling. Now lets see one more basic transformation known as translation.
Original | Translation  
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Basic%20Transformations/calvinHobbes.jpeg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Basic%20Transformations/Translation.jpg)

### 6. Perspective Transformation - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Perspective%20Transformation)
The perspective transformation deals with the conversion of 3d world into 2d image for getting better insights about the required information. The 3D object co-ordinates are changed into the co-ordinates wrt world frame of reference and then according to camera coordiante frame reference then continued by changing into Image Plave 2D coordinates and then to the pixel co-ordinates. 

Distorted Image         |  OpenCV - Perspective Transf Function         |  Manual Correction
:-------------------------:|:-------------------------:|:------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Perspective%20Transformation/chDistorted.jpeg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Perspective%20Transformation/ch.jpeg) | ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Perspective%20Transformation/ch.jpg)  

### 7. Est. Transformation - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Est.%20Transformation)
This is just and example of using custom transformations for the required purpose. In the below example I have tried to extract the root part from the image.

Original | Transformed  
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Est.%20Transformation/1.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Est.%20Transformation/image.jpg)  

### 8. Log and Contrast Stretching - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Log%20and%20Contrast_Stretching)
One of the grey-level transformations is Logarithmic Transformation. It is defined as ```s = c*log(r+1)``` , where 's' and 'r' are the pixel values of the output and the input image respectively and 'c' is a constant. 

Original | Log-Transformed  
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Log%20and%20Contrast_Stretching/log.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Log%20and%20Contrast_Stretching/log_transformed.jpg)  

Contrast Stretching is a simple image enhancement technique that attempts to improve the contrast in an image by stretching the range of intensity values it contains to span a desired range of values.

Original | Contrast Stretched 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Log%20and%20Contrast_Stretching/log.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Log%20and%20Contrast_Stretching/contrast_stretch.jpg)

### 9. Shading Correction - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Shading%20Correction)
Shading Correction is used for correcting the parts of an image which are having some faults due to multiple reasons like, camera light obstruction. So correcting the image for required purpose is essential. So in this example we have used a faulty image of a chessboard and corrected the image. Gaussian Blur is used to correct the shading in the corner of the image.

Original | Corrected Image 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Shading%20Correction/ChessBoardGrad.png)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Shading%20Correction/Converted.png)

### 10. Laplacian - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Laplacian)
A Laplacian filter is an edge detector which computes the second derivatives of an image, measuring the rate at which the first derivatives change. That determines if a change in adjacent pixel values is from an edge or continuous progression.
A laplacian filter or kernel looks like this:  
 	\[0,  1, 0]  
	\[1, -4, 1]  
	\[0,  1, 0]  
 
 But a point to note is that Laplacian is very sensitive to noise. It even detects the edges for the noise in the image.
 
 Original | Laplacian Filter 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian/original.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian/laplacian.jpg)
 
### 11. Laplacian+Gaussian - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Laplacian%2BGaussian)
As you can see from the above example, the Laplacian kernel is very sensitive to noise. Hence we use Gaussian Filter to first smoothen the image and remove the noise. And then the Laplacian Filter is applied for better results.

Laplacian | Gaussian and Laplacian 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian%2BGaussian/Laplacian.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian%2BGaussian/Gaussian%20%2B%20Laplacian.jpg)
### 12. Laplacian, Sobel, CannyEdge - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Laplacian%2C%20Sobel%2C%20CannyEdge)
The **Sobel filter** is used for edge detection. It works by calculating the gradient of image intensity at each pixel within the image. There are two sobel filters- SobelX and SobelY  
  SobelX   |    SobelY  
[-1, 0, 1]   [-1, -2, -1]  
[-2, 0, 2]   [ 0,  0,  0]  
[-1, 0, 1]   [ 1,  2,  1]  
	
Original         |  SobelX         |  SobelY
:-------------------------:|:-------------------------:|:------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian%2C%20Sobel%2C%20CannyEdge/originallenna.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian%2C%20Sobel%2C%20CannyEdge/SobelXLenna.jpg) | ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian%2C%20Sobel%2C%20CannyEdge/SobelYLenna.jpg) 

But the important thing to note here is, we have to pad the image before applying these filters to preserve the features of the image at the edges. I have used zero padding here to pad the image on the four sides.

**Canny Edge Detection** is a multi-stage algorithm  consisting of the following:
  1. **Noise Reduction** - Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter.  
  2. **Intensity Gradient** - Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction (Gx) and vertical direction (Gy). 
  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/images/gradient.png)
  3. **Non Maximum Supression** - After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient.
  4. **Hysteresis Thresholding** - This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to "sure-edge" pixels, they are considered to be part of edges. Otherwise, they are also discarded.
  This is an excerpt from [OpenCV Canny Edge Detection](https://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html).

Original | Canny Edge 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian%2C%20Sobel%2C%20CannyEdge/originallenna.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Laplacian%2C%20Sobel%2C%20CannyEdge/CannyLenna.jpg) 

### 13. Sobel-X and Y - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Sobel-X%20and%20Y)
As we have seen Laplacian previously, lets compare it with the Sobel Filters. 
Laplacian        |  SobelX         |  SobelY
:-------------------------:|:-------------------------:|:------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Sobel-X%20and%20Y/LaplacianLenna.png)  |    ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Sobel-X%20and%20Y/SobelXLenna.jpg) |   ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Sobel-X%20and%20Y/SobelYLenna.jpg)  

Because the second-order derivatives in Laplacian, this gradient operator is more sensitive to noise than first-order gradient operators. Also the thresholded magnitude of Laplacian operator produces double edges. For these reasons, together with its inability to detect the edge direction, the Laplacian as such is not a good edge detection operator. A better utilization of it is to use its zero-crossing to detect the edge locations.

### 14. Histogram Equalisation - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Histogram%20Equalisation)
A histogram of an image is nothing but the graphical representation of the intensity distribution of an image, quantifying the number of pixels for each intensity value. **Histogram Equalization** a method that improves the contrast in an image, in order to stretch out the intensity range.

As per [OpenCV Documentation](https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html):
  * Equalization implies mapping one distribution (the given histogram) to another distribution (a wider and more uniform distribution of intensity values) so the intensity values are spread over the whole range.

  * To accomplish the equalization effect, the remapping should be the cumulative distribution function (cdf) (more details, refer to Learning OpenCV). For the histogram H(i), its cumulative distribution H′(i) is:
  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/images/f.png)
  
 So, here I take an example image, plot its histogram and then equalize it.
 
 Original Hist | Equalized Hist 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Histogram%20Equalisation/hist.png)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Histogram%20Equalisation/equal-hist.png)

How the image looks after equalising the histogram.  

![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Histogram%20Equalisation/Equalized%20Image.png)

### 15. Normalize Histogram - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Normalize%20Histogram)
Image Normalization is a process in which we change the range of pixel intensity values to make the image more familiar or normal to the senses. Often image normalization is used for increasing contrast and removing noise. In a normalized image Mean = 0 and Variance = 1. In the following example, there is a very slight change, which may or may not be visible to us at times. But the main concept behind normalization is to bring the intensity values to a normal level which can be used for further processing.

 Equalized Hist | Normalized Hist 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Normalize%20Histogram/equilised.jpg)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Normalize%20Histogram/norm.png)

### 16. Image Temperature - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Image%20Temperature)
To increate the temperature of an image, I have used Look-up Table(LUT) and Univariate Spline. An LUT transformation assigns a new pixel value to each pixel in the input image according to the values given by a table. In this table, the index represents the input intensity value and the content of the cell given by the index represents the corresponding output value. A Univariate Spline is a one-dimensional smoothing spline that fits a given set of data points.

 Original | Temperature Increase 
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Image%20Temperature/hist.png)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Image%20Temperature/warmed.jpg)

### 17. Box Filter - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Box%20Filter)
By convolving the image with a normalized box filter, it takes the average of all the pixels under kernel area and replaces the central element with this average. Either of cv2.blur() or cv2.boxFilter() can be used for the same.

 Original | Box Filter
:--------------------------:|:--------------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Box%20Filter/orig.png)  |  ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Box%20Filter/boxfil.png)

### 18. GaussianFilter+Kernels - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/GaussianFilter%2BKernels)
Instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used before applying the other edge-detection kernels for better results. Gaussian Filter is very effective in removing the Gaussian noise and improves the accuracy of the other kernels like Laplacian and Sobel. To show the exact working of Laplacian and Sobel, I had used Gaussian Filter in the previous implementations. Because those kernels are not effective without Gaussian Blurring, I haven't shown that.

### 19. Morphological Processing -[Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Morphological%20Processing)
Morphological transformations are some simple operations based on the image shape. And they are performed on binary images with the help of kernels which decide the nature of the operation. Some of the mostly used operation are:  
  * Erosion - It erodes away the boundaries of foreground object. All the pixels near boundary will be discarded depending upon the size of kernel  
  * Dilation - It is just opposite of erosion. It increases the white region in the image or size of foreground object increases.  
  * Opening - Erosion followed by dilation is called opening.  
  * Closing - Dilation followed by Erosion is called closing.  
  * Morphological Gradient - Difference between Dialtion and erosion of an image.
  
  Erosion        |  Dilation         
:-------------------:|:-------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Processing/Erosion.png)  |    ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Processing/Dilation.png)

  Opening        |  Closing         
:-------------------:|:-------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Processing/Opening.png)  |    ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Processing/Closing.png)
 

### 20. Morphological Text Processing - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Morphological%20Text%20Processing)
I have used multiple combinations of the above mentioned morphological operations to enhance an image of text. I am mentioning some of the processed images here. For more images, please got to the [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Morphological%20Text%20Processing) here.

Original        |  Processed 1         |  Processed 2
:-------------------------:|:-------------------------:|:------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Text%20Processing/improved.jpg)  |    ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Text%20Processing/Processed%201.png) |   ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Text%20Processing/Processed%202.png)  

### 21. Morphological Fingerprint Processing - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Morphological%20Fingerprint%20Processing)
In this example too, I have tried out different combinations possible with various kernel sizes to give a better insights of the morphological operations and their effects on an image.

  Original        |  Improved         
:-------------------:|:-------------------:
![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Fingerprint%20Processing/Input.png)  |    ![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Fingerprint%20Processing/Improved.png)

### 22. Morphological Outline - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Morphological%20Outline)
It is the difference between dilation and erosion of an image.  

<img src="https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Morphological%20Outline/Outline.png" alt="drawing" width="300"/>

### 23. Capture Video Frames - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Capture%20Video%20Frames)
OpenCV function for capturing video frames is ``` vid = cv2.VideoCapture ```. Using ``` vid.read()``` we can fetch each fram from the video.

### 24. Video background Subtraction - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Video%20background%20Subtraction)
For subtracting a static background from the vido0 frames I have used multiple methods. The first one is to iteratively subtract the background image from each frame and then display on the screen. The other method consists of using ``` cv2.createBackgroundSubtractorMOG2()``` in OpenCV and creating a mask with that background subtractor. After background subtraction, I have used various thresholdings for enhancing the objects entering into the video frames(since everytime the background gets subtracted, the new objects get highlighted). I have used Adaptive thresholding, Inverse Binary thresholding and drew contours on them for extra effects. The same can be seen in the GIF below.

![](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/Video%20background%20Subtraction/ezgif.com-video-to-gif.gif)

### 25. VideoCapture_GoogleColab - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/VideoCapture_GoogleColab)
This is a script for enthusiasts working in various project in Google Colab which uses the web cam. Since Google Colab has no access t our hardware, we need to use this script for enabling web cam. This is not my code and has been taken from [here](https://colab.research.google.com/notebooks/snippets/advanced_outputs.ipynb#scrollTo=buJCl90WhNfq) for better reach.

### 26. Contours-OpenCV - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Contours-OpenCV)

### 27. Fitting Polygons - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Fitting%20Polygons)

### 28. Hough Lines - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Hough%20Lines)

### 29. Adaptive+Gaussian Thresholding - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Adaptive%2BGaussian%20Thresholding)

### 30. OTSU Thresholding - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/OTSU%20Thresholding)

### 31. Grabcut - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Grabcut)

### 32. Discrete Fourier Transformation - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Discrete%20Fourier%20Transformation)

### 33. OpenCV KMeans - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/OpenCV%20KMeans)

### 34. Object Movement Tracking - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Object%20Movement%20Tracking)

### 35. Live Hand Gesture Recognition - [Code](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Live%20Hand%20Gesture%20Recognition)



### Resources
I am mentioning some of the resources which I found very useful during my learning stage.
  1. [OpenCV Documentation](https://docs.opencv.org/master/)
  2. [PyImageSearch Image Processing Archives](https://www.pyimagesearch.com/category/image-processing/)
  3. [OpenCV Python Tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html#py-table-of-content-imgproc)

### Contributors
I thank the contributors for helping with implementing few of the concepts.
  * [Akhil Kolla](https://github.com/kolla47/)
  * [Vishnu Priya](https://github.com/vishnu2112)

### License
[MIT LICENSE](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/LICENSE.txt)
