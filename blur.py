import urllib.request
import cv2
from ultralytics import YOLO
import numpy as np

def segment_image(image, model):
    # Predict with the model
    results = model(filename)  # predict on an image 

    # Create an empty mask for segmentation
    segmentation_mask = np.zeros_like(image, dtype=np.uint8)
    
    # Iterate over the results
    for i, r in enumerate(results):
        # Iterate through the detected masks
        for j, mask in enumerate(r.masks.xy):
            # Convert the class tensor to an integer
            class_id = int(r.boxes.cls[j].item())  # Extract the class ID as an integer
            
            # Check if the detected class corresponds to 'person' (class ID 0)
            if class_id == 0:
                # Convert mask coordinates to an integer format for drawing
                mask = np.array(mask, dtype=np.int32)
                
                # Fill the segmentation mask with color (e.g., white for people)
                cv2.fillPoly(segmentation_mask, [mask], (255, 255, 255))
    
    return segmentation_mask

def apply_blur_using_mask(image, mask, blur_strength=(25, 25)):
    # Apply Gaussian blur to the entire image
    blurred_image = cv2.GaussianBlur(image, blur_strength, 0)

    # Create an inverted mask where the background is white and the person is black
    inverted_mask = cv2.bitwise_not(mask)

    # Use the mask to keep the person sharp and blur the background
    background_blur = cv2.bitwise_and(blurred_image, blurred_image, mask=inverted_mask[:, :, 0])
    person_region = cv2.bitwise_and(image, image, mask=mask[:, :, 0])

    # Combine the sharp person region with the blurred background
    final_image = cv2.add(person_region, background_blur)
    
    return final_image
 

# Download the image
url, filename = ("https://images.unsplash.com/photo-1634646493821-9fca74f85f59?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzk0fHx1bmJsdXJyZWQlMjBwb3J0YWl0fGVufDB8fDB8fHww", "scene.jpg")
urllib.request.urlretrieve(url, filename)

# Load the input image using OpenCV
image = cv2.imread(filename)

# Load the model
model = YOLO("yolo11n-seg.pt")  # load an official YOLO model
 
# Generate the segmentation mask   
segmentation_mask = segment_image(image, model)

# Call the function to apply the blur and save the result
final_image = apply_blur_using_mask(image, segmentation_mask)

# Visualize the segmentation mask before combining it with the original image
cv2.imwrite("mask.jpg", segmentation_mask)

# Save the result
cv2.imwrite("blurred_image.jpg", final_image)

# Optionally display the image (make sure you're running in a GUI environment)
cv2.imshow("Blurred Image Result", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()