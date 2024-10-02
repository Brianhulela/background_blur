import urllib.request
import cv2

# Download the image
url, filename = ("https://images.unsplash.com/photo-1676385901228-64ad87402847?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjh8fHVuYmx1cnJlZCUyMHBvcnRhaXR8ZW58MHx8MHx8fDA%3D", "scene.jpg")
urllib.request.urlretrieve(url, filename)

# Load the input image using OpenCV
image = cv2.imread(filename)