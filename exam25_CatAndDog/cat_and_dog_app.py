import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only allocate 1GB of memory on the first GPU
  try:
    tf.config.experimental.set_virtual_device_configuration(
        gpus[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Virtual devices must be set before GPUs have been initialized
    print(e)

form_window = uic.loadUiType('./cat_and_dog.ui')[0]

class Exam(QWidget, form_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path = (
            '../datasets/cat_dog/train/cat.18.jpg', '')
        self.model = load_model('./cat_and_dog0.8332.h5')
        self.pushButton.clicked.connect(
            self.image_open_slot)
    def image_open_slot(self):
        old_path = self.path
        self.path = QFileDialog.getOpenFileName(self,
            'Open file', '../datasets/cat_dog/train',
            'Image Files(*.jpg;*.png);;All Files(*.*)')
        if self.path[0] =='':
            self.path = old_path
        print(self.path)
        pixmap = QPixmap(self.path[0])
        self.lbl_image.setPixmap(pixmap)
        try:

            img = Image.open(self.path[0])
            img = img.convert('RGB')
            img = img.resize((64, 64))
            data = np.asarray(img)
            data = data / 255
            print('debug0')
            data = data.reshape(1, 64, 64, 3)
            print('debug1')
        except:
            print('error')
        predict_value = self.model.predict(data)
        if predict_value < 0.5:
            self.lbl_label.setText('고양이일 확률이 '
                + str(((1 - predict_value[0][0])*100).round(1)) + '% 입니다')
        else:
            self.lbl_label.setText('강아지일 확률이 '
                + str((predict_value[0][0]*100).round(1)) + '% 입니다')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())