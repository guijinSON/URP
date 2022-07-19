from torch.utils.data import Dataset, DataLoader
from factors import overlapStudies


class EquityDataset(Dataset):
    def __init__(self, data, ticker):
        self.open    = data[ticker].Open.values
        self.high    = data[ticker].High.values
        self.low     = data[ticker].Low.values
        self.close   = data[ticker].Close.values
        self.volume  = data[ticker].Volume.values

        self.ols = overlapStudies(self.open, self.high, self.low, self.close, self.volume)

    def __len__(self):
        return len(self.open)

    def __getitem__(self, idx):
        o = self.ols[idx]

        return o 

def get_dataloader(data, batch_size = 256, shuffle=True, drop_last=True):
    return DataLoader(data, batch_size = batch_size, shuffle = shuffle, drop_last = drop_last)
