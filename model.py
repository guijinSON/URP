import torch
import torch.nn as nn 

class MLP_Block(nn.Module):
    def __init__(self,d_ffn,seq_len): # d_ffn (deep_feed forward network), seq_len (time_series)
        super(MLP_Block,self).__init__()

        self.MLP_LAYER_1 = nn.Sequential(nn.Linear(seq_len,10),nn.GELU(),
                                         nn.Linear(10,seq_len),nn.GELU())
        self.MLP_LAYER_2 = nn.Sequential(nn.Linear(d_ffn,20),nn.GELU(),
                                         nn.Linear(20,d_ffn),nn.GELU())
        
    def forward(self,x):
        residual = x.clone()
        x2 = self.MLP_LAYER_1(x)
        x3 = torch.permute(x2,(0,2,1))
        x4 = self.MLP_LAYER_2(x3)
        output = torch.permute(x4,(0,2,1)) + residual

        return output

class MLP_TS(nn.Module):
    def __init__(self,d_ffn,seq_len,num_layers):
        super(MLP_TS,self).__init__()
        self.model = nn.Sequential(*[MLP_Block(d_ffn,seq_len) for _ in range(num_layers)])

    def forward(self,x):
        x = self.model(x)
        return x
    
class MLP_TS_with_Head(nn.Module):
    def __init__(self,d_ffn,seq_len,num_layers):
        super(MLP_TS_with_Head,self).__init__()
        self.model = nn.Sequential(*[MLP_Block(d_ffn,seq_len) for _ in range(num_layers)])

        #self.p_enc_1d_model_sum = Summer(PositionalEncoding1D(seq_len))

        self.MLP_LAYER_1 = nn.Linear(seq_len,1)
        self.MLP_LAYER_2 = nn.Linear(d_ffn,4)

    def forward(self,x):
        x = self.p_enc_1d_model_sum(x)
        x = self.model(x)
        x2 = self.MLP_LAYER_1(x)
        x3 = torch.permute(x2,(0,2,1))
        x4 = self.MLP_LAYER_2(x3)
        
        return x4
