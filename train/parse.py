from keras.utils.np_utils import to_categorical


from train.seq import encode_sequences
from train.val import getValData

def parseData(train, test):

    (train_data, train_labels) = train
    (test_data, test_labels) = test

    
    train_ys = to_categorical(train_labels)
    test_ys = to_categorical(test_labels)


    train_xs = encode_sequences(train_data)
    test_xs = encode_sequences(test_data)
    

    (train_xs, train_ys), (val_xs, val_ys) = getValData(train_xs, train_ys, 0.1)

    return (train_xs, train_ys), (val_xs, val_ys), (test_xs, test_ys)

