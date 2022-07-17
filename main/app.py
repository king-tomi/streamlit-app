import streamlit as stream
from PIL import Image
import numpy as np

def main():
    stream.title("Tumor Classification app")
    stream.write("Hello! welcome to T-Classify, a Tumor classification application that allows you to classify a tumor image as bening or malgnant.")
    stream.write("Please click the 'Browse here' button or drag and drop an image file below to classify your image")
    file = stream.file_uploader("Upload",type=["png","jpg","jpeg"])
    if file is not None:
        file_img = Image.open(file)
        fr = stream.image(file_img)
        file_img = file_img.resize((128,128))
        img_arr = np.array(file_img)
        if img_arr.shape == (128,128,3):
            img_arr = img_arr.reshape(1,128,128,3)
            
        main_button = stream.button("Classify")
        if main_button:
            stream.write("Tumor")



if __name__ == "__main__":
    main()
#stream.image("/Users/kingtomi/Desktop/Tomisin/Streamlit/main/Ticket Reservation.jpg")