import torch
mask = torch.zeros(shape)
bsize, _, mask_h, mask_w = mask.shape
print(bsize)