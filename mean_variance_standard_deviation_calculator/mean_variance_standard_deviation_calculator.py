import numpy as np

def calculate(list_of_nine):
      if len(list_of_nine) == 9:
        nplist = np.array(list_of_nine).reshape((3, 3))
        flattened = nplist.flatten()
        npdict = {"mean": [list(np.mean(nplist,axis=0)), list(np.mean(nplist,axis=1)), np.mean(flattened)], "variance": [list(np.var(nplist,axis=0)), list(np.var(nplist,axis=1)), np.var(flattened)], "standard deviation": [list(np.std(nplist,axis=0)), list(np.std(nplist,axis=1)), np.std(flattened)], "max": [list(np.max(nplist,axis=0)), list(np.max(nplist,axis=1)), np.max(flattened)], "min": [list(np.min(nplist,axis=0)), list(np.min(nplist,axis=1)), np.min(flattened)], "sum": [list(np.sum(nplist,axis=0)), list(np.sum(nplist,axis=1)), np.sum(flattened)]}
    
      else:
        raise ValueError("List must contain nine numbers.")
    
      return npdict