import streamlit as st
from openai import OpenAI
from streamlit_extras.let_it_rain import rain

client = OpenAI()
from PIL import Image
from src.utils import get_width_height, resize_image

def recycle():
    rain(
        emoji="🍡🍥",
        font_size=41,
        falling_speed=1.9,
        animation_length=0.99,
    )

def imgVAR3():
    st.markdown("## Draw Image :rainbow[Variation] ⚛️")
    #st.subheader("✨ Generate upto 4 numbers of synthetic variations against your uploaded Image ❄")
    #st.info("""###### NOTE: you can download image by \
   # right clicking on the image and select save image as option""")
    

    with st.form(key='form'):
        uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])
        size = st.selectbox('Select size of the images', 
                            ('256x256', '512x512'))
        num_images = st.selectbox('Enter number of images to be generated', (1,2,3,4))
        #submit_button = st.form_submit_button(label='Submit')
        submit_button = st.form_submit_button(label='✨ Draw Variations ✨ ', type="primary", use_container_width=False)


    if submit_button:
        recycle()
        if uploaded_file is not None:
            # Open the image
            image = Image.open(uploaded_file)
            
            st.image(image, caption="Uploaded image", use_column_width=True)
            
            width, height = get_width_height(size)
            image = resize_image(image, width, height)

               

            response = client.images.create_variation(
                image=image,
                n = num_images,
                size=size,
                )
            print(response)
             
 
            for idx in range(num_images):
                #print(response)
                image_url = response.data[idx].url          #added by PaulB to fix continous error in generation
                #image_url = response["data"][idx]["url"]   #commented by Paul by 21Feb

                st.image(image_url, caption=f"Generated image: {idx+1}",
                         use_column_width=True)


