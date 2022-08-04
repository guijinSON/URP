import torch 
import numpy as np
from torch.utils.data import Dataset, DataLoader

class StockDataset(Dataset):
    def __init__(self,OPEN,HIGH,LOW,CLOSE,VOLUME,span=40, target=4):
        self.OPEN   = OPEN
        self.HIGH   = HIGH
        self.LOW    = LOW
        self.CLOSE  = CLOSE
        self.VOLUME = VOLUME
        self.span   = span
        self.target = target

    def __len__(self):
        return len(self.OPEN-self.span-self.target)

    def __getitem__(self, idx):
        o = self.OPEN[idx : idx + self.span]
        h = self.HIGH[idx : idx + self.span]
        l = self.LOW[idx  : idx + self.span]
        c = self.CLOSE[idx  : idx + self.span]
        v = self.VOLUME[idx : idx + self.span]
        
        bb1, bb2, bb3, mp, var, cr, bop, adx = self.get_factors()
        
        bb1_s = bb1[idx : idx + self.span]
        bb2_s = bb2[idx : idx + self.span]
        bb3_s = bb3[idx : idx + self.span]
        mp_s  = mp[idx  : idx + self.span]
        var_s = var[idx : idx + self.span]
        cr_s  = cr[idx  : idx + self.span]
        bop_s = bop[idx : idx + self.span]
        adx_s = adx[idx : idx + self.span]
        
        target_1 = c[-1]
        target_2 = self.CLOSE[idx + self.span + self.target]
        
        target = self.targetVal_to_category((target_2-target_1)/target_1 * 100)
        
        return {'f1': o, 
                'f2': h, 
                'f3': l, 
                'f4': c, 
                'f5': v, 
                'f6': bb1_s, 
                'f7': bb2_s, 
                'f8': bb3_s, 
                'f9': mp_s, 
                'f10': var_s, 
                'f11': cr_s, 
                'f12': bop_s, 
                'f13': adx_s,
                'target':target}
    
    def get_factors(self):
        bb1, bb2, bb3 = talib.BBANDS(self.CLOSE, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
        
        bb1 = self.ffill(bb1)
        bb2 = self.ffill(bb2)
        bb3 = self.ffill(bb3)

        mp            = self.ffill(talib.MIDPRICE(self.HIGH, self.LOW, timeperiod=5))
        var           = self.ffill(talib.VAR(self.CLOSE, timeperiod=5, nbdev=1))
        cr            = self.ffill(talib.CORREL(self.HIGH, self.CLOSE, timeperiod=5))
        bop           = self.ffill(talib.BOP(self.OPEN, self.HIGH, self.LOW, self.CLOSE))
        adx           = self.ffill(talib.ADX(self.HIGH, self.LOW, self.CLOSE, timeperiod=5))
        
        return bb1, bb2, bb3, mp, var, cr, bop, adx
    
    def ffill(self, arr):
        idx = np.isnan(arr).sum() 
        arr[:idx] = arr[idx+1]
        return arr

    def targetVal_to_category(self,target):
        if target < -2.5: target = 0
        elif -2.5 <= target < 0: target = 1
        elif 0 <= target < 2.5: target = 2
        elif 2.5 <= target: target = 3
        return target
        
def get_dataloader(data, batch_size = 256, shuffle=True, drop_last=True):
    return DataLoader(data, batch_size = batch_size, shuffle = shuffle, drop_last = drop_last)
