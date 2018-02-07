import numpy as np

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop

np.random.seed(1337)  # for reproducibility

# Load train and test data from keras
# x shape(60000, 28, 28), y shape(10000, )
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Data preprocessing
# Normalize value to 0 ~ 1
x_train = x_train.reshape(-1, 28*28) / 255. 
x_test = x_test.reshape(-1, 28*28) / 255.
# Transform data to onehot format
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# Another way to build your neural net
model = Sequential([
    Dense(32, input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])

# Another way to define your optimizer
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

# We add metrics to get more results you want to see
# We only see 'accuracy' here
model.compile(optimizer=rmsprop,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training ------------')
# Another way to train the model
model.fit(x_train, y_train, epochs=2, batch_size=32)

print('\nTesting ------------')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(x_test, y_test)

print('test loss: ', loss)
print('test accuracy: ', accuracy)