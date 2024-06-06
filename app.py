from src.convert_image import convert_image
from PIL import Image
from rembg import remove
import streamlit as st


st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## AI-Powered Photo Background Remover")
st.write(
    ":dog: The Background Remover Streamlit App is a powerful and user-friendly web application designed to seamlessly remove backgrounds from images. **This code is open source and available [here](https://github.com/Bhavik-Jikadara/bg-remover) on GitHub.** Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

my_upload = st.sidebar.file_uploader(
    "Upload an image", type=["png", "jpg", "jpeg"])


col1, col2 = st.columns(2)


def fix_image(upload):
    with col1:
        image = Image.open(upload)
        col1.write("Original Image :camera:")
        col1.image(image)

    with col2:
        fixed = remove(image)
        col2.write("Fixed Image :wrench:")
        col2.image(fixed)
        st.sidebar.markdown("\n")
        st.sidebar.subheader("- Click to download your image with the background removed.")
        st.sidebar.download_button("Download Image", convert_image(
            fixed), "fixed.png", "image/png", )


if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error(
            "The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("assets/zebra.jpg")
