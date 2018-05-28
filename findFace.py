from PIL import Image
import face_recognition
from hashlib import md5
import time


def my_md5(data):
    md = md5()
    md.update(data)
    return md.hexdigest()


# Load图片至numpy array
image = face_recognition.load_image_file("./images/timg3.jpeg")

# 使用default HOG-based model查找图片中所有face.
face_locations = face_recognition.face_locations(image)

print("查找到 {} 张人脸".format(len(face_locations)))
i = 0
for face_location in face_locations:
    i += 1
    # 打印图片坐标
    top, right, bottom, left = face_location
    print("人脸坐标 Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # 保存图片:
    face_image = image[top:bottom, left:right]
    print(face_image)
    pil_image = Image.fromarray(face_image)
    print(pil_image)
    pil_image.save(open('./images/{}'.format(i), 'wb'), 'jpeg')