import numpy as np

vocabs = np.load("vocab.npy",allow_pickle=True).item()
print(vocabs.keys())
print(vocabs['s'])