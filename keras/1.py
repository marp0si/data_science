from keras.datasets import mnist
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()
digit=train_images[5]
import matplotlib.pyplot as plt 
plt.imshow(train_images[4],cmap=plt.cm.binary)
plt.imshow(digit,cmap=plt.cm.binary)
plt.show()