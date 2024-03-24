import streamlit as st
from src.imGEN2 import imGEN2
from src.imgVAR3 import imgVAR3
import openai
import os


# Retrieve the API key from the environment variable
api_key = os.environ.get("OPENAI_API_KEY")


#added by PaulB to increase the UX by showing inside the tab for easy access/ notice among many open tabs
st.set_page_config(
    page_title="PAUL AI ART",  
    page_icon="🎨",
    layout="wide"
)


st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Workbench&display=swap');
        .workbench-pixel-font {
            font-family: "Workbench", sans-serif;
            font-optical-sizing: auto;        
            font-size: 32px;
            font-style: normal;
            font-variation-settings:
            "BLED" 0,
            "SCAN" 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
        """<div class="workbench-pixel-font">::  AI CHILD ARTIST  ::</div>
    """,
        unsafe_allow_html=True,
    )
st.markdown("##### 👼 An Interactive AI Child Artist who can draw new images and synthetic variations 🎨")
st.write("a GPT4 powered app using neural network model capabilities - **Paul Biswa**")


#added by PaulB to chnage the default hyoperlink colors
link_color = "#e2dff4"
# Inject CSS using markdown and `unsafe_allow_html`
st.markdown(f"""<style>
a:link {{ color: {link_color}; }}
a[href="https://labs.openai.com/"] {{ color: {link_color}; }}
a[href="https://platform.openai.com/docs/models/dall-e"] {{ color: {link_color}; }}
</style>""", unsafe_allow_html=True)



# ... rest of the Streamlit app code...


def generate_image(prompt):
    # Escape non-ASCII characters in the prompt
    escaped_prompt = ""
    for char in prompt:
        if ord(char) > 127:  # Check if character is non-ASCII
            escaped_prompt += "\\u" + hex(ord(char))[2:].zfill(4)
        else:
            escaped_prompt += char

    # Make request to OpenAI API with the escaped prompt
    response = client.completions.create(engine="dall-e-3",
                                         prompt=escaped_prompt,
                                         max_tokens=150)
    


    # Check if request was successful
    if response and response.status == 200:
        try:
            # Extract the generated image URL from the response
            image_url = response.choices[0].raw.media[0].url

            # Extract and encode image caption (if available)
            image_caption = response.data.get("caption", "Generated Image from OpenAI API")
            encoded_caption = image_caption.encode('utf-8')  # Handle non-ASCII characters

            # Display the generated image
            st.image(image_url, caption=encoded_caption, use_column_width=True)
        except Exception as e:
            st.error(f"Error occurred while generating image: {e}")  # Present specific error message
    else:
        st.error("API request failed with status code:", response.status)  # Provide status code



# Define the pages dic
pages = {
    "Draw New Images from a Request": imGEN2,
    "Draw variations of a given image": imgVAR3,
}


# added by PaulB to increase the UX of the app : explnation 
selected_page = st.radio(
        " Select a Skill of the AI Artist", 
        list(pages.keys()),
        label_visibility="visible")

# Display the selected page
pages[selected_page]()


