# NewsClassification
A simple Tensorflow news classification AI based on the Reuters dataset


## Model structure
- Epochs: 25
- Batch Size: 512
- Input Dim: 10000
- Learning Rate: 0.0015
- Loss: Categorical Cross Entropy
- Optimizer: Adam
- Layer 1: 64 nodes with "relu" activation function
- Layer 2: 46 output nodes with "softmax" activation function





## Get Started

To use this project yourself, clone this repo and type this command in the root terminal of your project directory.

```
py -m pip install requirements.txt
```

**To run this code, you can use one of 2 possible terminal inputs.*

To run the model without retraining, type this:

```
py main.py
```

To retrain the model and run, type this:

```
py main.py -r
```

The system arguments for retraining the model can be "-r", "--r", "--re", "-re", "-retrain", "--retrain". All of these would yield the same result.
