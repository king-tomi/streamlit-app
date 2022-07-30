from typing import Dict
import streamlit as stream
from PIL import Image
import numpy as np
from keras.models import load_model
import os

def main():
    #Welcome message
    stream.title("Tumor Classification app")
    stream.write("Hello! welcome to T-Classify, a Tumor classification application that allows you to classify a tumor image as bening or malgnant.")
    stream.write("Please click the 'Browse files' button or drag and drop an image file below to classify your image")
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
            direct = os.getcwd()
            model = load_model(direct + "/" + "main" + "/" + "models/model.h5")
            clss = model.predict(img_arr)

            if int(clss[0][-1]) == 0:
                txt = "This is a Tumor image"
            elif int(clss[0][-1]) == 1:
                txt = "This image is not a Tumor image"
            else:
                txt = "This is an unknon image, please check well"
            stream.write(txt)



if __name__ == "__main__":
    main()