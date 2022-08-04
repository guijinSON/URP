import torch
import numpy as np

def single_epoch_train(model, optimizer, trainloader, loss_func, epoch, batch_size, device):
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

    print('[%d] loss: %.6f' % (epoch + 1, running_loss))   
