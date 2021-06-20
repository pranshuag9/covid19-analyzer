from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D,Activation,MaxPooling2D
from keras.layers import Concatenate
from keras import Input
from keras.models import Model, Sequential

def get_model(input_shape):
    inp = Input(shape=input_shape)
    convs = []
    parrallel_kernels = [3, 5, 7]

    # Building the first layer of architecture
    for kernel_size in parrallel_kernels:
        conv = Conv2D(
            filters=128,
            kernel_size=kernel_size,
            padding='same',
            activation='relu',
            input_shape=input_shape,
            strides=1
        )(inp)
        convs.append(conv)

    out = Concatenate()(convs)
    conv_model = Model(inputs=inp, outputs=out)

    model = Sequential()
    model.add(layer=conv_model)

    model.add(Conv2D(filters=64, kernel_size=(3, 3)))
    model.add(Activation(activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=32, kernel_size=(3, 3)))
    model.add(Activation(activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=128, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=2, input_dim=128, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    return model