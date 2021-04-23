from sklearn.model_selection import train_test_split


def getValData(train_xs, train_ys, val_split=0.1):
    
    xs, val_xs, ys, val_ys = train_test_split(train_xs, train_ys, test_size=val_split)

    return (xs, ys), (val_xs, val_ys)