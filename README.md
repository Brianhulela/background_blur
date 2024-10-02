# Portrait Effect with YOLO11 Segmentation and Gaussian Blur

![Cover Image](https://github.com/Brianhulela/background_blur/blob/master/cover_image.jpg)

## Overview

This project demonstrates how to create a portrait effect by combining the YOLO11 instance segmentation model with Gaussian blur. The effect keeps the subject (person) in sharp focus while blurring the background, resulting in a professional-looking portrait. We use the YOLO11 segmentation model to isolate the person from the image and apply a Gaussian blur only to the background.
For a detailed walk-through of the code, check out this [tutorial](https://hulela.co.za/create-portrait-effects-with-yolo11-segmentation-and-gaussian-blur-369b403a0a66).

## Features

- **Person Segmentation:** Uses YOLO11 instance segmentation to detect and isolate the subject (person) in the image.
- **Background Blur:** Applies a Gaussian blur effect to the background while keeping the subject sharp.
- **OpenCV Integration:** Uses OpenCV to process the image and apply transformations.
