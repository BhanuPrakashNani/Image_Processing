# Image_Processing
Welcome aboard. With the growing technologies out in the world, we have seen how important aspect Image Processing has become. This repository provides a complete understanding of practical implementation of all the concepts to be known for a developer to start their Image Processing journey.  

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

The following is the order I suggest to look into the concepts.
### 1. Basics with Images - [Averaging Images](https://github.com/BhanuPrakashNani/Image_Processing/tree/master/Image%20Averaging)
Image averaging is a DIP technique that is used to enhance the images which are corrupted with random noise. The arithmetic mean of the intensity values for each pixel position is computed for a set of images of the same viewfield. The basic formula behind it is.  
![Image Averaging over set of N images](https://github.com/BhanuPrakashNani/Image_Processing/blob/master/images/averaging.png)  

### 2. Successive Rotations
### 3. Interpolations
### 4. Interpolation-Inverse Mapping
### 5. Basic Transformations
### 6. Perspective Transformation
### 7. Est. Transformation
### 8. Log and Linear Transformation
### 9. Shading Correction
### 10. Laplacian
### 11. Laplacian+Gaussian
### 12. Laplacian, Sobel, CannyEdge
### 13. Sobel-X and Y
### 14. Histogram Equalisation
### 15. Normalize Histogram
### 16. Image Temperature
### 17. Box Filter
### 18. GaussianFilter+Kernels
### 19. Morphological Processing
### 20. Morphological Text Processing
### 21. Morphological Fingerprint Processing
### 22. Morphological Outline
### 23. Capture Video Frames
### 24. Video background Subtraction
### 25. VideoCapture_GoogleColab
### 26. Contours-OpenCV
### 27. Fitting Polygons
### 28. Hough Lines
### 29. Adaptive+Gaussian Thresholding
### 30. OTSU Thresholding
### 31. Grabcut
### 32. Discrete Fourier Transformation
### 33. OpenCV KMeans
### 34. Object Movement Tracking
### 35. Live Hand Gesture Recognition



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
