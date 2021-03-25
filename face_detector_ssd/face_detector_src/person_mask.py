import cv2

class Mask:
    def __init__(self, backgroundFrame):
        self.background = backgroundFrame

    def create(self, frame, blurKernel):
        self.frame = frame
        self.frame_copy = frame
        self.Kernel = blurKernel
        
        background_gray = cv2.cvtColor(self.background, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        difference = cv2.absdiff(frame_gray, background_gray)
        
        difference_blur = cv2.GaussianBlur(difference, (self.Kernel, self.Kernel), 0)
        
        binary_mask = cv2.threshold(difference, 0, 1, cv2.THRESH_BINARY+
                                                        cv2.THRESH_OTSU)[1]

        masked_frame = cv2.bitwise_and(self.frame_copy, self.frame_copy, mask=binary_mask)

        return masked_frame


    def create_box(self, frame, blurKernel):
        self.frame = frame
        self.frame_copy = frame
        self.Kernel = blurKernel
        
        background_gray = cv2.cvtColor(self.background, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        difference = cv2.absdiff(frame_gray, background_gray)
        
        frame_blur = cv2.GaussianBlur(difference, (self.Kernel, self.Kernel), 0)
        
        binary_mask = cv2.threshold(frame_blur, 0, 255, cv2.THRESH_BINARY+
                                                        cv2.THRESH_OTSU)[1]
        frame_canny = cv2.Canny(binary_mask, 100, 200)
        all_cnts = cv2.findContours(frame_canny.copy(), cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)[0]
       
        sorted_cnts = sorted(all_cnts, key=cv2.contourArea, reverse=True)
        cnts = sorted_cnts[:1]

        for cnt in all_cnts:
            hull = cv2.convexHull(cnt)
            x,y,w,h = cv2.boundingRect(hull)
            #if y > 200:  #Disregard item that are the top of the picture
            cv2.rectangle(self.frame_copy,(x,y),(x+w,y+h),(0,255,0),2)

        #masked_frame = binary_mask * frame_gray
        #masked_frame = cv2.bitwise_and(self.frame_copy, self.frame_copy, mask=binary_mask)

        return self.frame_copy
        