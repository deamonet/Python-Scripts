from numpy.random import rand
from numpy.random import shuffle

def gen_y(y):
    random_y = []
    random_y.append(y)
    for increase in rand(1,1000)[0,:]:
        y = y * (1 - 0.001*rand(1,1)[0,0] - 0.001) + increase
        random_y.append(y)
    
    data_y = [5] * 3
    data_y.extend(random_y[:-3])
    shuffle(data_y)
    return data_y

print(gen_y(10))