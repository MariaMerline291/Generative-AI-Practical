!git clone https://github.com/ultralytics/yolov5
%cd yolov5
!pip install -r requirements.txt
!python detect.py \
--weights yolov5s.pt \
--img 640 \
--conf 0.25 \
--source /content/person.jpg
import os
os.listdir('runs/detect')
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open('runs/detect/exp/Person.jpg')
plt.imshow(img)
plt.axis("off")
plt.show()
