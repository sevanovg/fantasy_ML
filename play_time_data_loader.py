import torch.utils.data.dataset as dataset
import torch.utils.data as data
import numpy as np

class EPL_Dataset(dataset.Dataset):
    def __init__(self):
        file = open('minutes_learning.csv', 'r', encoding="utf8")
        # self.data = np.genfromtxt('minutes_learning.csv', delimiter=',')
        self.data = np.genfromtxt(file, delimiter=',')
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        # input = self.data[idx][2:5].astype('float32') #prev, avg, med
        # input = self.data[idx][2:4].astype('float32')  #prev, avg
        # input = self.data[idx][3:5].astype('float32')  #avg, med
        input = self.data[idx][2:6].astype('float32') #previous 4 games
        output = self.data[idx][-1].astype('float32')
        dic = {'input': input, 'output': output}
        return dic

class Data_Loaders():
    def __init__(self):
        self.data = EPL_Dataset()
        test_size = round(len(self.data) * 0.2)
        indices = np.arange(len(self.data))
        np.random.shuffle(indices)

        test_set = data.Subset(self.data, indices[:test_size])
        train_set = data.Subset(self.data, indices[test_size:])

        self.test_loader = data.DataLoader(test_set, batch_size=1, shuffle=True)
        self.train_loader = data.DataLoader(train_set, batch_size=1, shuffle=True)

        

    