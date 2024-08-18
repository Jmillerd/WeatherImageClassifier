import tensorflow as tf


#Creates an ImageDataGenerator:
training_data_generator = tf.keras.preprocessing.image.ImageDataGenerator()



#Prints its attributes:
print(training_data_generator.__dict__)