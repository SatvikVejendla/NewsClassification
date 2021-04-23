from keras.datasets import reuters
from tensorflow import keras
import sys
import re
import os
import json

from pyUtils.newModel import Model
from pyUtils.neatify import neatify
from model.save import saveModel
from config.model import input_dim
from train.parse import parseData
from constants.categories import categories
from train.seq import encode_sequences



arg = sys.argv

x = 0
if(len(arg) > 1):
    arg = arg[1]
    reg = "--?r(|e|etrain)"
    x = re.search(reg, arg)

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=input_dim, test_split=0.1)

def encode(text):
    return ([word_index.get(i, 0) for i in list(text)])


word_index = reuters.get_word_index()


(xs, ys), (val_xs, val_ys), (test_xs, test_ys) = parseData((train_data, train_labels), (test_data, test_labels))

history = None
results = None

if(x != 0):

    model = Model(xs, ys, (val_xs, val_ys))

    r = model.evaluate(test_xs, test_ys)


    history = model.history.history
    results = r


else:

    model = keras.models.load_model("model/state/model.h5")
    
    res = model.evaluate(test_xs, test_ys)

    f = open(os.path.join(os.path.dirname("main.py"), "./model/state/results.json"), "r")
    hist = f.read()


    history = json.loads(hist)['train']
    results = res


res = neatify(history, results)
print(json.dumps(res, indent=4, sort_keys=True))

saveModel(model._model, res) if x != 0 else None