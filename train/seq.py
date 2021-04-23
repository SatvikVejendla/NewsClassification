import numpy as np

from config.model import input_dim

def encode_sequences(sequences):
    output = np.zeros((len(sequences), input_dim))
    for i, sequence in enumerate(sequences):
        output[i, sequence] = 1.
    return output