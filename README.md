# blur-detection-OpenCV  

## prerequisite required  
opencv  
imutils  

## How to install it  
For opencv, please use pip install opencv-python  
For imutils, please use pip install imutils  

## How this code operates  
<ol>
  <li> Image is fetched using tkinter module</li>
  <li> It is converted into grayscale using cv2.COLOR_BGR2GRAY</li>
  <li> It is passed to laplacian function where 2nd derivative of the image is calculated.</li>
  <li> Comparison with the threshold is done. From the laplacian variance is calculated. If variance is below a specific threshold, it is considered as blurry else not. If the image is more blurred, it has less edges and it signifies the low variance.</li></ol>  
  
## How to run this code  
```
python bluring_detection.py
```




