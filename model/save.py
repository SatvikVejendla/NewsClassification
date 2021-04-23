import os
import shutil
import json


def saveModel(model, results):
    old_model = os.path.join(os.path.dirname("main.py"), './model/state')
    shutil.rmtree(old_model)

    model.save(os.path.join(os.path.dirname("main.py"), './model/state/model.h5'))

    
    f = open(os.path.join(os.path.dirname("main.py"), "./model/state/results.json"), "w")

    json.dump(results, f)
    
    f.close()

    print("Model saved.")