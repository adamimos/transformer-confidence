import os
import pickle

class StorageManager:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)

    def save_output(self, idx, output, activations):
        with open(os.path.join(self.storage_path, f'output_{idx}.pkl'), 'wb') as f:
            pickle.dump({'output': output, 'activations': activations}, f)
