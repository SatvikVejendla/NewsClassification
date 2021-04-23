from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from config.model import epochs, batch_size, verbose, loss, learning_rate

class Model:
    def __init__(self, xs, ys, val_data):
        self.create()
        self.train(xs, ys, val_data)

    def create(self):
        model = Sequential()
        model.add(Dense(64, activation='relu'))
        model.add(Dense(46, activation='softmax'))
        self._model = model
        self.compile()

    def compile(self):
        self._model.compile(optimizer=Adam(learning_rate=learning_rate),
              loss=loss,
              metrics=['accuracy'])

    def evaluate(self, xs, ys):
        return self._model.evaluate(xs, ys)

    def predict(self, xs):
        return self._model.predict(xs)

    def train(self, xs, ys, val_data):
        
        self.history = self._model.fit(xs, ys,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=val_data,
            verbose=verbose)
        
