from keras.datasets import mnist
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()
import matplotlib.pyplot as plt
for a in range(28):
    for i in range(28):  
        digit=train_images[i]
        plt.imshow(digit,cmap=plt.cm.binary)
        plt.show()