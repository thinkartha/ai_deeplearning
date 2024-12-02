import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the MNIST dataset
# MNIST dataset is available in TensorFlow datasets, so we can load it directly.
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Step 2: Preprocess the data
# Normalize the pixel values to range [0, 1] by dividing by 255.0
x_train = x_train / 255.0
x_test = x_test / 255.0

# Step 3: Build the model
model = models.Sequential([
    # Flatten the 28x28 images into a 1D array of 784 pixels
    layers.Flatten(input_shape=(28, 28)),  
    
    # Add a fully connected (dense) layer with 128 neurons
    layers.Dense(128, activation='relu'),
    
    # Add a dropout layer for regularization (prevents overfitting)
    layers.Dropout(0.2),
    
    # Add the output layer with 10 neurons (one for each digit from 0 to 9)
    layers.Dense(10, activation='softmax')  # softmax is used for multi-class classification
])

# Step 4: Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Step 5: Train the model
model.fit(x_train, y_train, epochs=5)

# Step 6: Evaluate the model on the test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")

# Step 7: (Optional) Display some test images and predictions
# Predict the labels of the test images
predictions = model.predict(x_test)

# Plot the first 5 test images and their predictions
for i in range(5):
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    plt.title(f"Prediction: {np.argmax(predictions[i])}")
    plt.show()
