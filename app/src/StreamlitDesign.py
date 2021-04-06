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
        col2.image(image1, use_column_width=True)
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
                Mask_NoMask = Image.open("images/Features/Mask_NoMask_Detector.png")
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
            
            linkedin_base64 = """iVBORw0KGgoAAAANSUhEUgAAAUAAAAFACAYAAADNkKWqAAAgAElEQVR4nO29WY8sSZqe93zmHkvuefZTp2vpqV6mZ8hpkiIkSI
                            IAAQIESHe8EW+pn8H+BdQNfwhbN7qTAEEACQiSeCGSGpI9Mz3dXd1V1bWcOkueXCJjcfdPF27mbu7hkRl5MhbLLHtx8kTE4x4RZuZ
                            ur31mX4QHREVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVF
                            RUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFR
                            UVFRUVFRUVFRUVFRUVFRUVFRd1bybYLsJR+8UsAg2p5K2LslpKpQpGDFoB9XEmZr+aq2abe5z4yd9+/JbI7wwAovNvC7lfwz/8JoS
                            vddgGWlAF2QfYRdsv77KIMgb7dXkpbtyL1fdbFWu8Z2fJM2ubYNbhEFhwrvbAAnYKMUR2BjBBGKOfAiNoYg1X4EeAvfgmqu4i8AP0Y
                            5AXKhwhPQB+iHKM6RHMoChslqhdk2J6mtqprYZ5CCKruEgOQ1kaNLHDmjG0MnABvgO+AL1H9CpHP7e0o9CgwXAP8xb8wIENgH9XHIJ
                            8i/BT4BPgYeA76FOUYtF+aX2HQgmoKrNV/daSxDuZHNRLZjVjbGVXtw8gCZnaqyxSRE1RfIvINyueI/gHk1yi/A32FcA4y5p//kyCjw
                            TAN8Be/BHQX5Dnon6P8GPgRIh8DT4GHwDGqhwhDFErjs+ZX2LVA2FBntg/81oxsOeaiC7Ws2h5Z+AyAMcopwgnoG5CXwOfAb0F/A/I
                            r4BsgyGgwPAP8xb8wwBDkMfAzlP8W4eeofozIMeX6X1r9KaY8OO6vKA3QTYV9uYeyJua/XWTLMdehRKgid3c/srAZCioFaAZkiGSoj
                            hA5oTTBvwT+d+CvUV4hOuaf/49BRYIBJkFkCDxH9acIfx/k58DPEHlMmfQwjchLpB6ZADD2vk1Goevv0HZAbNyPbDkG1IkQ7zhGFj4
                            r7xtU+gh9u98+cIiya/d7Tdlnfw1SRoIBKdl2ARoqEx4PEP4T4L9B5L9A+FPgMTBEbLTnjoA7KI75B0u813UdDvWe457H7Zn/Xu49I
                            lueqXdcwJpjZHeUCUiCaJ9ytnYEsg9cAi/5L//RBf/3/0Iokut32YB+8UtQUoQh8DHofwfy34P+FOQxqkMQU5kO2OhBmGf2jlsL1NZ
                            02I/e7EvcmrlWbEc5kV3PfEV2f1g5BRuDvEL114j8r8D/hvI5MEbIQlgTNNfvshHZdT+eo3yK8ifAh5TrgLuI2Gmv1H9VNNFm3p8x9
                            V8VNdK8XQVTbZ4EkS3P1P6nre2R3W0GBmUXeIzIhyh/gvIpos8Ru5QVgIIoRBlKs0/58ZafIvIxqseUpohr0fr2OoZnhKa+7ztXdeB
                            YDesoQmRLMvWOiztGkd0PpjoEjhE+ppzRfYzqPoEoDAN03/RQ/RDhE5SnILsopnYbvNtlmDNAZ4KmNkHnhf7oxS1Y9ZlAjeymzD+Ev
                            iK7J0zst7h4CvIJyoeI7BKI94SRBS6/27uPyIfApwiPUfplY7ZbVG/GHDbWSwsvO9zulED5kRpuzlxZ/deLbDlW3VJvj+z+MOij+hjh
                            U5BvUfaRMAwwiELYyGoIPAGeUn7A2ZZNaawv3JgBVTTYigShPljVn9ycUb9dZDdkeLdQHZbI7hErPwZzCPIU1Segw2o2tWWFYYBlmD
                            xEeUi5aLoPmpaN5MyL8r77uxHz/taRGAkloXAXmRuwtLU9snvESFH2gccID0GG1Fd02qqCKEQVJsMhuOSHmHo00dbt+zA8I1xDYqTj
                            7SJbkoWyYB/Zepj7lIfqMcghov0YAc7LIAxBystbKfWIMhd6vS9zBuhMcEWJkVASCneR+YfLV2T3h5UbDOW3RVrBzXYVkgFSuorWa3
                            8C8y2qt2ft6XBjTZC6o1YdVK9m7nn+gn5kSzK8W+rtkd1HZuoNYSgMA6zaRAxqo7/KaazRqL/jbZl9/VUlRvx6RHYzhncL3gAT2b1j
                            4jobwfhgGAZYeZ12PHZG5TbIipj3d9vESCgJhbvI3OCkre2R3T/m7rtzIQCFYYDA/BQTbzTR1u2qGJ4R3jIx0vHSkS3JQlqwj2x9TD
                            wWiMIxQLcm5NQYMdqh1yqZM0Bngu+RGAkloXAXmX9ofEV2T1nXSLg9hWOAlTyj6hwxdD3sNokRt8/WEwp3keHdUm+P7B6ysMwPQjHA
                            qrHEe+wZ4cqTIF3Mvuf7JEb8ekR2M4Z3C94AE9m9Y35/CsQLwzDAyutcVOU9rkzJ7ShrZN7fTRIjoSQU7iJzA5G2tkd2/5i7786FAB
                            SGAQLbSYJ0MTwjvEFipONlIluSbXtxPrLNMPFYIArHALeWBOlizgCdCV6TGAkloXAXmX8YfEV2T1nXSLg9hWOAlTxT6hwxdHNs2cSI
                            e7z1hMJdZHi3tNo2svvFwjI/CMUAq8YS77FnhBtJgnQxW47rEiN+PSK7GcO7hfqwR3b/WEyCLFDldVqPFu5xZUBuR9kw8/4WJUZCSS
                            jcReYGHW1tj+z+MXffnQsBKAwDBMJJgnQxPCPsSoxI51MiW5Jte3E+ss0w8VggCscAg0qCdDFngM4EW4kRYOsJhbvI/Cb3Fdk9ZV0j
                            4fYUjgFW8gyoc8TQ7bJFiRGhNvGgkgyhM7xb6u2R3UMWlvlBKAZYNZZ4jz0j3FoSpIvZssXEyGoY3i3Uhz2y+8diEmSBKq/TerRwjy
                            uzcTtKAMz7qxIjvgm6unh1i6ybuQFGW9sju3/M3XfnQgAKwwCBsJMgXQzPCDsiQf8I+0+PbJ5te3E+ss0w8VggCscAg0+CdDFngB0m
                            WD1F69EwlMRDSMxvXl+R3VPWNRJuT+EYYCXPbDpHDA2PxcTILRjeLfX2yO4hC8v8IBQDrBpLvMeeEQaVBOlgruwxMXJzhncL9WGP7P
                            6xmARZoMrrtB4t3OMqwnI7SnhMobo+YEyM3Iy5wURb2yO7f8zdd+dCAArDAIG7lwTxmH8wY2Lk5mzbi/ORbYaJxwJROAZ4J5MgbWZ5
                            TIwsz/ym9BXZPWVdI+H2FI4BVvKMpXPEaBtOIKwqq2UxMbIkw7ul3h7ZPWRhmR+EYoBVY4n32DPCkBIenUmQ9oHVuj4xMXI1w7uF+r
                            BHdv9YTIIsUOV1Wo8W7nEVTbkdJTzW8ECfuf0lJkYWMTeYaGt7ZPePufvuXAhAYRggcG+SIF0sJkauZttenI9sM0w8FojCMcB7kQTR
                            Dmb3jYmRbuY3pa/I7inrGgm3p3AMsJJnJp0jRttcAmFVWa9gMTHSwfBuqbdHdg9ZWOYHoRmg2JbzowOoWblTgAxvYLuKeSZYRYL+5f
                            XFe55+f5jrMXY8iOy+sgYMQuEYoPq37YZyj7VlKoGwyrC7mP88atMzBpKk+xfn3P7qtcu9ZlozIru/TJsoAIVjgNK69SMFfycJkFUf
                            8bDMHWiX1VYFLcrbomjydn1V61upNlSee++Yeu0nWhtjZPeQuYPvnfdbVrrtAjTkOn3VTs5kxGswrweFxMoK2Pu+yRWeqVHf+ieAFv
                            U297r+utlc8uA+Ma8dOntFZPeHLbNtswrLAIGGmXSuGbTdIxDmvJDCRnk55DnkM6QorMk5M/RUJQbcr80Z1E2RxXgjp3urlpHcB9Y2
                            QyGye8nCifycwjLAKglCq6Ec8w0xIFZNea3J5TkUWWl+eQZFXppikVNFg2WFQaRpeNUaYWL/TL2vayM/oVBFyHeYudGjehzZ/WdhKB
                            wDdKanMD9M+OYjVBFEMIzS3PIMigzJZ/a+M74C1cJb/3NTXvt60v5zBphCkkJqzbA9sro7d55pzap9Irt/zDPB6vzfrsIxQPFuXZAk
                            jVYs74fEXDRYlFNdshmSzSCf1uZn9zQCkpjyltR6nVhPlWbdKb21EEVNQWESCimZgo0ipd5f7jBzXxd0x7v61kBk9495J3gg0WA4Bg
                            jcqSRIleSwkV82Q7KpnfbO0KJA7dTYGMMgTdnppRwM+xwMe+z0UgZpSpoaUiMYe0IUqmRFwTRTxpkyygtOZ8pFroxyZZqrc8H6JNp6
                            IuM2zD8BujpFZPeHLbNtswrLAIG6cVxnaTdWOxLbItMCZlMkn0I28xIeda82IgzShEd7Q54d7vHDx4d88uiQZ4d7PNwbsjfosdvrkS
                            blWt80z7mcZpyOp7w+v+Sb0xG/fX3KH0/HfH0x401RkCm1cYj9b9uJjNuwrS/OR7YZpiF5HxCaAboQec5rHPMNcZvMHswiL9f7ZjMo
                            ZkiRo6qIKokReknCbr/Hw70dPn54wMcPD/nJswf86OkxHxzt8fhgl8Nhn91+j541wEmeM5pkvBuNeXk24o9vzzgc9Hiwc87uyZjBxY
                            x344zLLCcr1EaZUpuLQjDJjWWZi66DWJyPbDMsDIVjgM70FOaHiZb5yBaZ2sdFUWV6nfmhRTUzHiQJzw53+fjRIT98fMSfPX/EJ48O
                            +eBoj6eHuxzvDjkY9hn2UnqJqabLe/Q4GCiHwz5HuwMe7w95erDLj04v+OT1BX/7+pw/nIz47O2It5ezMhr028+1lz8CB8+0ZtU+kd
                            0/5pmgO/5bVjgGKN6t0owU/J1CYEVuoz/7Wb8iR4sCESER6PUSHu3v8OOnD/h7Hz3lz1884ucfPuGDoz12+j36qSE15Z8xUkaNIlU0
                            lyawO0gZ9BKOd4e8eHDAj0cTPnl0xotvTvgP374jUyh0xOkkI6vWGz2TFggu4dHFYhLke8TcwXf3t69wDBC4G0kQBVWkyCDPEC3Npz
                            Qx2O33eX60xyePDvn5R0/4+x8/4afPHvLpk2OOdgbl9VChMjx36983IogxpAYGvZR97XEw6NNPE1IjpGnCZab0koTPTy54PZoyneVl
                            2baSyLgN80+Ark4R2f1hy2zbrMIyQKBuHNdZ2o3Vjs42zOzaXzn1zai/46skScLjgx3+4SfP+PmHT/i7Hz7mx08f8ORgl4NBr/wIjD
                            UAN+V1xncd66dlVJkaw95wwG6/x7ODIf/6C8NffnPCNMvrYgt1WW+SjNgW2/rifGSbYRqS9wGhGaALkef8xzHfELfI3Lc6XNJDBJMI
                            O/2Up4e7/NmLR/y9j5/yk6cPeH60x24/rT7m4vZ3BrcsU1WGvZR039BLDEYEY4TvRhO+eHfJ5TRnmhcU5c5lmf31llASHl3MRddBLM
                            5HthkWhsIxQGd6CvPDhG9IQhVBbIUBWtQfdFYlEWHY7/PkYIePHh7yk6cP+PGTY54d7rI76GFgbsrLDRmUH6npJYbDnT4fAtO84Pdv
                            L/jdmwsmWcab0ZRxVpRN6I/A7k6wTGtW7RPZ/WOeCbrjv2XFy2EtzVy5FLFfa1MbASaJ4WhnwIvjAz55dMhHDw94erjLbr/XaGDf3N
                            6XAaQm4XBnwPPDXX748IBPH+7z4nCX3X7qrTMrVfs5VplNQEyhmjIFdemmyL4Pl8MKxwChHCHAM5uqN3sNti3WKCjV2p8W9IzheG/I
                            hw/2+fB4n4d7O+z2eyQ24+GbV1lNfW8GYIzQTwwHwz4vDnf59NEBHx7tsdfvVVNt+8Z1m5YvGB5rqKuxI7s/bJltm1VYBgh47mfvth
                            tLt8Ram635iUI/NTw72OXHTx7wyaNDDoalEbk1vHZyY1VsmCZ8cLTLnz495kdPDjkc9ksDdD7TTjxUC9EhMbxb6u2R3UPWHMhDUFgG
                            6ELkuWyReo0nW2KLlSaGB7tDXjzY5/nhHsNeavu32mrNm+EqWGKE450+Hx7v8YFdbxTxLp/VWG9xEW2AzPUYwTvukd0/1oBBKBwDVP
                            +23VDusdb7bZr5ErzOC6kxHO0OeG6/3rbTSxFq02pHcatiqTEcDHo8PxjyZH/ITr+HSexls+aKLVRrMsExrRmR3V+mTRSAwjFAad36
                            kYK/07aSIHPlrU06MYa9Qfmd3we7Q/ppUkWAt0l4XMeMlNPgo2Gfo50+g35aGmB1cVWpi6+uuBoWU9uWCmEt2EcWkyCb1p1Jgoj3Vy
                            YldnppeWGDQVolP8oqvX/C4zomItYEDcM0YZAm9NIEcVGgqcton0xMgkS2PbbMts0qLAMEPPezd9uNpVtirnhSm4vtwIbymxo7/ZR+
                            klSZ2HUnQXyWGmGYJAx7CSZJkCSljgKFatoekyCRbY15A2AgCueD0ECdBKHlP475Ec2mWauc1e93FGAjMWPqhAU0DaqqyRpYWaTymy
                            HGGTTY8kH5K3W2Pn4yIn4TJLKtsTAUTgSo/q1vQv5jrffbGgM1CWrS6nc6VJW8ULK8oKguibXahMdVzA24hSpFoV7xpf7hdWPKujQG
                            Yft460w7yhbZ/WPaRAEoHAOU1q1W/zV32to3QdS7b3+0KElADKowzcorOU8z+wNI1AZVvYqsNgnizLdQyAtllhfMCmuCbiCpolWp/+
                            wmd15W7bwNpmU9qsjQGWNk95C5g691P9+ywjFAqEeIygRdg3mMLTMRkASSXvmrbWIoKL+XezmbMcky8jUkPDqZPcdmRcEsK5jlSpar
                            146e6YmfGfbOvpgEiWxjbJltm1VYBgh47mfvthtLt8+MsT9X2QOTUCBczjLeXU45G8+Y5YUd8NacBKGcel9MMy5mGeMsJysKykvCeG
                            V2Juimws4EhdqY/Mhwowzvlnp7ZPeQeQNgIArLAF2I7BqskhfV+Aa5DeY6r/3dXk1ScjGczwrejCacXE6YZHm1DlhWaz3fBMlVuZzl
                            nIxnnFzOGGcFeWGnGI162PuLIkFnTEr93E2yKrr2ixzZ/WMNGITCMUD1b9sN5R5rvd+2mUi5BpgOmEmPt+OMP55c8O27C8azDGX9SZ
                            A8V07GM746veTb8zGXs4zCj7T8NvWnw8ElRrSjHJHdP6ZNFIDCMUBp3fqRgr/T1pMgnkwCvT5T0+PVZc4f3l7w5ck5Z+OZTUR4ZgQr
                            TYKoKpO84LuLMZ+9veCL00vOp1nLZ7xIS6nvh5QYceastrzOGCO7h8wdfK37+ZYVjgFCPUJUJugazGMExKRcC5xheD3J+cO7S754d8
                            m78YxplttExZqSIMAky/n2fMLv3lzwh5MR5xMXAXaUGY+FlBhpl21Okd0ftsy2zSqsD0IDnvvNd0zHQ2BuNBPDVOHlZYY5GfPg4JKv
                            z8f84GhGL03oeUNMO4J7H+amwFmhvBvP+P3bC/79t+/42+/OeDeeUVQjbavM4v6zzO1iTImKoh653XRFWs9dF6tuqbdHdg9ZOJGfU1
                            gG6Exlzn8c8w0xAGYPdK7K+azg5WXGF6dTPns74sneEDHCg50Bg3R13w5xkd+byxlfvLvks7cjPj8Z8e3FhEt3Ofyus6xqU3+bM8It
                            f2PEGbO0yhbZPWZhKBwDdB1UYb4D++bjOm1ATEERRpny1fmE//erExQhU+FnTxP6Sd8OgO//myCO5UXBm8sZf/nNCf/uqxP+6uUpr8
                            4nXE7t9Ld8Qqt82sFonpAuElStfuukPgytEX3lTGtW7RPZ/WOtgTUAhWOA4t0qzUjB3ylYJuQFfDea8W+/fsfY/m7vwaBHIsJuv/xN
                            X9N+lSsMzzWG+4pbTsHpOOP3by/411+84d/88S1/++qM06md+pZP9iJUL9JayPCM0ACF91g9s6Q8gZHVsvjD6N8j5g6+u799hWOAUE
                            cdlQn6Hdbt5PWgwFgBjKY5X51eYkQ43umx00s4ncz44GDI0bDH/iBlmCQYM5/Vnc/+lmt9o1nO+TTjnf3Iy69envLvv3nHb16f8/Ji
                            wiQrmB9StVm+hYxWnTqmw9WxkdYovgrml7mrU0R2f9gy2zarsAwQaHTWxtobNQ+NeTgrCs4mypenlxSfv+bl+YSfPNrnL54f8aOH+3
                            x0vMvj3QGD1GAEL9IDP+GhlN/vPZ9mfH025ot3I3796py/fnnKb99c8JvXZ7waTRhNc/vhZ2pzEfefV+ZlmKvHphMjW1+cj2wzTEPy
                            PiA0A6zWqWg1lGO+IYbEqMqsCrNCObVfiTufZpyMZ8ysmZ1OZjzfH7I/SOknhsRewspFfUWh5KrkRcHlrOBkPOOLdyN+//aCX317yl
                            99d8pXZ2PeXk4ZZzlFYYsh82XpKt+1rDLCDSZGnAkHsTgf2WZYGArHAF1nVJgfJnzzcR00IOYnGShHvywvOLcfV5nl5ZVaPj+54Mne
                            kOOdHvv9lL1+yk6asNMz9Ex5UYXxLOcyy7m0097zScabyynfXUz44+klX5+NOZ3M7FVntG47OspyZRKki9E8STeWGKnbrd5nW4xbPD
                            eyq1lrEA1A4RigeLdKM1LwdwqRtZMMKoCgWn5k5dXFhPNpxt++NvTsb/ru9BKOhj0O+j0OhynDNKFQ5XSScTaZcTrJOJ9mTLK8MtBJ
                            XjDNcjJ11/wTr+0WlOW9GJ4RrjkxstEkiD9guOp0Ma7Zb5Nlvk/MHXx3f/sKxwChjjAqE/Q7p9vJ60EhMTzmeUWhyqQomMzyEtgTIU
                            kM+4OUvV5aJkZSQ6FwNskYTTPOphnTWU5R2Eu7iPe67kSq1lq0oyy3YX49LDNYwyqaZuCb5vsy/z3ntCJWldmNrnht19qnMTWnbge/
                            PXy+rjLfO7bMts0qLAMEGj3kriRB6NhUMamNvZpGQ16U64PjrOB0MiM1BlVlViizoiDL3RS3bbhd7ytrYNTvLcZeYssZeCvr3PKLW7
                            EuX66K6Zv+Vaz1XDelsNN4UaVa23SGWBm72MGm/lW9MujzLiUm7Q8z3bR831emIXkfEJoB3qUkSHXfiyiWkbdrnikFOVP3FjSDq0ak
                            4nfoxnekpXnr788NWVeUhMdUQfP6/k3qfWP5Juy7ozbr6hu3umOjtWG7Y6QKRY4U1uwsV1ePwots3RW//YFHpP65UXc7FxW6Tt4uX2
                            TzLAyFY4CNTt5uKN982ifdhpnrYFViIC9vb1Hthqf6b7tIzpBF7HUJE6/93Inml3lJBlDkUGRQFIg/3XWldUbhpsONmrQN4KbM3oir
                            W1pecqwdFs4NkJ6KvCxXUSBFUd5v/Lmyg/rmWJm6bd9q0PNM0Y8MjQFJvEuLeb/H3ChfV5m/r8w75uscO2+gcAywNciXbdY+0yUMpp
                            RGUGSQzZDCru95Wt/xtWVwHTCl7HTGldOdfF6Zl2WqdZ3yrDaTtgn6Bugbx0qqZ03GJNCz9fS3ufPCj4Ld2xcF5DlSZJA7I88X1MNr
                            Mteq4t6mJD5TLaqxAowdNAyFpmiRoImCJmCUuSlyo8xd9fi+MH9AWTSCbVbhGCBwN5IglLcuyshnkGfYeMLbZV0W6HqsvSy/SGmEJP
                            WbV8X36uHKzSJWl1tsFCh5htqITxthqtpI0JmKv+221bP1SdRGVVr+NYrfLG95LHJ7PLLS+KwRqpamqNqM0ssmNPSThH5q6CUJiZHq
                            c5mJGFIjJNaAZ3nBLM+rrxwWwEyFaaFMNS8/loTUP5blR4jVO85V9nvGltm2WYVlgECjYwaZBKkjICny0vzyWW14lQet2ADdy7mwxJ
                            gSJT0Wu49XjyqcuYq5OliDs5GTFmqf4RldZfAK7jL8qzB9EZtxNtZbu17TlbM0N/IZks1K066mwHWZqh8K1brKiSl/RP5od8DR7oC9
                            fo+dfsogTegnCYM0YdBL2O33UIXzyZSz8ZRZXhppVhScT8qvJ56Op5xcTpjmBSpJ+VsxSQppvx6s1L6xUE8F/WP6vWDuAISjsAzwTi
                            RBSi6VEZZrZQYlMYY0KaOK1Egd5q/SC10xjIGkh/YHaG+IJgmqZcecZkXZGas1Lbw29aOnLqaNuwYY9BIGvZReYkiNqX9vHUqjsetr
                            7gKwt6tfuaamSQ96A7Q3oJDyM5KzvGCS5UxmOUWRV9NcmU0hnyJFXkas3jlkROilZdl7iaGfGPppwk6vx96gx4PdIQ/2h+wPysfDtD
                            a/nV6P3X6KAmfjKe9GpclB+UH3s/GUt6MJb0djXp+XV+SeFEpGQiYJU4EZSq4FRVfkHUQyYlssDIVjgI0gpN1QviFJq9NumrW5liaR
                            JOwNehzvDXh2sMf+sE9iP9qiKILYW7+678PK2FKMKX+cvTdA0z65GGa5cj6Z8e35mG/Pyx9napq4V49FSZBGYkIZpAnPDnZ5cbzPw/
                            0hRzsDhr0UI4KfRNCioCgKtLBG2Ags7Z2FzO8cUpmgpH2KpMdMhdEs4+3lhC9PLvjq5ILLybSMvPMM8qya7lYmbF+z10t5tD/k4d4O
                            j/d3eLw/5Hh3yIPdIQfDPgfDPrv9HsNeQj9NSqN0A1laMhQus4zLyaz63nVeKOMs42Iy43w85WQ04XQy5eRyysl4xpvLGS8vppxMcs
                            5mBePC1i1J6gG1MdDr94B5x3mVQcEtFI4Beue/7XsEkfDoZOr9D8YIw17Cg70hHz885M9fPObZ4R691NTX6Lut/JcRqNfKUgqTkimM
                            Zjnfno8xL4WT8cx++BrKqy645zjj6WBend3SXj9NeH60x9/9wWP+5MkRP3hwwOGwT2oMhZtiKqgqRZ6T2/U2nav3Mu1g399mYcUk5B
                            gmufLmcsoXJ+eQZbw5OeVyNoFsitgsvBsgRARjBEEY2GPyw0dHfPTwgB8+PuLjhwc8P9qzg1SPvr0yj2CfJ2CsMRsp1wOh/EB7Xng/
                            UkVZ5/KrjjmX03Iq/PJsxB9PLvjj23N++90pX59d8s0o4+1UGRdClS5z53cwCYpNMNe53f3tKxwDBO5OEqR58MppVsLhzoBnR3v86f
                            OHfPzokIH9ettaVH1UJKHAVBdg2O+nfHs+oZeYug6V/DBbWszby523KKkR9oc9nh3t8smjI3705JgHe0PSxNRmoKBaRoBFXn57pXCR
                            INUK3LIVs9VzP/0Jl7OClxdjNM/4bd+QapmpJpsB5fu4/ftpwm4/5Xh3wJP9XZ4d7fEnjz0K/4IAACAASURBVEvj/ujhAT843ufJwQ
                            6P9nfZ7aUYI+Ux0psHJa4/F1p+eH00mfF4b4cHu0Me7w15sNPnq3eXfHl2yR/PZ7weZ7yd5IwyJXdNv6D+95Mts22zCssAgUbHDDUJ
                            4iOoOt7+oMezw11+9PSYnz57wCBNb9z9byTbPgpM8vJK0SLCX393Zg3QK7fglb9yuHnWfAMEoZck7PR7HA77PNof8nh/hyQxzaawHy
                            pWLSjygizPPBNkuaVB8e+W0VhewGiWMctzDvsJQ8lJshmST8vMrleVfpLwYHfIB0d7/NkHj/jzF4/4yEZ8R7uDarq700voJ+VCZit3
                            1ZK2hrzujisi9Ixhd9AjMYb9YZ+Pjvf52fOHvLmY8MXbc37z+ozfvL7gV9+d8fXFlItMyV3bVwkCaY6x945pSN4HhGaAdygJ0ig2kF
                            gT3Bv0eLg35OnBbrl+tG5fpsxDTLMcI8JLexFWszDQ816gi7Uldf16iWHYSxn2U1L/83n2dVzWtigKsiwht0kJd33Dm0gojSUrCgo1
                            DFNDz0CKlp/zK/LSO4yQJgk7vZTj3SEfPTjg0ydH/P2PnvEXHz7mB8cHHO/1GaQpiZ3quuo2f0Te09y3OajXNdv7WaiqJCLs9FOGvQ
                            T2dlBVzidTHu8PORz22e/3UISd/ohvR7NybTC3U2v/9dqzjiCSFqtmYSgcA2wEWO2G8g3Jj2a2wbrKR7X2lBhDLy0X0f1pYnW1Z9Px
                            Wx+3YfYWm+HsGVN+BK3Rtu7k8+qxKAnSVitCKj8jV66NVWWx5Sqvcg3GlAZcFIY8z0sjvKEDlgYISvleBkiw2XcULRRUMWkZmT4/2u
                            eHjw/5+Q+e8OOnD/jR02NeHO9zvFsmbUrzs0lr6nXLrt9bfh/muJHyfcprPEJq3zc1hqPdAY8Pdvns7QV//fqc37wZ8XI04XSS4fJV
                            82vN0hr47jLzTPCmI+KaFI4BinfrBuYgEh5dbP7o2eCn+v2O8vHtfwRpGaaUv0xX2L+54nUlPDqTIN0qbFRXvkexVN3ElFe8LrS8+E
                            B3YmSxFO8CNKq4tb76/UCMYW/Q48XxPj/74CF/58Vj/rM/+YAfPj7ieGdYDkSmtMzcfpaxKsEKza/NXPu4euwN+vSShEf7O3z88IAf
                            vxvx8Ku3pMkb0jeC6pizSU5e2F/1c4XcetJi1cw7AoFEg+EYIHBXkyC28M17LnJaY0eT1kmkrdvuMnp1a7BF+9uIy76372FXla+UwZ
                            jatNyaYGfZu17La3P3cSL3Wmli11yP9/jJswf8xYdP+DsfPOZHT495drBHPzX11NKquKrtVsTcffdeIkKaCL3UsKc9jnb67PRSJoUy
                            LZR+Wsa1X59NuJhm3uc3WwPwnO4iW2bbZhWWAQKNjjm39mb5Vtkie5k/qLf9EfRlWTuy6jy9xP3n1a2Ldb7S+9VNREiSBBEhz8uP5B
                            QdF45YZOqdw4zdZ3fY4+NHh/zpB4/4T3/4nH/w8TM+fnjIg72hzexe/x6bGZyaU8LEGA53evz50yMOhz2e7e+QmIQ0OeWP78a8G0+Z
                            5XbgcVGTP+66aeSdZBqS9wGhGWC1JkWrobyTwTfIrTDL5zTP2utD62LXlwSvTeVq1qn3q5t7bGzCpB0JOl0X0fpyn7kcpDt8+vQBf+
                            fFY/7sxSM+fXLEo72d6rWK1knUabAbYGAHKGsKqko/SXi8V34Vz2B4fTkjK8pkyDQvf+SqqKJAFwjUr3c/WBgKxwAbAVa7oXxDklan
                            3TTrKl8328T631IRoOuAfj262EK1NipXJ2SoI8QqOWBMFQ0CrY/IXB0Bum/zGhGGvZQHu0P2B33+3odP+AcfP+XTx8cc7QzpJeXnLl
                            2MuelobxkmUiZFkkQ4kB4fHu3yD188YJAaclXOJhnTrPz5A3Wt0PByvcPMM8FFE6kNKxwDFO/WzgDCSHh0sY6j14XWbHhd5tdZFDcl
                            Ea8eXWyR2u8hN6ubu+8bINQmeJVpeG9JLzEc7wz46MEBTw52+YsfPOFnzx/xaH+HxJQfmWm3ffv1QmCIVF+pO9rp8WdPDxmkhtNxxj
                            dnY8aznJPxrPl97mASGbdhVYQTTDQYjgEC1RpBZYJ+h3U7uY3bYu5+S9I9pG1mnWlZ+WG2tNii/Rdvvkn5/EhQdT4x0n5N+6TKfEWE
                            3X6PHxwf0E8Tnhzs8vGjQx7t77DTS8k8M+0qY2jMJUkGqdBL+kzzHX70aI8v3h0wzZXZm3Nml1N04eHpgqGzZbZtVmEZINDomCLMN1
                            bXGbFJtih2nz+ojVGf+ahkVezaKXAFW+bXxTpfaXV18yPBdmJkkakLQiqG4+GAn33wkJ/qQw6HfZ7s75C6r7K1yhRSxLeIoYpK+TnH
                            /X6Pnzw64HJW0EsMp5MpZ5MZRe79Ip9QTyP9sfjOMA3J+4DQDNCFyHP90THfELfFLJ9Tx1TUW/dZJ7u+JHhtKlezTq2ubu5xV2Kk40
                            2A8lsoA/td66PdAf20vDzXXr/XeA2nRRFoiKwsutJLDE/3B/z08T5nkxm/fnXG69GUU1UytU2hUA1YjYHiLrIwFI4BNgKsdkP5hiSt
                            Trtp1lW+braJ9b+lIkA3Am84CdLF/NurEiMuOhIgTQx7wx7DIiU15YUnUmNInKkyH22GFu1dxRToGeF42CM73OHN5ZRPH+5xOp7xJX
                            AynlUXYq2ORyNI0DvCPBNcNJHasMIxQPFu3WgXRMKji3UcvS60ZsPrMr/OorgpiXj16GKL1H4PuX3d3P1FiRG8/dLEsCe9qk+VEWV9
                            f9sGdluGll8jHJqE42GPFwc7/OnjA0bTnGlRMMpyZlnhKlz3jWCSG8uyKsIJJho01++yQbmOVvmM32BupwBYl1kskQRZF1tejTC7xR
                            btv3jzbcvspsbGmMZfe7roosCe/X51YsrvBkurE7WnmneFIfX3h4e9hEe7fX70cJ+fPN7n2f6QQZLMH7YlZyFhsWW2bVbhRICVvChL
                            hPnG6uqwm2SLjGf+oPqjvrtdB7t2ClxBV35ZzDpfaX11c/eXS4x4xyDASO5WDCgory5+NOzx0yf7ZFrw5btLfv3qjLeXNj5w00h/LL
                            4zTEPyPiA0A3Qh8lx/dMw3xG0xy+fUMRXVmARZlrlI0K/TfGJk+0mLdTG/3sOe4cnegA+Pdnl+MOTBsM/b0ZTxLLcXUnXLGHW7+IPC
                            3WBhKJwpsPq3bcNxj9Xri9tijrfVHSWpepdR90b+VbJrS1KNvF49uthCtV5RV1s311bOBJMkIUmSuenwJpYTtslcO6di2OulHA97PD
                            8Y8uHRDk/3hwx7iXck/INmn9s4jiEybaIAFI4BSutWq/+aO82ttW2DdRy9LrShSOLaolRTEq8eXWyR2u8hq6tb2wxEpDLAtgkGM11d
                            MxMp1wN30oRne0N++GCPHxzusNdP7STJHg+lnqEo5XEMmkld6ECCwXAMEOoDW5mgazCPrTO5sSzrOnr3KgnSGIUWnqyrqEeXXCS4KD
                            Gy6PnXMXexUvHvu/3f4/XWxco2gEFaJkQ+PNrlg4NheaXvueiq8azA2TLbNquw1gCBRucTYb6xujrsJtmis697CgxUHb896q+Ktc2w
                            8/QS959Xty7WeEI7LF993fzIx48CYbnEyLJRVmMcc1LviAYUBSplFNgzwqO9Pp8c7/LdxZi9l6krZvMwqXoRfcgsnMjPKSwDdCHyXH
                            90zO+U22KWz6ljKlpNaWSt7PqS4LWpXM2c2u2/xrp1TZUdvy4xsmia7aK7Qil/mFzxLjNFtT0RQQwkCGLqn8Gk9XqbWs4QkWr1JzWG
                            o0GPZwcDnu4N2e0lJCLMqif5d7RR5vBZGArHABsBVtcwZ3eK3wRZyBaWxI3Afj26WPXs+fZvUOW9vwlyHWubAix3KS1Xn+o3OeyvQs
                            1yZTItGM1yLmYZk6ygQOkZQz8pv2K3kyYMUsMwSUitAa3rt0OWZQokRsqLpu4Nebw3YK+fkiamw0hs52kEDiEyzwQXTuM3q3AMULxb
                            tX9BfOuji3UcvS60ZsPrMr/OorgpiXj16GLNJ/kVKY3A27SqerS3d9VN5OpLaaFl+VXLHyovUDSDrFBGs5y3owkn4xlvL6ecTXMKVY
                            apYaeXsN9PORj02B+kHA5SdtKk+vU4qcbBzU+JUSUxQmq/HfJg2OOw32MnTRiZrLzmYTXNlLq/BPOtjy5WRTjBRIPhGCBQrRFUJuh3
                            WLeT27gt5u63dC8vh1VuLbA/jGRNUKsBfTX1WEZuOuxME2oTNDZimuXK+TTjbJJxOplxcjnjnTW+d+MZ7yYzLqYZhcIgMQx7Cbu9hI
                            N+yv4g5cFOn+Ohu+2x20vop+W0k1a5G220JiZAmgjDtDTqw2HK4bDH+SxjkuVzl/3vPo4hsWW2bVZhGaA3+tUjhBvh/X22yKrwdK7w
                            HdWZj3LWxa4uiSt6FdJ0sNau9r5Srp3N8qK65t4663ad0bcTI1oUCJAXBeeTjD+8G/GHtxf8+tU5v3tzzncXEy6mOeM8Z5oV1UVTjY
                            iNsIR+YtjtJTwY9nlxOOBnj/f5s8cHfHC4w8O9IcN+eeGFolWWda4D+jJG2OknPN4b8HR/wMU0402hTIu8PmJCq98QKLOP4xT4Bqqm
                            OQGwReqaim4oWliubC2j62Kdzy3fw/00pnu7VdVjkZkvMngXCbrnTgvlcjrj5HLK12dj/ubVGX/7+pz/+M276pJS07ygsIbrt5Yrlb
                            EmeDRIeXEw4HI8ocgyJlkGCA+AYVpmYKtZ3JJlvj0ry9hPDMc7PR7u9HnZn/BuMmsG9C7JULWVhMmgdX+7CscAq4O5aEomVB+ulADY
                            XPEWR4Du/rrZlRKgnfDoYljmWYXSnAKvuh43nTYDJIlBJGU0y/nDuzG/+uaE37055zdvzvny3SVfnoz45nzM5TSz59SC88qeb2MjjG
                            c501lGNpny7nzEd6cX5HnBnxRHPLTfxEjEsMrp/zJLGyLWAAc9Huz02esn1aXAqiMkUhlzVa/gmDM+iRHgnPxOqbQa0tupGoG3xBZp
                            QQTo32+b1apZta0N/NHYi2DmmP/s1ntpZSK61rq1jXERKxSmBbweZ/zquzP+1e9f8TffnfLV6SWnkxmX04xZ4V1CamGoW/NMlbfjGa
                            PRiJcnp7y9uCw/fCxgDDza3yG10acfAbbrsSqGSHVY+onhYNCza5Np/XEdBYw7lv4xDZS5QscI8Bq5BnLRl+ulLjGyVdbhhAsiQGia
                            xTrYtWuAjdEYqgxdg/nV8qM/36zqTauqhx8VtrWIFapczvJyyvvdOf/x5Rl/9eqcz95c8HY0ZZbndgCl87gsUlHAtCiYTjPG45yege
                            dfvWFgf4pzf1j+qHk9o6tfu6seq2AoCELPGA4GZRJkp2dIjN1Yref6EQQBM8tjBLhI7fCrCgk9vG22vNa7PrRkJtgbeKt6zLGbaxX1
                            cK9zk0gpL5SXFxP+9Rdv+DdfveXffvWOz08nnExzZn5U213oeVN0zBmmMeSF8upiyr/94iXT6YS9QcoHR/sc7gzKr6N5kfA613nd4e
                            kl5WcCXQSYdB33q+oWDIP3PuHWoAANsEP+dG3bbJEWTIHvehKk/ERcaV4i9f7bSIIoMMsLLqYZX52O+Q/fvuMvv3nHZ28vOJlkzAoq
                            A6vC1Spir8I271h1MAGSBAVG2Ywv354zNMpPnz3gzWjM8d6QnSohImsZ0ObWTCkvCLvbS9jrpwxSU0+B3exk28mNZZkrcyBT4HAuhu
                            DaqrFW4Es6ArAtsrnizTN3MndNWVfJlpJAbQhXMOZjXGMMqTGkRmz0s7p6dCVBFrGsUN6NZ3x+MuI3r8/5tZ32vh5N7Q+JC4gpDdAY
                            qmMnfqe0jxey0kDVlO93MZ3x+nzMVyfnfPHmjJenIy5nWWNV4aoy34b5xymV8vOAu72EQWJap9uydds28wzxZhOptSmcCFC8W6UOoR
                            t+6JnRttgiLYgA/ft3Iwky/9REhDQREu+qLNtIgszyglcXE37z+py/eXXG5+8u+O5iwuU0o3BGJy76K+rzp9EB/Xp3MNcgUn7lrCjg
                            cpbx8mzE569PORz22ev37LX5TLVGuo4kiIhUr5+Y0gCHaUIvscfBnaPL1i0Ehnc8AlA4BthWNby6CMX20pgE6YymGu/bLogfrihcnw
                            SZr5oRO+3yop5V1GPZJIgC07zgO2uAv31zzquLKaNZRl5omQltvIaxZS2aJthuoTZzA6/9K1CmWc7JxZivTy54erjLRw8P6yat+vh8
                            PVaSBLElK38a1LCTGnrGzE/dlqlbEMzyQCLAcKbAldo90Rs1qkFk22x5XRXRrIpdK68qVT3m2OKnllMy6wn+y62gHv79K5nCNCv46u
                            ySv/7ujN++PufdeGYDi1bncoV1U2HxSt3VZH47eubn/rJCObmc8PW783IKPM1Kn0Q6m64zKn9fZh+6CHCnl9BPvSmyenXqOh+CY4E4
                            n1W4EaCvxvrBltkiLTiZ73oSpN63jTabBHER4JvRlC9PR3x7Nmac5XWQ7pezYfKtSLARxdvBtrEcIPWtNc5ccy4mM95ejHl3OWGa5W
                            U5q6Cxu8yrYK5cRqCfCP20XI+dC5i1VY+uuoXAoHV/uwrHAKvzcVFIIsRvgmzqmyDzdWtvXmU9llkXKwplnOW8G894dTHl5HLGLCusA
                            UptAOWTLbN1NIZqXbkoqC6w0djPq6FjttZFAeNZxul4yvl4Wn7AGq8ZF5T5tgwtfxwe1cZ3l83c8eioR1fdts7cMXLtu32FY4B+p3Qn
                            q38Su41u+7bYIl0znbmrSRBXt/bmTSdB8kIZZwXn05yz6YzxLCOvOpnWt37dxFUOytWeJRMj/sH3zPd8MmU0zcjzYu5wrysJ4gcERsT
                            +tQ/QgnqEyPDaPgCFY4BtVVMR9UZjF61sm3W4xYIIEJpmcReTIOus23VJENXyO8jTvGCc5Yyz8qouubsWlHj18Kf0jYjO3VkyMdIaAQ
                            uF6SznYjpjNJt5EWA9MK4tCWJvDdiPIpmOCJDuegTJLA8kAoxJkPdiy+uuJ0Gu0iaSIAC5KpdZzmiWMc3moy/7hCuY1Ea5bGLEPY3yq
                            3eTLON8PONiMisvC4YuDGJWmgQBRBUj5bUB+0n5ecyuAePqNgiFBeJ8VuFGgL786dq22SItOJljEuR2SRAFiqL8KMokK8i0NJ9yJ/eC
                            NI+VvwblT/Or+l6RGGkfc/tSWa5MspzJLK+mwG6vdSZBHBMREspLdy00v0bZq9A0LOYOWJwCt1RNwxaFJEJMgmwvCbLOul23LpZred2
                            /aV5e8r5ZW6+zVVP6q5it98LEiKuvNt4CVbK8ICvK9UhV++0WpbPMK10HtIUWe5hk7nD5deuqbyjMHQ8JJhAMxwD9TulOTP+EdRvr82
                            E7bJGumc7c9STIpurWNV0uFPJcyYqCotBmcRodS5t162SuwtCdGOlqQbX/lELLi6vm2vydlHWZXyOCVpq3dSPUgUMjCg6QuQrECPAau
                            QbaesKji3W4xYIoCZpmEZMg8xGTz9rvUZug2p+1vKp8Xmh0JcNrpAWJkTnTtyao9uc1vZ8H8Mu/6iRI53S3S359g2aWBxIBxiTIe7Hl
                            FZMgVzP/fmcSRMv7Bdf0ma62uJLZAUCkOzEyp9q0Cy2q3xjufot5eBu2tFvcuA22wQJxPqtwI0BfXSPyttgiLTiZYxLkdkmQ2qjL8Gv
                            +E4nUEW5jyrUMw2sDLxLs7KTlOyvllNz9xoh7f/XKvI4kSLu688VrR642kAiNuRrEKXBL1TRsUUgixCTI9zMJ0lC7qn7Hr6b0N2W2Lf
                            zEyNzPnF7RQCL21F1vEgRap6HfKL7Bz9UtFObaXoIJBMMxQL9TViehMG9GbJct0jXTmZgEWY7deIrf6FjarNvSzDUClKtCSpUcuaKBf
                            LKRJEjH+1blc4FDI+INkLkaxAjwGrkG2nrCo4t1dMwFURI0zSImQZjr5D5rv8ecCXb1G9+o5H2Ze213nA3umoCL3rhssmb5150Ekc6S
                            0F3OIJnlgUSAMQnyXmx5xSTI1cy/vygJsmRhVsDsoCBCdWVpkWva5+roeBVs6UZYSRusmwXifFbhRoC+/OnattkiLTiZYxJkRUmQ6sl
                            d5aN5rPw1qPdhiGd+stAEbUnnyhyTIFcwV4M4BW6pmoYtCknc1MTfvEU2V7x5FpMgy7EbJUHmDNHrbNWU/hbM1Vftm4k3Fe6YjpbfCe
                            4281Ux/+Tr7h1al3mubiEx186ufbevcAzQ75RKqyG9nZrnw+bZIl0znYlJkOXYtVP8Nmp0LG3W7TasMR22RuhYoyjrNb+YBFmvwjHAt
                            lwDbT3h0cU6OuaCKAmaZhGTIMx1cp+132NzSRCPNRrDM0F3IT77uLFXRz1iEqSLWR5IBBiTIO/FlldMglzN/PvbT4JYSfuBNTwxiEkQ
                            a36LopiYBLmKBeJ8VuFGgL786dq22SItOJljEuQOJkE6m9RFggYxglQ/Eaqgal8mJkGuZa4GgUyBw4kAXVs11gp8yXxwuE02V7x55k7
                            grinrKtlSEqii2atY53PXV7euJMiijl+X2ZMzSWcAruO9L+t6D//tjZAkKUmSYLxM8XX1uA3zD1B373CGg1ePEJlniIEEguFEgOLdKt
                            6I5m1bVSLjNmyRrpnOxCTIciycJEiXSmMyJiFJSxNUBaWYM7B23WISxO9Q4USA4RhgW9Vo7CIUd5JKAKyjgyyIkqBpFjEJwlwn91n7P
                            bafBGm/vb06swjGGJJEKQrQorxOYEyCXMcsDyQCDGcKXKl98nmjRjWIbJstr5gEuZr598NMgsyrbELBJAlJkpCmqbcmSOdxiUkQxwJx
                            PqtwI0BfXdOSbbFFWnAyxyTIfUmCNCVif583SSiKolwPBAr7i3ExCbKAuRrEKXBL1TRsUUgixG+CxG+CzBui19mqKf0tmHuPZcY9KT8
                            OY4whTRPyvHwNZ4LterzvOqB/8nX3DlcPOuoWEnPtvNwgswmFY4B+p1RaDent1DwfNs8W6ZrpTEyCLMfCToJ0t4tLjPjW5C6ZH5MgLe
                            ZqECPAa+QaaOsJjy7W0UEWREnQNIuYBGGuk/us/R6hJUE63rx6CWMMqvVHfnwT9Ovk396EuZJ1Wodfj6CZ5YFEgDEJ8l5secUkyNXMv
                            39XkiCtJ5dPEZsdtkkR9znBVSRGlm6EVbbB2lggzmcVbgToq2tasi22SAtO5pgEuZ9JkFrNgaicDpuqbrCaxMh1TVBN5auy2EAiNOZq
                            EKfALVXTsEUhiRCTIDEJMm+IXmerpvS3YO49ljbBrqQF9jOCSfX4NokR/+Tr7h2uHnTULSTm2vmmg8z6FI4B+p1SaTWkt1PzfNg8W6R
                            rpjMxCbIcu1NJkFZbtI3dN0C4fWJkURMQkyDvrXAMsC3XQFtPeHSxjg6yIEqCplnEJAhzndxn7fe4S0kQV2Zfq0yMuJJ1Wodfj6CZ5Y
                            FEgDEJ8l5secUkyNXMv3+XkyDly8zXdxWJkaUbYZVtsDYWiPNZhRsB+uqalmyLLdKCkzkmQb4/SZCuejh+28TIdU1QTeWr97WBRGjM1
                            SBOgVuqpmGLQhIhJkFiEuQuJEG6ExnvnxjxT77u3uHqQUfdQmKunW86yKxP4Rig3ymVVkN6OzXPh82zRbpmOhOTIMux+5IEWUdiZFET
                            EJMg761wDLAt10BbT3h0sY4OsiBKgqZZxCQIc53cZ+33uOtJkC72vokRV7JO6/DrETSzPJAIMCZB3ostr5gEuZr59+9bEqSLvU9iZOl
                            GWGUbrI0F4nxW4UaAvrqmJdtii7RgmhiTIN/vJMiqEiPXNUE1la/ewwYSoTFXgzgFbqmahi0KSYSYBIlJkLuaBLlNYsQ/+bp7h6sHHX
                            ULibl2vukgsz6FY4B+p1RaDent1DwfNs8WaUGU5N+PSZDvdxLktomRRU1ATIK8t8IxwLZcA2094dHFOjrIgigJmmYRkyBN9n1MgnSxZ
                            RIjrmSd1uHXI2hmeSARYEyCvBdbXjEJcjXz738fkiBd7LrEiHuPa5tilW2wNhaI81mFGwH66pqWbIst0oJpYkyCxCTIbRMjVdGuaIJq
                            Kl+9ng0kQmOuBnEK3FI1DVsUkggxCRKTIPOG6HW2akp/C+beY2kTfP8kyE0SI1cH7K4edNQtJOba+aaDzPoUjgH6nVJpNaS3k9u+LbZ
                            IC6Ik/35MgsQkyDKsKzHiKt59qFyZ/WMaKHN1iRHgNXINtPWERxfr6CALoiRomkXYSRCtH2+objEJspj5iRFDnSDptA6/HkEzywOJAG
                            MS5L3Y8rp7SRAt/9Terrlu/v3vaxKki80lRtIUIzYxsih6WmUbrI0F4nxW4UaAvrqmJdtii7RgmnjnkiDacX+NdYtJkMXMcWMMgqJG7
                            X3mTdBN5avn2kAiNFYWdrGJb1jhGGBjGtY5zyEmQTaUBNHqv43ULSZBrmZlkQQxWn5EJklax8TVg466hcRcO990kFmfwjFAv1MqrYb0
                            dnLbt8UWaUGU5N+/s0kQu0ujy62pHjEJsoABYgxJktoo0B4RsSeq+rd+PQJjrjYxArxGroG2nvDoYq6DaKuzKH4HvXtJkHY9SmAEjBi
                            MSCOKW0U9wk+CtM1QW2x9SZAuJkYQY8AYEFOWRVyZ/VuadQuGWR5IBBiTIO/F2vJdr7VlA9HBtfKqUtVjji14qgiJGHrGkCalCbr9v1
                            dJkIXlWK4eq2JlEsSanzFUU8pFZVxlu6yEBeJ8VuFGgL66piXbYuUGFAGTQJJCQnlrUjsqz0c4TsEnQaSul1LWS5IUkyYkJvGWde5zE
                            sTdN2ASNEkh1dYxrhpsrsyrSoIsSoyAlOZnBAqpY4bGDMXCxjkcAHMHLE6BW6qO2aKQRAgmCSIGkgTolUVPDToYor0hpP3y5IS5k3nd
                            7EoJcF0SRKTs4CkgCRQ5OhjCYIhJ+2Wdxdhd72kSxL8vSXlMTQpJ+/yjkQAADctJREFUhg76aH9YGqHXmdedBKlvbQNUbWDKOZzrN0V
                            BY03QN/hGfbfFXNtKMIFgOAbod0ql1ZDeTtVotyUGZbkkoTwBe9AzMNgBa4AiiT0H66O8/iSINGa1zbb1oxrqk7PNkNLkjCk7uWpZr/
                            4Q0h5iXPZxffXomi6LVP+1a9bqWNqs220Y2LYYlsaSFjDsQW+nNESvLBtJgjgG9QEWAGNvi7q/NCIw/zgHwPDKF4DCMcC2qlFY684ZT
                            BLEGqKxZpAm1VRRTEKSNBMG606CoEpqhNQYEiPlOp2/LtQYjV2bymLmOhZAkmKSFJMkpIkhNabcZUX1uC4JgiqJEVKRsm6LTLC84w2k
                            q2CUA50kQIEmPSRNMYkhScziMq+RlQkpd265PgINI/RNsN6hVbdtMctjBLhI7fDLPVYPB8I6ii7+Xu5EtBu1GgVXy5Y+l/x6yDVsvmp
                            go0ytqn/7etRt1D7udd1EpbNPNevWEVWsjDUbRKp2aIRiV9ZjNUzLwzTXBm5ANuWuhWeC/svdqg1Wxego0PYUoAF2yJ+WBMcULZQsL7
                            iYZrweTfj9yQW9ROgnyVLVu61UlUle8PZyypfvRpyMZ2RF4Z1nLrprPImG6bWZ7UB5UXA+yXh5PuaLdyN6iXC80yORzXyAoNCC0Szn5
                            fmEr84ueTeekRetjuQi3MaUa4XMvomqMppmfHV6yW9fn/Nwt9+Mrtcu5YuTS15dTJnlRWubO5atSDC0xIitR5wCt1Udn64hi5KFkgSp
                            WHlgc1XObMcwIozzgqd7AxLjd9AF9V0BU4WsUC5nGS8vJvz61Rmjad48ycQ+8bpvgjhmDWacFXz+bkT6pfCHkxGP9/rs9BI7zV5RPa7
                            YpgrTvOBsMuPl+YTfvr5gNPPqNrfAviZmhLxQvj4b8y8/e8lnb8/Z7be6z5qPMwpvL2f8f9+ccDbJqJcr8IybOhJUDSwx4trUbg9A4R
                            ig3wHdwfMPqts412G2zYSsUC6mGdO84PVoym9en9FLOler1iYF8gJmec7FNGc0y+qNjQiH+uS8ilmNs5wvTka8upjQTwy9xGC8frduu
                            VMhL5RpXjCaZVzOvOin0bG0WY9VMfs+mSpfn13yLz/LGKYJyRaCmKxQziYZ59OsZX71oFXKEGRiBK8sASgcA2zLNVAICY9rmZDlSpZn
                            XKpycrGZJuqU4J1cXpkXJTyuYUVRTvtGk9n2R22/bo3o1q/vmhiAwniaM55m220LF/l1tgFemUNMjFi+7XPJKn4TZBWsMZiFMbIB8+X
                            rKvN1zH+xrVftigK012rXwbylga1q0dv7a25i/0xo3xgJxPmswo0AfQWT8FjAquSBNQl1Jt4+UzfIGpHLLRiUzNhbF0msrMxdj+lm/p
                            LIuhIeyzCB5rdBrijzuti1bWD/EwgqMeLqEsgUOJwI0LXVlUkQb7/QmNhK+MUXypONLTB//WqVbOVldp3DvoeLXLqYMx8NgC1b5nWxa
                            8vs2tY+dpGgsV8dEb/tvf3XyjxDbPSn7SmcCNDvHEp9MBt+6BlPUMw7uJHdkHmdw3UWf7/IbslcQ0MQiRG89w1A4RhgW66Bgkt4dDGp
                            y6tEdiPmjrPrEFL3k8hWxKjZ1hMjlitBKJwpcCVrLo3HUI9sATIPR3ZT5mljC/HfRyZUU9KtJkYCcT6rAA2wQ13hckhMdb5DR7Yccx3
                            FRYOqka2TVUZorynoTNDFHe74+EsTq2TujTq60TYUjgG649NYK/DlHaQQmdhKRHYz5q9VuU4S2ZoYnuHJFhIjngk3+tP2FM4aoHi3jV
                            HE2+YbT1DMO7iR3ZB5ncN1loYxRrZ65hofNp4YwXuPABSOAbblGii4hEcXk7q8SmQ3Yu44uw4hdT+JbI2Mmm00MWK5EoTCmQJXsubSe
                            Az1KBYg83BkN2WeqilSZJthQjVN3VhiJBDnswrQADvUFS6HxNxCr0R2Y+Y6iosG3cJ5ZJtjlRFuIDHiXrSjG21D4RigOxaNtQJf3gEJ
                            kYmtRGQ3Y/66lOskkW2Q4RmerDkx4hluoz9tT+GsAYp32xhFvG2+8QTFvIMb2Q2Z1zlcZ2kYY2SbYe6AwFoTI3ivF4DCMcC2XAMFl/D
                            oYlKXV4nsRswdZ9chpO4nkW2YUbO1JUYsV4JQOFPgStZcGo+hHrECZB6O7KbMUzVFimx7TKimrmtJjATifFYBGmCHusLlkJhb6JXIbs
                            xcR3HRoFs4j2y7rDLCFSdG3At0dKNtKBwDdO3eWCvw5TV+iExsJSK7GfPXoFwniWzLDM/wZIWJEc9cG/1pewpnDVC828Yo4m3zjSco5
                            h3cyG7IvM7hOkvDGCPbHnMHCVaWGMF7bgAKxwDbcg0UXMKji0ldXiWyGzF3nF2HkLqfRBYAo2YrSYxYrgShcKbAlay5NB5DPToFyDwc
                            2U2Zp2qKFFlYTKims7dOjATifFYBGmCHusLlkJhb6JXIbsxcR3HRoGpkobLKCG+RGHE7d3SjbSgcA3Rt3Fgr8OU1dIhMbCUiuxnz15t
                            cJ4ksQIZnePKeiRHPSBv9aXsKZw1QvNvGKOJt840nKOYd3MhuyLzO4TpLwxgjC4u5AwfvlRjB2y8AhWOAbbkGCi7h0cWkLq8S2Y2YO8
                            6uQ0jdTyILlFGzGydGLFeCUDhT4ErWXBqPoR6JAmQejuymzFM1RYosfCZUU9wbJUYCcT6rAA2wQ13hckjMLfRKZDdmrkO5aFA1srvEK
                            iNcMjHiNnR0o20oHAN07dlYK/DlNWqITGwlIrsZ89eWXCeJ7I4wPMOTJRIjnmk2+tP2FM4aoHi3/ojR8EPPeIJi3sGN7IbM6xyuszSM
                            MbLwmTuYcG1iBI8FoHAMsC3XQMElPLqY1OVVIrsRc8fZdQip+0lkd4hRsysTI3ZHJQiFMwWuZM2l8RjqUSdA5uHIbso8VVOkyO4mE6r
                            pcWdiRAnG+awCNMAOdYXLITG30CuR3Zi5zuOiQdXI7jqrjLCdGHFmqPOD35YUjgG6tmusFfiS+eAwJCa2EpHdjPnrSG6NKbI7zGgaXj
                            sx4k6ARn/ansJZA/TaBqVu1IYfesYTFJN69IvshkxrJnanhjFGdjeZO8AwnxgBTNWRtqpwDLBUYf9so0J4CY8uJnV5lchuxNxxdh1C6
                            n4T2R1n1KxMjGSIZgSkcKbAUHYIFZc6spJ6o7qHgTEPR3ZT5qlaQ4rs/jAp/8rpcIFJ3N/8c7agcAxQtUAYI0wRKRrbpN1TAmOq8x06
                            suWY6yguGlSN7L4xAUQKRMb2r+jsR1tQOAYoMgXOUU5RHeOmwvUOZUNqoEwoQWQ3Y/6akVtPiux+MaQApog5R8wIZIqEYT2hrAEWoGO
                            QNwivQPZRUoR+M4LwjCcoJvXoF9kNmXodx+7UMMbI7gHLgHPgFaonNthpBTjbUSgGCMgY+A7lJcJD0P3SZGwjuh609YRHF3MjHfaARx
                            aTIJFVTLVA5BR4hfAdMK4GwS0rjDgUCpQRql8i/A7VVyDTcpNrTDeaBMg8HNlNmaeuThHZPWAyBX0F+nvgS2BEe51/SwrDAMvGGiHyJ
                            fAHRF6CjtHWR2J8hcRU5zt0ZMsx11FcNKga2b1i1fLWS5DPUCkNMEaADRXAKfA58Gvg98AbRL1Q2YXT/tMCYkIJIrsZq9aMoFo7iuwe
                            Mcq1ffg9yq8RPgdOQ4kAQ1kDLD8Co/oVIn3Qz0C+BHYRHoMOKb9UWBuPuKeGwKQe/SK7IVOv49idGsYY2R1lBTBGeYXwJcpnCL8DvgI
                            6PuWxHcn1u2xQ//SXIDwF/nPQ/xrl58BPgceIDEHNXDKiWljfJpO6JZXIbsTmzoKoOy8tUBkjvAJ+jepfIvKvgP8HeMk/+8dbLl+tMD
                            6O7fR//s/wX/0PijBCeYfIJcgRInvAAMUgInO9RoStsrkOHdnyzFMVTUR2h1mBMgVeI/I3wP+ByP8F/BXKG/6nfzwjIIUyBa4lOgb5B
                            nDfGXxibz9EeAgMgRQhRSVFtF7H9KdXm2Rqe7NEdmNWTYFptm1kd4UViGSgBeUnN8aIvEH1S1T/Evh3wK+AV4iMCUztMTgM/eKXALvA
                            c+DvovwY4UcoHyM8Bh4Dh6geIjJsRBPbmM411kEie2/mRxKRhc/KjjAFTlFOEN4AL4HPUX6L8BvgP6B8gzAKaerrFKYBAvzTf2FKc9N
                            9kKegnwI/ReQT4GNUn4I8R/Qh0C+f5EYp9yK6QTZ3YkS2DGt3rEZ0EVm4TECYonqC8A3IS8pPb/yB8pMcv6M0w3NgzD/7x0EkPdoK1w
                            Cd6mjwBfBDlBcILyinxk+BY/C+MuffsiFGx+PIlmPhn4FRnfKiv9LovqP8kPNXKL9H9CuQIKM+X3fj9PunvzQIu6juI7IL7KMMEYaU0
                            V+9DtjVsdbNlPmWjOzmzN8WWfgMClQzREaUH20ZUUZ858Ao1KjPV3hJkC4JBWXjlh+Mlupnp0zzINkQ3YebYF3DSGTLMf/4dUWGkYXN
                            yqWMwvaL+jaQz/lFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUV
                            FRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRU
                            VFRUVFRUVFRUVFRUVFRUVFRUVFfY/1/wPey+86CUYjogAAAABJRU5ErkJggg=="""
            git_mark_base64 = """iVBORw0KGgoAAAANSUhEUgAAAHgAAAB4CAYAAAA5ZDbSAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAy
                                RpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ld
                                GEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1Njoy
                                NyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcml
                                wdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLm
                                NvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yV
                                G9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpFNTE3OEEzMjk5QTAxMUUyOUExNUJDMTA0
                                NkE4OTA0RCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDoyQTQxNEFCQzk5QTExMUUyOUExNUJDMTA0NkE4OTA0RCI+IDx4bXBNTTpEZXJpdmVkRnJvbSB
                                zdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkU1MTc4QTMwOTlBMDExRTI5QTE1QkMxMDQ2QTg5MDREIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkU1MT
                                c4QTMxOTlBMDExRTI5QTE1QkMxMDQ2QTg5MDREIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kP
                                SJyIj8+R7ClIwAADR5JREFUeNrsnQuwVWUVx79zeWUXNWB4RIhXCCNUVLiCQJoBlqCIYaIBUpRGltMICE6JxojSjIKlhTmkgmjkoClqcBkTHeSNIAooQkTI
                                w3gooAKCXL39/+x1bvtezjl373P22nufc741s2ZzmXu/x/rt/T3Xt75EVVWVsVK4kiiESrRs3qI1Hp2hX4e2g5ZBW0GbiTaGNqr1Z0ehB6Efiu6CboVugW6
                                Grt29d8/7FnD4ML+MRw9oL9FyaFOl7PZBV0GXiC4D9MMWcPBQ2+IxCNoP+u0UX2NYwq9+IbQC+hxgv2cBZw+1BR5DoddCu8e0mCugs6FPAvYeC9gb2D54jI
                                ReBW2QJy3hMejz0IcBeoEFfCLU+nhcBx0rg6V8lrXQ+6BPAXZlUQMWsMOg46HtC2yG8m/o3dJ8VxYdYMC9HI/J0I4FPhXdCB0DyHOLAjDAnonHA9DLimzNY
                                T70FoDeWJCAAbaB9LF3RjjNiVo4zbqLfTRAHysYwIDbCY9Z0HONFcpb0CGA/E5eAwZYpv8L6Wu/ZLnWkCPSok0F6Kq8Awy4XP99DHqNZZlRnoGOAOSDeQMY
                                cDvgMQfayfLzJBugAwH5X7EHDLjfMs6qTlPLzZfsE8iLg0y0JGC4g/FYYOFmJbTZArFhYFIvQLgj8JgJrW9Z5cTj6salpTsOHT60JjaAAfcmPKaZAnEgiFh
                                ow4GAvAeQV0UOWL7caZZL4HI5IG/P9UuulyPcwdIs2y9XRwYA8ruA/Hboo2gZLXNA1dByUJXPoH2yHV0nsoTLee5yO1oOdQp1YTbz5EQWcLlCtRL6TWv3UI
                                WLId38rniV+ITLF2K6hRuJ0ObThYHOIAsd/s143JpjQQ9AOWigLzK3DQt9E4L1ZdO6A1qaY3259PsBBl0rA2+iZcvvDZP7Xu4Vbu8GpNuGgwjjOAAMhJ6U5
                                0A/Nc5SLTf4F6CuO1x1HYDHCzmmzz3lrkj37cAAy2b96yb3/VwOFlql2+xGPqcYx0eLXpX55ny3DvqwcXywPs5gx93QJjnmxf3kC7w4DXjtg8eZYDbrKzIV
                                ioaBPgRlXnRyX5EHYNlc9kOZO0vZP85QP9a9IoA8aZ/bAhlk4a37Bh53BGSM17z+IozBJo5HVK42znmhuAnL9AOZvsz38XeLAsp/vLDJKF42Bh40wflQ+Vp
                                bFU+HZ1GRuTK4uyNDWd6Twdu70J3Q90U5mDskfeNR+d1G0tdz0MPDaa1Fv2YcL8+zoKdn6AMnQe9F+Y5kYYPXA7JlI2Hzvaz7YHFt/UdABWLzVJqLs5kssD
                                wKPRu6VFoEfhHrgvaIkPn+OVCu2F1snINufIFuyMUzUvphvnBBndq4IpNLbiJDQepLhc4MqCDbUJDTAzA8y5xAWl+E2R4j3xJpVb4IIK3teLQJqGicgnVK5
                                1yfqYkeFiBcyq4gEpFmO/RT6wG/UP8NEHAHYTXD8yBLmpHxCvNDK44EfcaYA66GfkbRPAjW3nLIGyGra/0AvlWhENYv+v+isVo31hNgfOp9jc4q0umWa7W0
                                VUjzHGFX5xf8c62BKApwcrGTFRu0VEr+poyAJWzClUqZc3rTxX68x22g5eI0QBim/YKHGd2wCX0tX1UbNBCGaQEPVq7cAMtX3QaDUwLGp80AYtrRbO62fNV
                                t0B0s26f6gq9Sznji7r17nil2umKDu5SzGZgKcD/FDJeHUKl8koliEy3p7x7ZJsMD0ttCI7TC55yj4c3dYLnWmLFwW5JeIBpnubil2ZRhF5NfcC+jFzdjqo
                                WbsqnmvvVUpeQbCdPqJrqnUkbcEL/H4kwrk8RGGtLTDbiXUiZPxDWGY0y+YtrmCaXka3zBXZUyecRijMxGx5km0NnTD2mHQgZb8IbaLUdvAy6GPWynkHQbf
                                sFa/sfzLDrPUqGUbmcC7qCU+GLLLXJbdSDgMqXEV1pukduqTAswXWO3WW6ehbaq1ALcSiHh7RhgfW65eZ4uEe5OhaRbEXAzhYQ/sdh8ywGFNJtpAf7I8vIt
                                B7UAa/hJ1bO8fIvGpsPJBKwRJaex5eVbNNyKG5YoFbbU8vItp2gkqgXYxs6Kic20ALfyGw2mmEVOLrbQAlyp9Da2tug8C22l4a5cWaI4pTnDcvMs7ZTS/ah
                                EaYKtWehCFK2P4QAB71VKvNxy8ywXKKW7l4B3KiXe03KL3FY7NQGfJ+64VjKPoLlm0FkT8GalxLlc2dsirFN6G72l3c0EvEmx8IMsvzrl+4ppb0pIMNDtSh
                                lw25CxKQ9bjimbZ3ZhjD6kdTD+tBKJhvqhUgYs+FCLMq0MVYS7j2yTS5WrFSsxOhlEzEqNr5fbg6MVszgeNjJp+KWKGfGQ1Y8s0hPkeqN7+/kyN+AlypWZJ
                                LGgrZjquNiTlLNZ7AbMH44qZkbHvvst2mr5g9FxdkzK0RqAJSzuIuVK/RRv7hD79bZgkJQRytksSoY6dg9+Xgyhfo+ggj2KGC5P/IVxDWB1CGg34OdDyJgh
                                /Oajot2LEC7rPM+Ec+nInBMA45NmxPQwjptwgPESKvzdIoLL+Cf/NEp+V7VkpbA84Qum/DWkOrOiFaj4BGi9AgZbD8qwSXMVFzRqyyz3D7UB/80454rCEOb
                                9W+hCGOHcAoTbRaaft5vwbmc9JgxTA8anvdfdfockHHishkH+BG1bAGDPgP7FOCtJYY815tQOmZFIUcBL8HjV54oJR21MmNECuHnNLbD6Wb6B7Cb+jIKuzC
                                OotONFxonUy1CCUXU7vWG3VzMClgLzCrvzPSTI20NOrX2SEH/fHI9R0DEme39fhl56Sl6eNXJXQ6z6V+Pc68SgY4yQH7WT4Vuw0Xm1/zORYTLuNfrLb5Dw7
                                2r9/SJZSZkpX+T5ORae18G9Jq0F7x1ajzwPhAyU26q8zqdcWinC/UqM3rnrYZMnvQJm88pAXV6DqDwAvQ0ZHHXN+RhprUJcUmYbV3i9gITbnAxewuvvfh30
                                NTtyMcmD0o/SQ/TUGPcStEPHVFfrZLo3iTtAM3xkwhdiCDJZ40qD3gq3SBPG5vbigCvGLuIid54BQ+4qI+FGJt4yAjaYkW6qkk7YRK/zkQm3vpbAKO6r1ug
                                OxGtp2TcMMsGHaxqjBVdmFdwnHxdzuOulK0wpdV1txxUYv+GQeD9SXxhnaYr0+sukP5BBBbSL9g1oMpjiix7XW8/7syvMtNiQ6Q2uMP7vLuRa69/ddwewH4
                                ZyqY59xOMBVey+MK63kxnCvTGFOy8T3DoBi7AP9btXzL1Od4g+TnHYn02U9DbmWDE68z0boiEZxPtIzOCSya/q+qUSD28wR2h3ZlGAAdIkG/Gq5IrVOJne8
                                N6CXBzuX0E6oV2VJzebvhIzwBOEjcn1C6bQG2NVFoWY4rq1cwN0oUybOJfk1bXvZFm5pREYNE6R+zj4m+zlF0s8vsHsO4cZ/xdMdjQn3jLC+3i54/FH4xy6
                                mgL9zEeaHJm/FIFR4xLUnAyGpbtONtsv2MilyKOymcrU+vll6Z8/ZdMN5T2JXOa7XeactZ3kPzCOOxH77wtlQv9mBIbdGhPAoyRavCfxvY2FJpbLYX6d2Xu
                                iUMvSpEe402ShZCx9ifB/TYyzf7ofP38iv1cuCyYvsqkP26rIvwyP/0QMdxbq7sv22Tikj4Su9fk392fY2OdLxrXqm6Fnyf/xanVueKwQ2EZeArYGN0Zk3I
                                MRw10ntjeqgPEGcXmQ9xv6OTjOpnVCmvS24HGacc4wrXb1M9vki0lO0XgX0GXQn0Rk4MoI4bKbulJG874ka08D8Y5cYPw5kf0ShXzI5KGgvtw52h/RoCrly
                                qBWE5388pZJn+hnNWkqDDVZdmryTaIoM207JFu4OQEWyC/gMdwnZPajbwDypXkGuDQCuMNh45xcqAJxBpOtxceyeGHoljPdOL5Euzzm9VU89oQdjzrkUTTh
                                jkQdc76RJRGgATh8n5lDq8Blt/Uy3zwg82GWj+GOuXFRJqPrptAmEXh0hAU4+eUG4sIcWAhbFghGYFC12SY77/32xrsHSdw34HMZUF0nXV8gEujBbBSMW4v
                                fMY6HpaacVIBwabM+QcINHLBApo9UN+ibxopX4cJRt3SrfbECLJB5NoabCo9bdnUKXaN6us8TxR6wQD4E/TH+eYNxnOOs1BTa5EbYaLisDpq8AuwC/ahxnO
                                5WWKbVQlt0CWIaFDlggcxoevToGG387ykX2iiZ26O9YJNNYWQYWngjLkxAf28c78TnihAu69wJNpgS5iJN6PGrOJiA0ke6j3G2BAtd6Ld9KesM3Rp25pEFK
                                ENl6cTGTfwfGv/uMPkQkmmD1K0cdX05qkJEGoGOJwahPNLCQ108drnc45/ui6C4Xl2HV0hdzmbdwvDdziSxuxmlZfMWdA5InrNNtWK1GkYrj6hs9Cztmgb+
                                08Y517w0TvaM7dU3ssF+jXH8v3pIWXm4+WdaiwIeylSGB0/vX2KcTQG2ONwUeBpl2h9HOyaqqqqMlcIVGwW2wOV/AgwA+MQnGo+UarEAAAAASUVORK5CYII="""


            st.markdown("<h3 style='text-align: center; color: black;'>The team behind MASK GUARD</h3>", unsafe_allow_html=True)
            st.write(" ")
            
            ad1, ad2, ad3 = st.beta_columns([1,2,1])
            with ad1:
                st.markdown(" ")
            with ad2:
                aderemi_im = Image.open("images/Team/Aderemi.png")
                st.image(aderemi_im, use_column_width=True)
                st.markdown("<h4 style='text-align: center; color: black;'>Aderemi Fayoyiwa</h4>", unsafe_allow_html=True)   
            with ad3:
                st.markdown(" ")
            ad4, ad5, ad6, ad7 = st.beta_columns([2, 1, 1, 2])
            with ad4:
                st.write(" ")
            with ad5:
                aderemi_linkedin = f"<a href='https://www.linkedin.com/in/aderemi-fayoyiwa/'><img src='data:image/png;base64,{linkedin_base64}' style='max-height: 40px; max-width: 40px;'></a>"
                st.markdown(aderemi_linkedin, unsafe_allow_html=True)    
            with ad6:
                aderemi_git = f"<a href='https://github.com/AderemiF'><img src='data:image/png;base64,{git_mark_base64}' style='max-height: 40px; max-width: 40px;'></a>"
                st.markdown(aderemi_git, unsafe_allow_html=True)    
            with ad7:
                st.write(" ")
            st.write(" ")

            ma1, ma2, ma3 = st.beta_columns([1,2,1])
            with ma1:
                st.markdown(" ")
            with ma2:
                marcin_im = Image.open("images/Team/Marcin.png")
                st.image(marcin_im, use_column_width=True)
                st.markdown("<h4 style='text-align: center; color: black;'>Marcin Szleszynski</h4>", unsafe_allow_html=True)   
            with ma3:
                st.markdown(" ")
            ma4, ma5, ma6, ma7 = st.beta_columns([2, 1, 1, 2])
            with ma4:
                st.write(" ")
            with ma5:
                marcin_linkedin = f"<a href='https://www.linkedin.com/in/marcin-szleszynski-560b021bb/'><img src='data:image/png;base64,{linkedin_base64}' style='max-height: 40px; max-width: 40px;'></a>"
                st.markdown(marcin_linkedin, unsafe_allow_html=True)    
            with ma6:
                marcin_git = f"<a href='https://github.com/martinezpl'><img src='data:image/png;base64,{git_mark_base64}' style='max-height: 40px; max-width: 40px;'></a>"
                st.markdown(marcin_git, unsafe_allow_html=True)    
            with ma7:
                st.write(" ")
            st.write(" ")

            to1, to2, to3 = st.beta_columns([1,2,1])
            with to1:
                st.markdown(" ")
            with to2:
                tobi_im = Image.open("images/Team/Tobi.png")
                st.image(tobi_im, use_column_width=True)
                st.markdown("<h4 style='text-align: center; color: black;'>Tobias Schulz</h4>", unsafe_allow_html=True)   
            with to3:
                st.markdown(" ")
            to4, to5, to6, to7 = st.beta_columns([2, 1, 1, 2])
            with to4:
                st.markdown(" ")
            with to5:
                tobias_linkedin = f"<a href='https://www.linkedin.com/in/tobias-schulz-77b09691'><img src='data:image/png;base64,{linkedin_base64}' style='max-height: 40px; max-width: 40px;'></a>"
                st.markdown(tobias_linkedin, unsafe_allow_html=True)    
            with to6:
                tobias_git = f"<a href='https://github.com/Tobias-GH-Schulz'><img src='data:image/png;base64,{git_mark_base64}' style='max-height: 40px; max-width: 40px;'></a>"
                st.markdown(tobias_git, unsafe_allow_html=True)    
            with to7:
                st.markdown(" ")
       
            st.write(" ")
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
            st.write("""INQUIRIES: \n\n maskguard21@gmail.com""")

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
        
        col1, col2, col3 = st.beta_columns([1,3,1])
        image1 = Image.open("images/logo_large.png")
        col2.image(image1, use_column_width = True)


        col1.header(" ")
        col2.header(" ")
        st.markdown("<h1 style='text-align: center; color: black;'>Let's make the world a safer and healthier place.</h1>", unsafe_allow_html=True)
        col3.header(" ")
