from torch.nn.functional import mse_loss
import torch.nn.functional as func
def completion_network_loss(input, output, mask):
    #return func.cross_entropy(output * mask, input * mask)
    return mse_loss(output * mask, input * mask)
