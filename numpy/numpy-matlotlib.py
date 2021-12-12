import numpy as np
import matplotlib.pyplot as matplot
maaslist=np.random.normal(4000,500,1000)
print(np.mean(maaslist))
matplot.hist(maaslist,30)
matplot.show()