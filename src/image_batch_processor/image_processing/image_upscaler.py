import cv2
from cv2 import dnn_superres

sr = dnn_superres.DnnSuperResImpl_create()

image = cv2.imread('./testbild.png')

path = './EDSR_x4.pb'
sr.readModel(path)

sr.setModel('edsr', 4)

result = sr.upsample(image)

cv2.imwrite('./upscaled.png', result)
