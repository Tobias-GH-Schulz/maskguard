import cv2
import numpy as np 
from PIL import Image

class BrightnessOptimizer:

    def optimize(self, frame):
        self.frame = frame
        self.frame_copy = frame

        hsv = cv2.cvtColor(self.frame_copy, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        if np.mean(v) > 120:
            return self.frame
        
        elif np.mean(v) > 100:
            alpha = 2
            beta = 10

        elif np.mean(v) > 80:
            alpha = 2
            beta = 20

        elif np.mean(v) > 60:
            alpha = 2
            beta = 30

        else:
            alpha = 2
            beta = 70
        
        new_image = cv2.addWeighted(self.frame, alpha, np.zeros(self.frame.shape, 
                                    self.frame.dtype), 0, beta)
        return new_image
    
    def image_agcwd(img, a=0.25, truncated_cdf=False):
        h,w = img.shape[:2]
        hist,bins = np.histogram(img.flatten(),256,[0,256])
        cdf = hist.cumsum()
        cdf_normalized = cdf / cdf.max()
        prob_normalized = hist / hist.sum()

        unique_intensity = np.unique(img)
        intensity_max = unique_intensity.max()
        intensity_min = unique_intensity.min()
        prob_min = prob_normalized.min()
        prob_max = prob_normalized.max()
        
        pn_temp = (prob_normalized - prob_min) / (prob_max - prob_min)
        pn_temp[pn_temp>0] = prob_max * (pn_temp[pn_temp>0]**a)
        pn_temp[pn_temp<0] = prob_max * (-((-pn_temp[pn_temp<0])**a))
        prob_normalized_wd = pn_temp / pn_temp.sum() # normalize to [0,1]
        cdf_prob_normalized_wd = prob_normalized_wd.cumsum()
        
        if truncated_cdf: 
            inverse_cdf = np.maximum(0.7,1 - cdf_prob_normalized_wd)
        else:
            inverse_cdf = 1 - cdf_prob_normalized_wd
        
        img_new = img.copy()
        for i in unique_intensity:
            img_new[img==i] = np.round(255 * (i / 255)**inverse_cdf[i])
    
        return img_new

    def process_bright(img):
        img_negative = 255 - img
        agcwd = BrightnessOptimizer.image_agcwd(img_negative, a=0.25, truncated_cdf=False)
        reversed = 255 - agcwd
        return reversed

    def process_dimmed(img):
        agcwd = BrightnessOptimizer.image_agcwd(img, a=0.9, truncated_cdf=True)
        return agcwd


    def a_g_c(self, img):
        # Extract intensity component of the image
        YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        Y = YCrCb[:,:,0]
        # Determine whether image is bright or dimmed
        threshold = 0.2
        exp_in = 150 # Expected global average intensity 
        M,N = img.shape[:2]
        mean_in = np.sum(Y/(M*N)) 
        t = (mean_in - exp_in)/ exp_in
        
        # Process image for gamma correction
        img_output = None
        if t < threshold: # Dimmed Image
            result = BrightnessOptimizer.process_dimmed(Y)
            YCrCb[:,:,0] = result
            img_output = cv2.cvtColor(YCrCb,cv2.COLOR_YCrCb2BGR)
        elif t > threshold: # Bright Image
            result = BrightnessOptimizer.process_bright(Y)
            YCrCb[:,:,0] = result
            img_output = cv2.cvtColor(YCrCb,cv2.COLOR_YCrCb2BGR)
        else:
            img_output = img

        return img_output        

    def ContrastStretching(self, img):
        # resizing using aspect ratio intact and finding the circle
        # reduce size retain aspect ratio intact
        # invert BGR 2 RGB
        RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        Ig = RGB[:, :, 2]
        [w,h] = np.shape(Ig)
        r=800.0/Ig.shape[1]
        dim=(800,int(Ig.shape[0]*r))
        rz = cv2.resize(Ig,dim,interpolation=cv2.INTER_AREA)
        #  convert in to float and get log trasform for contrast streching
        g = 0.96 * (np.log(1 + np.float32(rz)))
        # change into uint8
        cvuint = cv2.convertScaleAbs(g)
        # cvuint8.dtype
        ret, th = cv2.threshold(cvuint, 0, 255, cv2.THRESH_OTSU)
        ret1,th1 = cv2.threshold(Ig,0,255,cv2.THRESH_OTSU)
        # closeing operation
        # from skimage.morphology import disk
        # from skimage.morphology import erosion, dilation, opening, closing, white_tophat
        # selem = disk(30)
        # cls = opening(th, selem)
        # plot_comparison(orig_phantom, eroded, 'erosion')
        # in case using opencv
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35,35))
        cls = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
        Im = cls*rz # the mask with resize image
        # cv2.imwrite('mynew.jpg', mask)
        return (Im,th,th1,cls,g,RGB)


    def normalizeRed(intensity):
        iI      = intensity
        minI    = 86
        maxI    = 230
        minO    = 0
        maxO    = 255
        iO      = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
        return iO

    def normalizeGreen(intensity):
        iI      = intensity
        minI    = 90
        maxI    = 225
        minO    = 0
        maxO    = 255
        iO      = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
        return iO

    def normalizeBlue(intensity):
        iI      = intensity
        minI    = 100
        maxI    = 210
        minO    = 0
        maxO    = 255
        iO      = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
        return iO


    def ContrastStretching2(self, frame, intensity):              
        # Create an image object
        imageObject = Image.fromarray(frame)
        # Split the red, green and blue bands from the Image
        multiBands      = imageObject.split()

        # Apply point operations that does contrast stretching on each color band
        normalizedRedBand      = multiBands[2].point(BrightnessOptimizer.normalizeRed(intensity))
        normalizedGreenBand    = multiBands[1].point(BrightnessOptimizer.normalizeGreen(intensity))
        normalizedBlueBand     = multiBands[0].point(BrightnessOptimizer.normalizeBlue(intensity))
        # Create a new image from the contrast stretched red, green and blue brands
        normalizedImage = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))
        imgArray = np.asarray(im)[:,:,::-1].copy()

        return imgArray
