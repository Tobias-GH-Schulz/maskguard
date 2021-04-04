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
            st.write("""The classifier has been trained on 2350 images, split equally in two classes. The dataset consists mostly of volounteers' 
                        selfies and an external Chinese dataset available on https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset. 
                        Model was validated on 784 images, and then tested on another 784 images. Class equality was preserved and the test accuracy was 0.985%.
                        We are constanly working on upgrading the quantity of data batches and the diversity of characters and perspectives, 
                        therefore improving the classifier. Classifier's accuracy should be tested on an external, truly random footage, which 
                        we are yet to acquire.""")
            st.write(" ")
            col1, col2, col3 = st.beta_columns([1, 2, 1])
            with col1:
                st.write(" ")
            with col2:
                st.markdown("<h3 style='text-align: center; color: black;'>Image examples from dataset</h3>", unsafe_allow_html=True)
                Mask_NoMask = ("images/Features/Mask_NoMask_Detector.png")
                st.image(Mask_NoMask, use_column_width=True)
            with col3:
                st.write(" ")
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
                st.write("""The MASK GUARD comes equiped with a state of the art audio alarm system that ensures that no person without 
                            a mask secretly enters your business. You and your employees will instantly be aware of insecure indivduals.""") 
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



    def sidebar(self):
        with st.sidebar.beta_container():
            image1 = Image.open("images/logo_large.png")
            st.image(image1)
            
            st.markdown("<h3 style='text-align: center; color: black;'>The team behind MASK GUARD</h3>", unsafe_allow_html=True)
            st.write(" ")
            
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
            
            st.write("""ABOUT US:""")
            st.write("""We are three students at Strive School who embarked on this project during the computer vision module. 
                        The goal was to train a model to detect if someone is wearing a face mask or not. We took the task up 
                        several notches by including other amazing features like image optimization, distance measurement and audio warning.
                        On this page we showcase the results of one week of work and are happy to update the application 
                        during the next months.""")

            github_base64 = """iVBORw0KGgoAAAANSUhEUgAAA+gAAAGaCAYAAACc1mkHAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA2hpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/
                            eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIF
                            hNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAy
                            LzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN
                            0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaW
                            dpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpGQTdGMTE3NDA3MjA2ODExQjM0QkRCMTI3QTg3OTlBMCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpDQjg3OEJGRTM4M0YxMUUzQTZEM
                            UI0MDIyQjJEMDFGNSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpDQjg3OEJGRDM4M0YxMUUzQTZEMUI0MDIyQjJEMDFGNSIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob
                            3AgQ1M2IChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6RDY1NjNCMTEzNDIwNjgxMTgwODNGMTQ4QTZCNTMyNkQiIHN0UmVmO
                            mRvY3VtZW50SUQ9InhtcC5kaWQ6RkE3RjExNzQwNzIwNjgxMUIzNEJEQjEyN0E4Nzk5QTAiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2t
                            ldCBlbmQ9InIiPz4OgPucAAAu90lEQVR42uzdCZgdVZk38IohgUCAlqZlh7DvO8qmgiCgILK4MKIo4oLjOA6ozKjo5+7ngqLgjDrgKCiyysinA4gMBMK+yg6yhR3sdGjCkkAI+d7jLZyek
                            KW7c2931anf73nepxoe6K56z7l17//WNmbu3LkFAAAAMLrGCOgAAAAgoAMAAAACOgAAAAjoAAAAgIAOAAAAAjoAAAAgoAMAAICADgAAAAjoAAAAIKADAAAAAjoAAAAI6AAAAICADgAAAAI6AAAAI
                            KADAACAgA4AAAAI6AAAACCgAwAAAAI6AAAACOgAAACAgA4AAAACOgAAACCgAwAAgIAOAAAACOgAAAAgoAMAAAACOgAAAAjoAAAAgIAOAAAAAjoAAAAgoAMAAICADgAAAAjoAAAAIKADAAAAAjoAAA
                            AI6AAAAICADgAAAAI6AAAAIKADAACAgA4AAAAI6AAAACCgAwAAAAI6AAAACOgAAACAgA4AAAACOgAAACCgAwAAgIAOAAAACOgAAAAgoAMAAAACOgAAAAjoAAAAgIAOAAAAAjoAAAAgoAMAAICADgAA
                            AAjoAAAAIKADAAAAAjoAAAAI6AAAAICADgAAAAI6AAAAIKADAACAgK4LAAAAIKADAAAAAjoAAAAI6AAAAICADgAAAAI6AAAAIKADAACAgA4AAAAI6AAAACCgAwAAAAI6AAAACOgAAACAgA4AAAACO
                            gAAACCgAwAAgIAOAAAACOgAAAAgoAMAAAACOgAAAAjoAAAAgIAOAAAAAjoAAAAgoA+3IWPGaMJi6OnqHheLlaNWL2vV9K+juqNWGFBLRS0TtVzUklFLL+JXz456bsA/PxM1q1w+Xf78bPnzjKjpUX
                            1R08qfX/7nh3v7+2YaKXJg/w0AIKAL6KQgvlYstojaIGr9staLWiO1seKr3x/1WNRDA5b3Rt1XLh+NEO+FgYAOAICALqBXLoyvHYsdo7aP2rKsrow3eVYZ1O+Iui3qlnJ5TwT3F80IBHQAAAR0AX2kA
                            vlGsdgr6vVRO0etYmb8LbjfFHV91NXl8o4I7S9pDQI6AAACuoDejkA+MRZvKUN5qjXMhEF7MuqyqEujLom6IQL7HG1BQAcAQEAX0AcbypePxd5R7yyXSxn9tkg3o/tj1PlR50ZY/4uWIKADACCgC+jzhv
                            JXxWKPqMOi9o8ab8Q7Kp36fkXUmVG/ibD+iJYgoAMAIKA3OKBHME+nrH8k6tDC6eujlqWiLoz6ZQrsEdZnaQkCOgAAAnpDAnoE8+1icWTUQVFjjW5lpNPgfx51XAT1B7UDKrG/fHMs9otatgar2xt1Wuw
                            /rjdyfx27SUXrC+hJNVjd54vW/UpOd78SMnwtjovFe6N2KupxlubDUSfHa/HPRm90yaMCevYBPXaQ6YZvn43axYhWWvpwdkrU1+LN4R7tgFHbZ349FkfXbLXTJTSHxb7jpIaPXQoCf4iaWLNV/33Ufp4CQ
                            mbhPN1/Z7earXo6o/Ht8Vr8o1EU0AV0Ab0TO8ddU9grWo9Ho15B/fioL8UbxAztgBHdb24Si9tquvrPRK0S+41nGjx+N8di85qu/sExdqd6FZLJa/HwWPykpqt/f9S68XoUigT0SniVFmSxU9w26oL48WL
                            hvJbS5QdHRN0a47iOdsCIqvM+Mx013rLB733L1jicJ2/w8iMjb6zxuq8dtaohRECnHR9OVohK31ZeW7Tuzk69pRv4HacNMKKWrvn6j2vw2I0196AylrEvhfZYQgtqGczTFysfjfpm1Kt1JCuvz2ieplOHt4
                            laP2qDonXzrXTEb8mop4vW6bkPRd0VdXvU1b39fTNNAQAABHTqEnpS2El3AN9ZN7L0QI3nZvr2Od2g8O+ido9aaYi/4vn4HVfF8pyoUyOsP246AAAgoFPF8JPuXvfxqO8UTovL2ZQazs0VY/HpqA9HrbgYv
                            yodWd+lrO/G7z0vlt+IoH6VaQEAQBO4Br0eAWiVWKTHP/xIOM/eZTWalxOj0hdGU4vWY/1WbOOvT9eWvi3qyvgbk6O2MjUAABDQGe0QlO6KeWPROmWY/F1ak3l5YCzuiDqq6PyNYdIR9evib/4wahlTBAAA
                            AZ2RDkBjoj4VP15UDP1aXurp/t7+vkcrPi+XKp8c8Juo1UfwT6cj6p+Muib+/qamCgAAAjojFYLSaeynRX2vqP9jZBi8KRWflz2xuDzq8FFcjU3KkH6A6QIAgIBOp0NQOlp+cdS7dUNAr9C8XCcWVxatx6a
                            NtvQF1lmxTh82ZQAAENDpVAhaLxZXRL1ONxrpsorOy9WK1pdG61Zs33VCrNuhpg0AAAI67Q5Bmxet04fX0Y1G6u3t77uzgvNy+VicH7VmRft2YqzjPqYPAAACOu0KQdsXrSOUr9GNxppSwXk5Jha/iNqswn
                            1L92j4dazruqYQAAACOosbgraLxQVR3bohoFdMumv6/jXo3XJRZ8RraZxpBACAgM5ww3k6rf28MmDQbJdVbG5OisX/rVH/0s3rjjKNAAAQ0BlOAFo7Fn+IWlE3Gu/ZqBsrtk7HRU2oWR+/EK+rtUwnAAAEd
                            IYSzlcsw/kqukG4vLe/b06F5ucbY7FvDfuYvlD4iukEAICAzmDDz/hY/DZqfd2gVLXrzz9f416+rzw9HwAABHQW6cSonbWBASpz/XmE2y1isVeNe5nu6n6kKQUAgIDOosLPEbE4RCcYYHbUNRVan/dn0NOD
                            3dEdAAABnYWF83Rd73d1gnlc39vf91xF5mjaH7w3g56mezzsZWoBACCgM7/gkwLDqVFL6AbzuLRC65IeVbZyJn3d29QCAEBAZ95wPiYWJ0etqhvMR5VuELdrRn3dzdQCAEBAZ15/H/VWbWA+5kZdUaH1yen
                            mhRv2dHWvYIoBAFAnTrnuoAgIG8biGJ1gAW7r7e+bXqH12Tiz/m5SVOgO+QP2C+l+FOkU/DpcTvBS1KNR58ZcvcJLFgBAQK9rOE9nJ/wsaoJusABTKjRf075g3cz6u0HVAnr0edtYXFzU7+ylz8W6bxUh/R
                            YvWwCAznGKe+d8vPC8cxauSjeI6y7y+8JulQqu04413e++yv4MAEBAr6Weru50Q7hv6gSLUKWjuxMz7G8Vt6nOX4Is5SULACCg19H3o5bVBhZiam9/38MVWp8c56vLSwAAENCbrKere9dYHKQTLMKUiq3Pr
                            Ax7/KJpBgCAgN7ccJ76eaxOMAhVu7v4Mxn2+BnTDAAAAb25Do3aShsYhEsrtj59Gfa41zQDAEBAb6Ceru7xsfiyTjAI06LuqlSS7e+bGYtHMuvzvaYaAAB14jno7XNY1Bra0BHpWuJny59nD/h5XhPLOZ1u
                            eFblL58ui0A8t4Lr9eeo1TKaN3d56QAAIKA3THn0/PM6MWQvRN1dBsOpUQ9FpTubTy8rnXY9PcLsM8Mcl65YLBO1/IBaMWrlcrl61JpRa5XBdOwIbfeUio7HdVFvymRuTSvnFAAACOgN89HC0fNFmV0GwMu
                            jboi6MYXzCN9zOvUH43f3xyLVIk/djjC/RBnSU1hfN2qLqM2jNotaqSEB/aKoozKZb5dU9CwFAAAQ0Dslgt2SsThaJ+brzqjzos5Nwby8zrmSYt3SafQPlHXpPGPcE4sto3aI2jlqx6J1NH440un5N1a0De
                            nO8umshvEZzL0LvfwAABDQm+fgonXKNC33R50SdXqE3ltz2KDYjt4y8F1YBvZ0ffvGUbtF7Vkulx7kr7u1/DKgitv5TGzbOfHju2o+ZKm/Z3kpAgAgoDfPEVpQpFOJfxv1kxRiI+i9lPPGltt3W1nHl/cge
                            H3UvlEHFK3T5BfkPyq+eb/MIKCfG2M0zcsSAAABvUEimKUbam3R4BakI5UnR30nAlFj75gd255OC7+orCNjXmwdy/3LsL75gP/0h1EnVHxz0iUJ6fFk69Z4SH5k7wQAgIDePE0+en521GcjnN5tGrwisKdr
                            zFN9KcL62rHcNOquOvQqnX4f6/zdonU2RB1dHdvwR7MQAAABvUEixKQjjPs2cNPTkfKPRQiabBYMKvCma/Lvr9lq/zzqn6PWqWHLv2zWAQBQV6/SgmE7PGpMg7Y3XXf9jagthfO8lafs/2MNV/3sWPfzjSA
                            AAAJ6g/R0dY+NxSEN2uT0HPE3Rfj5QtTzZkAjQnp6NN4ZNVrl9Lx7N2wEAEBAb6A9iuY8Wi09E3yrCGyXGvbG+VjU1Jqs60dijj5kyAAAENCb59CGbGd6JNgeHlnVTDHuT8bioKiZFV/VY2NdPfccAAABvW
                            l6urq7itYjtHL37Qg9HyqvR6a5If2aWLy7aN2DoIpSMD/KSAEAIKA3UzqiuGTm2/jVCGafNdSUIf33sXh/BUN6uk7+vbF+c4wSAAACejO9K/PtS6cLf8kwM09IPyUW+xXVOd395Kj9neEBAICA3lA9Xd0rx
                            GKXjDfx11GfNtIsIKSnI+lviLpvFFcjHS3/XNShsT6zjQoAAAJ6c+0TtUSm23ZV1Acj9Mw1zCwkpF8fi22iThuFPz81atdYh2+Zp6NiOS0AABDQq+SATLfriah3Ol2YQYb0p6LeEz++JereEfiTaV5+M2qT
                            +LuXGQHvFwAAPnA1XE9X94QykOQmHYl8TwSfR4wyQwzqf0ihOeqwDgX1WVHHRa0ff+voqJm6DgCAgE6yV9SEDLfruAg+FxtehhnSX4j6efy4YdRbo04tg/XiuDbqk1FrxO/+p6gHdRoAgCZYQgsGLcej53d
                            FeZwa7Qjq6eZt56fq6epeKpY7Ru0etWXUxlGTosbO53/ti7oj6vaoKVEXxu96XEcBABDQWZjdM9ymwyMMzTK0tDmspzl1cVl/E8G9KxbLlkH96VTuewAAAAL6kESwWDMW62W2WadHOLrE6DKCwb0/Fv06AQ
                            AA8+ca9MHZLbPteS7qM4YVAABAQK+bN2e2Pcf39vc9bFgBAAAE9LrJ6Qj6s1HHGFIAAAABvVZ6urrT46NWyWiTftTb3zfNyAIAAAjodbN9RtuS7ph9rCEFAACoHndxb1ZAP623v+8JQwoAAKOrp6t7xbSIS
                            suVorqjJhStg6jLDfhP50Y9Vf6cLldNn+d7o/qi/lI+KQcBvTFel9G2/NBwAgDAiIXwJWOxSdQWZa0btU7U2lET2/Q3nonFfVH3Rt0cdWvU9RHc7zcCAnqOL6gtM9mca+NFeoNRBQCAjuWHSbHYKer1UTtG
                            bR41tsN/duKALwAOGLAu6Sj75VH/nSqywB1GSECvu62jxmWyLScZTgAAaGsgXzoWe0btUS7Xq9LqRe1fVlrXe2JxTtTpEdavNXoCeh29NpPtmB11muFkGG86yxad/9Z3cb0QbzLPGa2OWyrmQ9co/e0XY4y
                            fMQQAVOTz0fJl6D2wDOVL1WTV05cHn04V23BnLH8RdWK8x/YZVQG9LrbNZDvO9cJjiG886U3nB1Fr1WR9b4rFP8Q8v9zodcy/lDVaY3xVLD4WY3yToYAFvk7GxOLQMjgsX4NVnhU1OeqH8dqeWcN+bxWLTx
                            ata4nHVHx1003Ezoz6dfR6rlfLsMY7HbDYO+r9UW+rUShfkI2ivhX15di2U9LPMTfuMdICetVtkcl2/KehZAhvQPvUcM6ke0VcEOu+ZdXeXGKd0nVhry/rQDNs2HaI+mP0c2NfOMIC/Tjq8Jqt815R+8Zre
                            9d4bc+u0XvlbrE4v6jXpZD7RW1TtI6gMvixXq18XX04apUMNzF90fChqMNiW8+I5RfjtXi3kR89noO+4Bdj6s1GGWzKS1G/N6IMwXdrut7pGrCPVmDfsULUflHHRKXru9JRi/Oijo7a2PRavPZGvUcbYL77
                            ns1rGM5ftlMNX9vHFPW8T9GnYq6s7xUzqNfU1lG/jh+nptCaaTgfKJ0FclDUbbHd3x/Fy9oazxH0BZtUtJ5DWHeXOdrEEN6MJtY8RK4zCj1bORZvLGuXqE2L6p/qWPd9M/BKW2ew/ifr94hIl3A6Qrrg9/X
                            tY/G5onXGQROlL56OjDo4evGJyBFnmRUCelVslsl2/M5Q0qB9QsfXv3x8yhvKMJ6WG5g25ihUQN3PivTF5shZSgvm+/6ezpxNZxG+TTf+aqWoM6MvZ8fyIxHUp2uJDzqjbZNMtmOyoYTFfsMeGMjX1BUAyE
                            q6Wdo7i+o/uWY0pPvnvDY+Dx0UIf1K7RDQBfTF82TUDYYShhTIVy7fpF8O5CvpCgBk7SAtWKg1oqaUp7z/RDsEdAF9+C6NF9FLhhIGHc7Ts0x/EzVRNwAA/iadXfDj+Ky0YSw/ExljjpZ0hru4L9ikHAK6Y
                            YRBh/N0Td6vhHMAgAU6Iurk8rnwCOgj9kE9fUDvzmBTrjaaMGjp2bA92gAAsFAHR50dmWm8VgjoI2VSBtuQTm3/k6GEQfMmAwAwOG+P+pUj6QK6gD54t/X29z1rKAEAgA54V9QPtKG93CQu34B+vWEEyN6J
                            PV3dzzR02x21ARh9n4j3oQd6+/uO0QoBXUBfuFsMI0D21tUCAEbZtyOk3xgh/b+1YvE5xT3fgH6nYQQAAEYgU54RIX1NrRDQO2WNDLbhdsMIAACMgBWK1uPX5EsBvSNWqvn6z4x6wDACAAAjZJeoT2mDgN4
                            Jr6n5+t/d29831zACAAAj6Bs9Xd0baYOA3jYxoZaJxYSab4aj5wAAwEgbH/Vv2iCgt9PKGWzDg4YRAAAYBW/q6er+O20Q0NulJ4NtcAQdAAAYLd+LkD5BG4bOc9AF9NFrdOtF+4moXaOWMfUW6vmom6OO7e
                            3ve1Q7AACosFWj/iHqGK0Q0BdXDqe4P1KDcJ6uT7koagdTbtD2jDokeve6COkuYwAAoMo+G59bT4jPrU9pxeA5xf2VujPYhmk1WMdDhfNhSY8A/KI2AABQg1z1SW0Q0BfXxAy2obcG67idqTZs22oBAAA18
                            I+uRRfQmx7QX+zt75teg/Ucb6p53QIAkLV0f69DtMEH/cXRVfP1n2YIAQCAivhUT1f3GG0Q0Ier7kfQ+wwhAABQERsWrac2IaA3MqA/awgBAIAKOUwLBHQBHQAAYPS9o6eru0sbBPQmBvQZhhAAAKiQdCf3
                            g7RBQB+Oun+z87QhBAAAKuYALRDQm8gp7gAAQNXs3tPVvYI2COhDtXzN13+WIQQAACpmiaj9tGHRTeJ/84w+AABgsJ6Muj3qnqiHoh6N6i9rZvnfpAOj3WWtGrV51GZR6zWsV2+P+rkpI6ADAAAsrrlRt0R
                            dHnVZ1JW9/X33D/eX9XR1rxGLvaP2j9qryP9g4W6xzUtEz140lQT0pnCTOBie57WgFvq0AIBR+Izw31HnRP0uwuVj7frF8bvSEfefporgum4s/znqQ1FjM+3lclHbF60vOJgP16C/Ut2vQZ9jCGFYboh6Qh
                            sq7zwtAGCEXBn1kajXRJDeJ+rf2xnO5xPW7406PH7cMurqjPv6ZlNLQAdY1Jti+nb8fYWzUKoqnVJ4dIzTdVoBQAelJyL9W9TG8Z6zU9SJUTNG+DPJbbHYOerbAnrzOMUd4H/eEC/s6epeP358W9RqRfu/x
                            NyhaF1fVkeXRE0epb+dbrJzYYzPrWYpAB2SLqH6XtRP4v3myQp8JklnxX42PpekG8/9tMjrwOq2rkMX0I0pMNg3xHSa+8868bvjzeiIGgf0ydGbL5shAGQmHTFPR6qPjfe5Zyr4ueTE+PyQbhz37xn1fELU
                            VlHOipsPp7jnZ6IWAADAoLwjQvDXqhjOB4T0E2Lxrcz6vr2pJ6ADAAAMVJenuHwhakpGfd/R1BPQAQAAaqe8Jv3QqFmZbNKWRlVAH6znar7+EwwhAABkF9Lvi8U3M9mcjXq6uscZVQF9MGbXfP2XNoQAAJC
                            lY6Mez2A70o2tNzScAnoTLKsFAACQn/Jmdt/PZHM2M6IC+mDU/Xl87uIOAAD5Snd1fyaD7djEUArog1H3ye4UdwAAyFRvf19/LE7PYFPWM5oCehM4xR0AAPJ2UgbbMMkwCuiD8WzN17/bEAIAQNYuj3qs5t
                            uwjmEU0AdjhoAOAABUVW9/30uxOKfmm7FST1e3R0QL6Iv0VM3Xf3xMdDeKAwCAvF2QwTZMMowCeu4BPVnJMAIAQNYujppb821Y2TAK6IsyI4NtcJo7AABkrLyb++013wwHFuexhBa8Qg5H0FczjACN8O2oO
                            xu67emxov9qCgANd1XUpjVe/9cYQgF9UXI4gr66YQRohPN7+/smN3HDe7q6uwR0gOJPNV9/p7jPwynur5TDEfQ1DSMAAGTvlpqvf48hFNAXZXoG27CGYQQAgOzV/Rp0984S0BfpLwI6AABQdb39fb2xeLrG
                            m+Dx0AL6Ij2SwTZsWIN1nGaqAQDAYru/xuu+rOET0Bfl8Qy2obunq3uFiq/jGaYaAAA0Or84gi6gL1xvf186svtCBpuyUcX7fE0s/j5qllkHAADD/2hd43V3BH0eHrM2f+lbqLrfCX2DqCsqHtJ/0tPVfWb
                            8uH3U+BH+8/9euGskAAD191iN173L8Anog53kdQ/om9ZhJSOk98Xi3JH+uz1d3T8wzQEAyIB7O2XEKe7z92gG27CNYQQAgOw9UeN1H2f4BPTByOFO7lsbRgAAyF5/jdd9acMnoA/GPRlsw6t7urrXNpQAAA
                            ACuoA++rYzlAAAkLV+LRDQc/fnTLZjZ0MJQKaW1wIABPRmmBo1J4PteKOhBCBTY7QA4K+e0wIBPWu9/X2zY/FABpuyZU9XtyMMAACQrxe0QEBvgrszGd/XG0oAAAABvc5yuQ79rYYSAABAQK+z2zPZjr0NJ
                            QAAgIBeZzdksh1r93R1b2w4AQBApquY2YZPQB+sW4o87uSe7Gc4AQAgS8vVeN3dgV5AH5ze/r6Zsbgzk805yIgCAAAVM0sLBPShyOU09616uro3MpwAAICALqDX1Z8y2pb3GE4AAMjOMjVe95mGT0Afiusz
                            2pbDerq6xxpSAADIypI1XvfnDZ+APhTpFPeXMtmW1QuPXAMAgNzU+SZxzxo+AX3Qevv7no7FjRlt0uFGFQAAsjKhxus+w/AJ6EM1OaNt2dsz0QEAICt1PsVdQBfQGx3Qx0T9iyEFAIBsdNV43Z8yfAL6UF0
                            RNTej7Tm4p6t7TcMKAABZ6K7xujuCLqAPTW9/3/RY3JzRJo2L+pKRBQAAAX2UOYIuoA/L5My259Ceru5NDSsAAAjoo2ia4RPQh+PCDMf9O4YVAAAEdAFdQK+bi6Kez2yb0h3dDzS0AABQayvVeN2fMHwC+p
                            D19vc9F4uLM9y04yKkL2eEAQCgfuKz/BKxWKXGm+AIuoA+bL/PcJtWizrG0AIAQC2tHjVWQBfQm+g/M92ujzjVHQAAamlSjdd9dlSvIRTQh6W3v+/RWFyd6eadGCF9klEGAAABfYQ8EhlrriEU0BfHmZlu1
                            6ujzomQPtEQAwCjYJwWwLCsX+N1f9jwCeiL6/SoXL/l2SLqlxHSxxpmAGCELaMFMCxbCegCemP19velSTQl403cP+qnEdLHGG0AAKi8rWu87g8aPgG9HX6V+fZ9KOoHQjoAMIKW1gIYmvi8np5/XudHrN1v
                            FAX0dkinuT+X+TZ+smjdOM7p7gDASOjSAhiy19Z8/e82hAL6Yuvt75sRi7MasKmHRf3GjeMAgBHwai2AIduz5ut/jyEU0NvlhIZs535RV0VIX9eQQ+O5gRPQSWtoATQqoL8Q9ZAhFNDbore/77JY3NyQzd00
                            6sYI6e838tBoK2kB0Ml9THzWWEobYHDi9bJmLDas8SbcHZnqJSMpoLfTvzZoW5eNOil2BOmU99UMPTTS2loAdNimWgCD9o6ar//thlBAb7d0N/e+hm3zgVF3REj/TNQEUwAaZRs3jgQ6bCstgEGr+9mttxh
                            CAb2tevv70p3cf9zATU9H078bdVd8WP9o1JJmAzRCegTSjtoAlTUzg23Y1TDCosXn752K+n+hJaAL6B1xfNSshm57upnLT6Omxk7iC1GrmA6wSE/VfP3fZQihsp7PYBv2jM8TPpvCov1zBttwk2EU0Nuut7/
                            vL2VIbbKVo74W9VC8qf4+6pCo5c0OmK+5NV//Q+P1vZxhhEqakcE2vKao/2OjoKPifTidzbZfzTcjHbCYajTnbwktWGzfjvp41LiG9yFdm7pPWbNj53F5LP8YNTnqht7+vlE70yDWJY3NBlGbR21XtE6hW9PU
                            ZRRMr/n6p3D++ajPGkoQ0DskfaY6v+IBaWnTjVGaeym7/SiDTbk6ssFcIyqgd0RMrsfixZKOon9CN/5mXBmCdy3/OQX2O2OZ6o5yeV9qX9QT0cNnh7mTSmFhmTI0rFi0HgPVU7S+gV+rDOHpztOTzHUE9LY5M
                            l57Z8Xr9jrDCQJ6B+ybjhDGPubKigakPQpnT+Zm7xjXK2LOvVCDdf1y1DYZ9Pwa005A77RvRH2wDIvMP7BvXtb83uzS0fVpUXOK1jX98x5t7xrw81JlnydqKzX0ZAbbMD7qrHjdvj4+zDxsSKEycnqyzAmxj9
                            luNM++m89nlY2L1lmT+5pq2Tkqav8Y4/8TyzOq+mzuWL90H5ijM+n5VabdgrkGvQ3ihfx4LI7ViWFLoXv1onXUe8OoLeeptQbUSsI5NTY9k+1Ir8XJ8WFhHUMKlfkskgL6C5lszqZlSB9TgVC0WdQvi9Ydp4X
                            zfK0fdWrUrTHeH6jaU4pifdKjjk/JpNfp1ParTTkBfSR8J+oJbQAWIn2ZNzuTbVk36rr40HCAYYVK7WNy8b6oE2MfM34UwtCrot6Sbn5bBvO0LmNNr0ZIZ0r8IurBGP+vRK07ysF8bNQX48ezinzud3Vzb3/f
                            NFNNQO+4mGhPF62bJwEsaD+RvjV+MKNNenXU2fHh4XdRWxthGHWPZrY9h0VdGvuXzUcoDK0f9c1yP31e0brxLc2U7meUTnm/J+bElVGfGOlHCpfPOk/3Yvhq1JiMejvZ9Fo416C31y+iDo96nVYAC/BA0Tr6n
                            JO3pYoPExfHMp0Kek5vf990Qw0j7p6oHTLbpu2jboz9y8mxPD72LTe2MQAtVfYr3fgtPbZqU1OI+dihrONjzqQzKi6MuiBqynBvdLyQOZku49w76qNRu2fazwtNKQF9xKSbSsQL62Px47WFU6GA+UtPMNgt02
                            17U1lpX5g+RF9RtE4PTU9ueCzq0dhPPreADyXpaHx6CkN3uUxHKlYu/zk9qeGRqJ/F/3+fKQQLDeg5Sp+p0s14P1g+FSYd3U6Pc70p7VMHc1Ov+P9WKFqPXE33utmqaB1MSWf+TDBtGIKXb3p8ZPlel55OlJ5
                            q8vJTiqaW73W9g5iTae6tX9Zm5WeD9IzznB/d/GLUpaaRgD7SIT19y3t8/HiEbgDzcWsDtjFdPrVtWfN+IEmLpwb8qxS+B3vq3j/F/79X7GcvN41gvu5twDZuVNaR5T/Pif3CX2KZqn+e/zY9BWb5ovWF35Km
                            Bx14r9u0mM+ZFzEn55TvdU+X/yot07+bUM7JrobOycnxHj7D1BHQR0N6BEI65XM9rQDmcbMW/PXDyXCkRyym5w9vpoVg/1IaWwbwVQw/FZuXK5TF//i9Fiyam8R1QHkKZ7qxyVzdAOZxqxYslk17urp7tAHmK
                            51m+4I2ABV1jhYI6KMZ0qfE4hidAObZN6Tr0qbqxGJZRgtgvvuX9BjH23QCqKAbYh/l84+APuq+EHWjNgDzmKIFQIdcpQVABf1aCwT0Udfb35dOMzuo+J8bRAAkl2kBLDZPS5k/d0gGqiZd9nuqNgjoVQnpdx
                            et69EBXnaRFsBiW1YLBHSgHp97IhM9qg0CepVC+lmx+I5OAOU+IT2r+C6dADqwf0kfgm/XCaBCfqoFAnoVfT7qXG0ASr/TAsD+Bcjc41G/1QYBvXJ6+/vmxOLgwjOQgRZvVoCADuTuhPIJEwjolQzpT8Vin6h
                            HdAMa74qoe7QB6IArox7UBmCUzYr6sTYI6FUP6Q/H4i1R03QDGr0vSHc0PUkngA7sX16KxSk6AYyyX8T+6DFtENDr8MZ5a9E6kj5DN6DRUkCfow1AB5ysBcAoSp9vvq0NAnqdQvo1sdhTSIdG7wceisUZOgF0
                            YP9yZyz+qBPAKElHz6dqg4BetzfPq4V0aLzva8GQvaQFMCjHawEwCp6L+qI2COh1Dum7FK5Jh6buA64rPIJxqHypCYPzX1F/0gZghH3PtecCet0/oKc3z52i7tMNaKTPRc3VBqDNny/S2SZf0QlgBD1QuPZcQM
                            /kTfTuWOwQdbVuQONe/zfH4pc6AXTAOVHXaAMwQv4+Ptc8qw0Cei4f0ntjsWvh0SjQRJ+Jmq4NQJs/W6Szcz5ZOEsH6LzTYp9znjYI6Lm9kc6Kel/8+OmoF3UEGvPaT1/QHaUTQAf2L+nsvBN1Auig9GSaj2uD
                            gJ7zm2m6s/Oboh7RDebhKGu+fl60TkcFaLd0ls6D2gB0QLrfxXsjvzypFQJ67iH9slhsGfVb3WCAn2lBtq/5dArqYVEP6wbQ5v1LevrBBwqPKQTa7/Oxj5miDQJ6U95Q+6IOKD+0P6UjjfZE1LtjPrhHQd6v+X
                            SGxIFRM3UDaPP+ZXIsjtYJoI1OiX2Lu7YL6I18U02nvm4UdbZuNE66F8EPojaMeXCmdjTi9X5tLN6vE0AHpA/S3kvI3b1RP9aGjrsy6sPaIKA3+UP741HviB9TPaYjjXBB1BYx7kdGOYOiWa/3swo3WwHav29J
                            l9IcEnWJboyom8tiZNwdcz29hx4a9Zx2dMT1UW9NN7jWCgHdm2t/XzqKvkHU16O8KPKUnlm7e4z1XlF3aEdjX+vp2/9/0gmgzfuW52OxX+H56CMhXft/RNS2UZO1Y8TcW871k2KxQ9RtWtJWt5bh3MEjAZ0Bb6
                            7PRH0xfly/8Nz0nKRH4bw9vZnE+F6kHcQ8OC4WH4qaoxtAG/ct6YP1noUj6Z2S9tnppq4bRK9/GJUuV7tHW0bMfQPm+i2x2C7qGO+lbXF51BvKx8MioDOfN9iHy+emb1N4PFOdXVy0volMwfx35SmI8PLr/D9i
                            sW/hRpFA+0P6W6PO0I22Smc6bh79/XDUEwP+/d1aM2LunWeuz4o6Kn7cPuoG7Rm29GSpPaOX/VohoLPoN9kbo/aPH7eKOj1KwKu+2VG/ito6xm63qPO1hIW8xs8rWkcAbtENoI37lvTEiL+L+nLhEWyL68Ko16
                            b7BS3g8rQ/a9GIuX0B8z1dN/26qI+lf9SmQUu54ktRB0YPXdMvoDPEN9qbotIb7SZF6+6Vz+pK5TwYlS5PWDPG6pCoP1Vo3ep+6tezmb++0+mR6dv/Hxa+hAPat2+ZG/WV+PHNhZvQDse5UTtHD/eIum4h/93U
                            wg3LRkK6P9N9C5nvc6J+WrQuE/2Wz8qLlM4CSWd5ftUZngI6i/dme2d598pVi9bNSVz3NLpeKFqnBe0TtXaMzdfTXfkrOG+eLur9/O0ZDXhtz4xKr+ndotxAEGjn/iVdbrVp1M91Y5HSWXAnR20Vfdsn6opB9D
                            edoXC71nXc7SmED2I8nor6XPy4btH64tuNl18pXf6yafTpD1ohoNO+N9sZ6eYkReuu77tG/UcTQkyFpDfs9EXJKjEOB0SdW75BV9nkGvf75ga9ttM4bRn1maJ516a38zVU96NZsxu8f637h+lKHrWLfcuTUYcV
                            rS8B/1Qwr3Q08WtF6yy4D6QzF4f4/1ehp89nPp+vHeKcf6L84nvNqK9G9Znmf71fQvri6aAo/RDQ6dAbbjp97ZKodDfolYvW9Wa/K3xb2G5zy1CebkSybvQ7nfL246jpNdqGrxf1vA4xHfn/bcNe17Ojvhc/Ti
                            o/MDbhy7dp6YvHNv6+KUV9LxdIZ7zcVDRX+gBZ59OxL634/iUdTU+PBvtAMc8Ntxr63p7uA/KOqDWiN/9nMc6Cu6QC23J1B37v5AqN138Nc873RqXrrNcoWteoN/Fmcn3lZ9jN0kElH+tHx5i5c11K8L8aMmZM
                            o7a3p6t7mVjsVbSeh5ruEv1qs2BYwTC9Mf2/FBCreOr6MOZF+hCS7mHQU5NVTt/cfzB6f2aTJ2KM23Kx+HDUJ6LWznQzj45x/mab+5aOmHyxZn1IX6IdVj7jt8lzPr1v/SZqXM1WPT115cAanFH1cp+XiMU7oz
                            4V9doGTbF0VtavU8VYPdSmXi4Vi8uK1pcfo+GrZQht9xwZV36Jsfsoj9lJsX2HtnG70jilg1sHRy2f8VxPX3amx7r+KD3KeaT/uDwqoAvoC94JjS1ad4neo9zB7hi1pFnxyv1I0TpF7YKyLo+d2fMZzocJResZ
                            uenNabmKrmbqe7or7jkxBtNMzb+NXTo7arfyQ0UKMMtk8JpLpyz+IuonnbhJTfQs3RwrfVG5bA36ke48fFp5N2Lzvat741gcUrTuuVJ1aZ81OeqMwVwjW9F+pztgpy8C351pYEmh/JxyjG7tUA8nll92vHme99
                            cUjF4cxq9MX1Iv6nKXJ6POim36rw7OjfRFTnr0705R40d43NLlShdF/aZD7xFLlp+J0rx/e4U/Fw1VOpPn36LOTmfljdqbvDwqoAvog94ZLR2LHcpKO9t09+gVG9iKdIQ83ZX1yhTG0zKdBmWGUJPXcfqiZe8y
                            qL8laqWarPoDRetU0PTYovN8AQOV27ekwJJufJoe8fq2or5n4KX3+HREOx39TWfB3W90GcTcf2PROgM1hfbNa7YJ6UuoU4vWF71Tq7BC8qiALqAv3k5pvaL1rPV0c6otyuVaGW1i+vY6fWN+S7kDuybqhtiBvW
                            j0yeD1m3Zw6Q7NO5WVzpLZoCKvu3RWytXla+7Kdp1OCozIviWdgZdOfU9HhHcpWl/sT6zo6qYjrensk3Tk8MJyf/O8UWQx5v8qReustfSe+rryc3KVLrtJNzZMX0Kdnyrm+8NV66E8KqAL6O3fMaVTQtcra4Oy
                            JkWtXtb4iq1yCtvpw//UovWczPRt+W1F62ZLUz3jkYa9fleIxWbl63bjAa/hVTvwATvdLPHustKjH28u6z6vO8hqv5Ius9mkaF0itUW5j0mPskpf6C8xgquS9jm3l5XOhEtfAt5W18sLqM38T0fYty5rw7I2Ku
                            d/J4PG3PLzbfpMe0v5ufaqmO/3Vb1n8qiALqCP/I5qpTKovyaqu2jdRX7F8ufl5qkU9scOWA4mIKRHTKVvv2eWP6fTz/sG1F/K5aNlKH/YEXEY1Gt36TKop9dwT/l6XLZcvnxde3rdvvxEkHTDq3SH9ReK1jWR
                            6bWXvrlPN595ND1zVleh0fuU9L6+WtH6En+d8ud0avwK89TL7/1pPzNuwM+zy/3Ly9dqzygrvb8/Xu5rUqW7zt/u8VBUbP4vVc79lcrPwi9Xen9duqzx5XLcgDn/8iPsnivnfnqCx/Ty8+4T5dxPB5vSQaYX6t
                            gbeVRABwAAAAEdAAAAENABAABAQAcAAAAEdAAAABDQAQAAAAEdAAAABHQAAABAQAcAAAABHQAAABDQAQAAQEAHAAAABHQAAAAQ0AEAAAABHQAAAAR0AAAAQEAHAAAAAR0AAAAQ0AEAAEBABwAAAAR0AAAAENAB
                            AAAAAR0AAAAEdAAAAEBABwAAAAEdAAAAENABAABAQAcAAAAEdAAAABDQAQAAAAEdAAAABHQAAABAQAcAAAABHQAAABDQAQAAQEAHAAAABHQAAAAQ0AEAAAABHQAAAAR0AAAAQEAHAAAAAR0AAAAQ0AEAAEBABw
                            AAAAR0AAAAENABAAAAAR0AAAAEdAAAAEBABwAAAAEdAAAAENABAABAQAcAAAAEdAAAABDQAQAAAAEdAAAABHQAAABAQAcAAAABXUAHAAAAAR0AAAAQ0AEAAEBABwAAAAR0AAAAENABAAAAAR0AAAAEdAAAAEBA
                            BwAAAAEdAAAAENABAABAQAcAAAAEdAAAABDQAQAAAAEdAAAABHQAAABAQAcAAAABHQAAABDQAQAAQEAHAAAABHQAAAAQ0AEAAAABHQAAAAR0AAAAQEAHAAAAAR0AAAAQ0AEAAEBABwAAAAR0AAAAENABAAAAAR
                            0AAAAEdAAAAEBABwAAAAEdAAAAENABAAAgD/9fgAEAKcxisFjVfn0AAAAASUVORK5CYII="""
            html = f"<a href='https://github.com/Tobias-GH-Schulz/mask-detector'><img src='data:image/png;base64,{github_base64}' style='max-height: 150px; max-width: 150px;'></a>"
            st.markdown(html, unsafe_allow_html=True)
            st.write("""INQUIRIES: mask_guard@gmail.com""")

    def timeline(self):
        st.markdown("<h1 style='text-align: left; color: black;'>Road map</h1>", unsafe_allow_html=True)
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
        timeline = Image.open("images/timeline.png")
        st.image(timeline)

    def end(self):
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.markdown("<h1 style='text-align: center; color: black;'>Let's make the world a safer and healthier place.</h1>", unsafe_allow_html=True)
        


        col1, col2, col3 = st.beta_columns([1,3,1])
        col1.header(" ")
        col2.header(" ")
        image1 = Image.open("images/logo_large.png")
        col2.image(image1, use_column_width = True)
        col3.header(" ")
