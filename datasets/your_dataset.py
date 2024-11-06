from pathlib import Path

import numpy as np
import torch
from torch.utils.data import TensorDataset

import utils
from datasets.core import TrajectoryDataset


class YourTrajectoryDataset(TensorDataset, TrajectoryDataset):
    def __init__(self, data_directory):
        data_directory = Path(data_directory)

    def get_seq_length(self, idx):
        raise NotImplementedError

    def get_frames(self, idx, frames):
        raise NotImplementedError
        # return obs / 255.0, actions, masks

    def __getitem__(self, idx):
        T = self.get_seq_length(idx)
        return self.get_frames(idx, range(T))
