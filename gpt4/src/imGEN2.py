import streamlit as st
from openai import OpenAI
from streamlit_extras.let_it_rain import rain

client = OpenAI()

def recycle():
    rain(
        emoji="🍭🍬",
        font_size=41,
        falling_speed=1.9,
        animation_length=0.99,
    )


def imGEN2():
    st.markdown("##  Draw :rainbow[New Images]  :rainbow: :potted_plant: ")
    
    with st.form(key='form'):
        prompt = st.text_input(label='Type ur text request for image generation')
        size = st.selectbox('Select size of the images', 
                            ('512x512', '1024x1024'))
        #num_images = st.selectbox('Enter number of images to be generated', (1,2,3,4))
        submit_button = st.form_submit_button(label='✨ Show your magic ✨ ', type="primary", use_container_width=False)

    if submit_button:
        if prompt:
            response = client.images.generate(prompt = prompt,
            model="dall-e-2",
            quality="hd",                                  
            n = 1, #num_images,
            size=size)
            
            #for idx in range(num_images):
            image_url = response.data[0].url

            st.image(image_url, caption=f"Generated image: {0+1}",
                         use_column_width=True)
        recycle()
    
    st.write(""" Few examples: \n\n Kids Enjoying Holi  \n\n  Sketch of Albert Einstein  \n\n Panda Eating with baby panda \n\n Make an illustration of a cat playing chess against a robot.""")
    st.write(""" Generate a realistic depiction of a modern kitchen with sleek appliances, marble countertops, and natural light streaming in through the windows. """)
    
    #st.subheader("Draw upto 4 numbers of new Images using your creative prompts :potted_plant: ❄")
    #st.info("""###### NOTE: you can download image by \
    #right clicking on the image and select save image as option""")
