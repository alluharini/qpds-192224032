import numpy as np
import pandas as pd
np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 5), columns=list("ABCDE"))
black_bg = '\033[40m'   
yellow_text = '\033[33m' 
reset = '\033[0m'   
for index, row in df.iterrows():
    formatted_row = [f"{black_bg}{yellow_text}{value:.5f}{reset}" for value in row]
    print(' | '.join(formatted_row))
