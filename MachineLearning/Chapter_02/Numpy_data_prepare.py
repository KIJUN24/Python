import fish_data_list as fdl
import numpy as np

# print(np.column_stack(([1,2,3], [4,5,6])))

fish_data = np.column_stack((fdl.fish_length, fdl.fish_weight))
# print(fish_data[:5])
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
# print(fish_target)