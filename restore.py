import numpy as np
import matplotlib.pyplot as plt

# restore=np.zeros([60,900,400])

# Restoring condition for control experiment
# for k in range(0,60,1):
#     for j in range(0,600,1):
#         for i in range(0,400,1):
#             if i < 40:
#                  restore[k,j,i] = 1.0 *(40-i)/20
#             else:
#                 if i > 360:
#                     restore[k,j,i] = 1.0 *(i-360)/20
#             if restore[k,j,i] > 1.0:
#                 restore[k,j,i] = 1.0
# restore.astype(">f8").tofile("restore_control")

restore=np.zeros([60,900,520])

# Restoring condition for the longriver experiment
for k in range(0,60,1):
    for j in range(0,180,1):
        for i in range(0,400,1):
            restore[k,j,i]=1
for k in range(0,60,1):
    for j in range(180,200,1):
        for i in range(0,400,1):
            if restore[k,j,i] < 1.0*(200-j)/20:
                restore[k,j,i] = 1.0*(200-j)/20
        
# restore.astype(">f8").tofile("restore_longriver")
