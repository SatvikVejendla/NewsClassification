from config.model import show_details

def neatify(history, results):
    (loss, acc) = results

    res = {
        "test": {
            "loss": loss,
            "accuracy": acc
        },
        "train": {
            "loss": history["loss"][0 if show_details==1 else 0:show_details],
            "val_accuracy": history["val_accuracy"][0 if show_details==1 else 0:show_details],
        }
    }
    return res