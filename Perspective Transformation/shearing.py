class RandomShear(object):
    """Randomly shears an image in horizontal direction   
    
    
    Bounding boxes which have an area of less than 25% in the remaining in the 
    transformed image is dropped. The resolution is maintained, and the remaining
    area if any is filled by black color.
    
    Parameters
    ----------
    shear_factor: float or tuple(float)
        if **float**, the image is sheared horizontally by a factor drawn 
        randomly from a range (-`shear_factor`, `shear_factor`). If **tuple**,
        the `shear_factor` is drawn randomly from values specified by the 
        tuple
        
    Returns
    -------
    
    numpy.ndaaray
        Sheared image in the numpy format of shape `HxWxC`
    
    numpy.ndarray
        Tranformed bounding box co-ordinates of the format `n x 4` where n is 
        number of bounding boxes and 4 represents `x1,y1,x2,y2` of the box
        
    """

def __init__(self, shear_factor = 0.2):
    self.shear_factor = shear_factor
    
    if type(self.shear_factor) == tuple:
        assert len(self.shear_factor) == 2, "Invalid range for scaling factor"   
    else:
        self.shear_factor = (-self.shear_factor, self.shear_factor)
    
    shear_factor = random.uniform(*self.shear_factor)


def __call__(self, img, bboxes):

    shear_factor = random.uniform(*self.shear_factor)

    w,h = img.shape[1], img.shape[0]

    if shear_factor < 0:
        img, bboxes = HorizontalFlip()(img, bboxes)

    M = np.array([[1, abs(shear_factor), 0],[0,1,0]])

    nW =  img.shape[1] + abs(shear_factor*img.shape[0])

    bboxes[:,[0,2]] += ((bboxes[:,[1,3]]) * abs(shear_factor) ).astype(int) 


    img = cv2.warpAffine(img, M, (int(nW), img.shape[0]))

    if shear_factor < 0:
        img, bboxes = HorizontalFlip()(img, bboxes)

    img = cv2.resize(img, (w,h))

    scale_factor_x = nW / w

    bboxes[:,:4] /= [scale_factor_x, 1, scale_factor_x, 1] 


    return img, bboxes

# from data_aug.bbox_utils import *
import matplotlib.pyplot as plt
import cv2

(h,w) = img.shape[:2]
center = (w/2, h/2)

M = cv2.getRotationMatrix2D(center, angle30, scale)

abs_cos = abs(M[0,0]) 
abs_sin = abs(M[0,1])


bound_w = int(h * abs_sin + w * abs_cos)
bound_h = int(h * abs_cos + w * abs_sin)

M[0, 2] += bound_w/2 - center[0]
M[1, 2] += bound_h/2 - center[1]

rotated30 = cv2.warpAffine(img, M, (bound_w,bound_h))

  
shear = RandomShear(0.7)


plt.imshow(draw_rect(img, bboxes))