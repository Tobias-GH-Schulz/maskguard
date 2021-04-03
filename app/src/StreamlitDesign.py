import streamlit as st
from PIL import Image

class StreamlitDesign():
    @staticmethod

    def content():
        icon = Image.open("images/logo_symbol.png")
        st.set_page_config(
            page_title="MASK GUARD",
            page_icon=icon,
            layout="wide",
            initial_sidebar_state="auto",
            )

        col1, col2, col3 = st.beta_columns([1,3,1])
        col1.header(" ")
        col2.header(" ")
        image1 = Image.open("images/logo_large.png")
        col2.image(image1, use_column_width = True)
        col3.header(" ")

        st.write(" ")
        st.markdown("<h2 style='text-align: center; color: black;'>Are you looking for a way to make your business a safer place during this corona pandemic?</h2>", unsafe_allow_html=True)
        st.write(" ")

        col1, col2, col3 = st.beta_columns([2,3,1])
        col1.header(" ")
        col2.header(" ")
        col2.markdown("![Gif](https://media.giphy.com/media/zCbtS0oW5na1ttTVVf/giphy.gif)")
        col3.header(" ")
        
        st.title("Why Mask Guard?")
        st.markdown("""
                    We are living in the dangerous and uncertain time of a pandemic.
                    A huge amount of SMBs has been closed down by the authorities 
                    during the pandemic. Do you also want to be one of them because your 
                    business has been declared a super spreader location? 
                    Of course not! And thats why we invented the Mask Guard, a Mask-No-Mask 
                    detector that detects if your customers are wearing a mask or not and only 
                    lets them enter your business if they are wearing one. 
                    Our highly educated team put all their knowledge in deep learning and computer vision 
                    together to create a tool that gives you one thing that lets you and also your customers
                    sleep well at night: SECURITY!
                    """)

    def features(self):
        col1, col2 = st.beta_columns([1, 2])
        st.markdown("<h1 style='text-align: left; color: black;'>Features</h1>", unsafe_allow_html=True)
        bgcolor = "#ffffff"
        fontcolor = "#ff0000"
        html_line = """
        <hr style="height:1px;border-width:0;color:{};background-color:{}">
        """
        st.markdown(html_line.format(bgcolor,fontcolor),unsafe_allow_html=True)
        sceme = Image.open("images/Features/Mask_detector_sceme.png")
        st.image(sceme)

        st.markdown("<h2 style='text-align: left; color: black;'>1. Image optimizer</h2>", unsafe_allow_html=True)
        with st.beta_expander("Read about it:"):
            '''st.write("""The potential places in which Mask Guard will be used differ a lot and so will the lighting conditions. 
                        To prepare the detector as best as possible for different environments we implemented an image optimization 
                        stage. In the current version of Mask Guard the optimizer uses adaptive contrast stretching. 
                        Therefore the frame is splitted into H, S, and V channel to adjust the original image depending 
                        on the mean pixel value in the V channel.""")'''
            '''col1, col2, col3 = st.beta_columns([12,12,13])
            with col1:
                st.markdown("<h4 style='text-align: center; color: black;'>Original image</h4>", unsafe_allow_html=True)
                original_image = Image.open("images/Image_optimizer/Original_image.png")
                st.image(original_image)
            with col3:
                st.markdown("<h4 style='text-align: center; color: black;'>HSV cylinder</h4>", unsafe_allow_html=True)
                hsv_image = Image.open("images/Image_optimizer/hsv.jpg")
                st.image(hsv_image, use_column_width=False)
            with col2:
                st.markdown("<h4 style='text-align: center; color: black;'>Optimized image</h4>", unsafe_allow_html=True)
                optimized_image = Image.open("images/Image_optimizer/Optimized_image.png")
                st.image(optimized_image)
            '''
            col0, col1, col2, col3 = st.beta_columns([9,12,12,9])
            with col0:
                st.write(" ")

            with col1:
                st.markdown("<h4 style='text-align: center; color: black;'>Original image</h4>", unsafe_allow_html=True)
                original_image = Image.open("images/Image_optimizer/Original_image.png")
                st.image(original_image)

                st.write(" ")
                st.write("""The potential places in which Mask Guard will be used differ a lot and so will the lighting conditions. 
                        To prepare the detector as best as possible for different environments we implemented an image optimization 
                        stage. In the current version of Mask Guard the optimizer uses adaptive contrast stretching. 
                        Therefore the frame is splitted into H, S, and V channel to adjust the original image depending 
                        on the mean pixel value in the V channel.""")

                st.write(" ")
                st.write(" ")
                st.markdown("<h4 style='text-align: center; color: black;'>Optimized image</h4>", unsafe_allow_html=True)
                optimized_image = Image.open("images/Image_optimizer/Optimized_image.png")
                st.image(optimized_image)
            with col2:
                st.markdown("<h4 style='text-align: center; color: black;'> </h4>", unsafe_allow_html=True)
                arrow_right = Image.open("images/Image_optimizer/Arrow_right.png")
                st.image(arrow_right)
            
                st.markdown("<h4 style='text-align: center; color: black;'>HSV cylinder</h4>", unsafe_allow_html=True)
                hsv_image = Image.open("images/Image_optimizer/hsv.jpg")
                st.image(hsv_image, use_column_width=True)

                st.markdown("<h4 style='text-align: center; color: black;'> </h4>", unsafe_allow_html=True)
                arrow_left = Image.open("images/Image_optimizer/Arrow_left.png")
                st.image(arrow_left)

            with col3:
                st.write(" ")
                

        st.markdown("<h2 style='text-align: left; color: black;'>2. Motion detector</h2>", unsafe_allow_html=True)
        with st.beta_expander("Read about it:"):
            col1, col2, col3, col4, col5, col6, col7 = st.beta_columns(7)
            with col1:
                st.markdown("<h4 style='text-align: center; color: black;'>1. Captured background</h4>", unsafe_allow_html=True)
                background_frame = Image.open("images/Motion_detector_images/background_frame.png")
                st.image(background_frame)
                st.markdown("<p style='text-align: center; color: black;'>The motion detector first captures an image of the background to later isolate only the moving parts in the image. The motion detector only works on a static camera such as CCTV.</p>", unsafe_allow_html=True)
            with col2:
                st.markdown("<h4 style='text-align: center; color: black;'>2. Differenced frame</h4>", unsafe_allow_html=True)
                differenced_frame = Image.open("images/Motion_detector_images/differenced_frame.png")
                st.image(differenced_frame) 
                st.markdown("<p style='text-align: center; color: black;'>To isolate only the elements in the image that are moving cv2.absdiff() is used. The output image still contains some noise that need to be erased in the next steps.</p>", unsafe_allow_html=True)
            with col3:
                st.markdown("<h4 style='text-align: center; color: black;'>3. Thresholded frame</h4>", unsafe_allow_html=True)
                thresholded_frame = Image.open("images/Motion_detector_images/thresholded_frame.png")
                st.image(thresholded_frame)
                st.markdown("<p style='text-align: center; color: black;'>The difference between background and current frame now gets thresholded so that pixel values above 50 will be 255 (white) and pixel values below 50 will be 0 (black).</p>", unsafe_allow_html=True)             
            with col4:
                st.markdown("<h4 style='text-align: center; color: black;'>4. Opened frame</h4>", unsafe_allow_html=True)
                opened_frame = Image.open("images/Motion_detector_images/opened_frame.png")
                st.image(opened_frame)
                st.markdown("<p style='text-align: center; color: black;'>To reduce the remaining small noise on the thresholded image even more a combination of erosion and dilation ('opening') is used.</p>", unsafe_allow_html=True)                            
            with col5:
                st.markdown("<h4 style='text-align: center; color: black;'>5. Dilated frame</h4>", unsafe_allow_html=True)
                dilated_frame = Image.open("images/Motion_detector_images/dilated_frame.png")
                st.image(dilated_frame)      
                st.markdown("<p style='text-align: center; color: black;'>So far the recieved image is a bit scattared. To generate clearer areas of interest the opened image gets dilated a lot more.</p>", unsafe_allow_html=True)                            
            with col6:
                st.markdown("<h4 style='text-align: center; color: black;'>6. Found contours</h4>", unsafe_allow_html=True)
                original_frame = Image.open("images/Motion_detector_images/original_frame.png")
                st.image(original_frame)
                st.markdown("<p style='text-align: center; color: black;'>In this step cv2.findContours() finds the contours of all elements that differ between background and current frame.</p>", unsafe_allow_html=True)                                  
            with col7:
                st.markdown("<h4 style='text-align: center; color: black;'>7. Crop original image</h4>", unsafe_allow_html=True)
                original_frame = Image.open("images/Motion_detector_images/cropped_frame.png")
                st.image(original_frame)
                st.markdown("<p style='text-align: center; color: black;'>Bounding rectangles recieved from the found contours are saved to crop the original image into small parts that probably contain faces and should be send to the face detector.</p>", unsafe_allow_html=True)                                  

        st.markdown("<h2 style='text-align: left; color: black;'>3. Face detector</h2>", unsafe_allow_html=True)
        with st.beta_expander("Read about it:"):
            st.write("""Face detection in general is a popular topic in biometrics and still evolves quickly. 
                    There are tons of surveillance cameras in public places and businesses which deliver a huge amount of images 
                    for face detection. The most important bottlenecks in applications like this are speed and accuracy to detect faces. 
                    In general the face detection network gets a BGR image (in our case a frame of the webcam stream) 
                    as input and produces a set of bounding boxes that might contain faces. All we need to do is just 
                    select the boxes with a strong confidence. Our face detector is based on a SSD framework (Single Shot MultiBox Detector), 
                    using a reduced ResNet-10 model.""")
            ssd = Image.open("images/Features/resnet_ssd.png")
            st.image(ssd)
            st.subheader("SSD:")
            st.write("""A Single-shot MultiBox Detector is a one-stage object detection algorithm. This means that, 
                    in contrast to two-stage models, SSDs do not need an initial object proposals generation step. 
                    This makes it, usually, faster and more efficient than two-stage approaches such as Faster R-CNN, 
                    although it sacrifices performance for detection of small objects to gain speed.""")
            st.subheader("ResNet:")
            st.write("""Deep Residual Networks (ResNet) took the deep learning world by storm when Microsoft Research 
                        released Deep Residual Learning for Image Recognition. In the 2015 ImageNet and COCO competitions, 
                        which covered image classification, object detection, and semantic segmentation, these networks led 
                        to 1st-place winning entries in all five main tracks.
                        The robustness of ResNets has since been proven by various visual and non-visual tasks. The Network 
                        depth is of crucial importance in neural network architectures, but deeper networks are more 
                        difficult to train. The residual learning framework eases the training of these networks, and 
                        enables them to be substantially deeper, leading to improved performance in both visual and non-visual tasks.""")
        
        st.markdown("<h2 style='text-align: left; color: black;'>4. Mask-NoMask-Classifier</h2>", unsafe_allow_html=True)
        with st.beta_expander("Read about it:"):
            st.write("TEST")

        st.markdown("<h2 style='text-align: left; color: black;'>5. Distance measurement</h2>", unsafe_allow_html=True)
        with st.beta_expander("Read about it:"):
            st.write("""To detect the distance of peoples from the camera, the triangle similarity technique is used. 
                        During the camera calibration an image of a person with the head height H (we have assumed that 
                        the average height of humans head is 22 centimetres) has to be captured as a reference in a 
                        specified distance D (in centimetres) from the camera. After measuring the pixel height P of the 
                        person's head on the reference image, these values can be used to calculate the focal length of 
                        the camera with:""")
            st.latex(r""" F = {(P x D)\over H} """)

            st.write("""After calculating the focal length of the camera we can use a conversion of the formula to 
                        calculate the distance of the camera to different persons on each frame of our video stream: """)
            st.latex(r""" D' = {(H x F)\over P} """)
            st.write("""Since there can be n people detected in a video and we want to measure the distance between 
                        these peoples, the euclidean distance is calculated between the mid-points of the bounding boxes 
                        of all the detected faces. If the distance between two people is less than 150 centimetres, a 
                        red bounding box is displayed around the face indicating that they are not maintaining social distance. 
                        """)
        

        st.markdown("<h2 style='text-align: left; color: black;'>6. Audio alarm</h2>", unsafe_allow_html=True)
        with st.beta_expander("Hear it:"):
            
            col1, col2, col3 = st.beta_columns([1,2,2])
            with col1:
                st.write("The MASK GUARD comes equiped with a state of the art audio alarm system that ensures that no person without a mask secretly enters your business. You and your employees will instantly be aware of insecure indivduals.") 
            with col2:
                st.write("As soon as one person on the image is detected as not wearing a mask the system will play this alarm:")
                wear_mask = open('./src/utility/please_wear_mask.mp3', 'rb')
                wear_bytes = wear_mask.read()
                st.audio(wear_bytes, format='audio/mp3')
            with col3:
                st.write("When all detected people on the image are wearing a mask the MASK GUARD will give them a nice 'Thank you message'.")
                thanks_mask = open('./src/utility/thanks_wear_mask.mp3', 'rb')
                thanks_bytes = thanks_mask.read()
                st.audio(thanks_bytes, format='audio/mp3')


        bgcolor = "#ffffff"
        fontcolor = "#ff0000"
        html_line = """
        <hr style="height:1px;border-width:0;color:{};background-color:{}">
        """
        st.markdown(html_line.format(bgcolor,fontcolor),unsafe_allow_html=True)

        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")


    def sidebar(self):
        with st.sidebar.beta_container():
            image1 = Image.open("images/logo_large.png")
            st.image(image1)
            
            st.markdown("<h3 style='text-align: center; color: black;'>The team behind MASK GUARD</h3>", unsafe_allow_html=True)

            team1, team2, team3 = st.beta_columns([1,2,1])
            with team1:
                st.markdown(" ")
            with team3:
                st.markdown(" ")
            with team2:
                st.image("images/Team/Aderemi.png",use_column_width=True)   
                st.markdown("[*Aderemi Fayoyiwa*](<https://github.com/AderemiF>)")
                st.image("images/Team/Marcin.png",use_column_width=True)            
                st.markdown("[*Marcin Szleszynski*](<https://github.com/martinezpl>)")
                st.image("images/Team/Tobi.png",use_column_width=True)
                st.markdown("[*Tobias Schulz*](<https://github.com/Tobias-GH-Schulz>)")

            st.write("""We are three students at Strive School who embarked on this project during the computer vision module. 
                        The goal was to train a model to detect if someone is wearing a face mask or not. We took the task up 
                        several notches by including other amazing features like image optimization, distance measurement and audio warning.
                        On this page we showcase the results of one week of work and are happy to update the application 
                        during the next months. Check out our GitHub repository and feel free to contact us if you have comments and ideas 
                        on improvements.""")

            #st.markdown('[./images/Links/GitHub_Logo.png "GitHub Logo"]("<https://github.com/Tobias-GH-Schulz/mask-detector>")'))

    def timeline(self):
        st.markdown("<h1 style='text-align: left; color: black;'>Road map</h1>", unsafe_allow_html=True)
        bgcolor = "#ffffff"
        fontcolor = "#ff0000"
        html_line = """
        <hr style="height:1px;border-width:0;color:{};background-color:{}">
        """
        st.markdown(html_line.format(bgcolor,fontcolor),unsafe_allow_html=True)
        timeline = Image.open("images/timeline.png")
        st.image(timeline)

    def end(self):
        col1, col2, col3 = st.beta_columns([1,2,1])
        with col1:
            st.write(" ") 
        with col2:
            st.subheader("Let's make the world a safer and healthier place.")
        with col3:
            st.write(" ")
