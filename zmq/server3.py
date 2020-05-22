import cv2
import imagezmq

image_hub = imagezmq.ImageHub()

while True:
    rpi_name, image = image_hub.recv_image()
    cv2.imshow(rpi_name, image)
    key = cv2.waitKey(1)
    if key == 27:
        break
    image_hub.send_reply(b'OK')
