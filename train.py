import torch
import wandb
import numpy as np
from collections import Counter
#from utils import log_output_distribution

def single_epoch_train(model, optimizer, trainloader, loss_func, epoch, batch_size, device, wb=True):
    running_loss = 0.0 
    
    model.train()
    for data in trainloader:
        
        X_batch= torch.stack(
                            [data['f1'],data['f2'],data['f3'],data['f4'],data['f5'],data['f6'],data['f7'],
                            data['f8'],data['f9'],data['f10'],data['f11'],data['f12'],data['f13']],
                            dim=1).float().to(device)

        target = data['target'].to(device)
        
        optimizer.zero_grad()
        output = model(X_batch).reshape(batch_size,4)

        loss = loss_func(output, target)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()

    acc = (torch.argmax(output,dim=1).detach().cpu() == target.detach().cpu()).sum()/batch_size
    d0,d1,d2,d3 = log_output_distribution(Counter(torch.argmax(output,dim=1).detach().cpu().tolist()))
    
    if wb:
        wandb.log({'Training Accuracy':acc, 'Class 0': d0, 'Class 1': d1, 'Class2': d2, 'Class 3':d3})
    else:
        print('[%d] Running Accuracy: %.2f' % (epoch + 1, acc)) 

def log_output_distribution(counter):
    try: dis_0  = counter[0]
    except: dis_0 = 0

    try: dis_1  = counter[1]
    except: dis_1 = 0

    try: dis_2  = counter[2]
    except: dis_2 = 0

    try: dis_3  = counter[3]
    except: dis_3 = 0

    return dis_0, dis_1, dis_2, dis_3
