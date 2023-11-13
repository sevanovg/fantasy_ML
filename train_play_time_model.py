import play_time_data_loader
import tqdm
import torch
from model_play_time import LinearRegression
from model_non_linear import NonLinear

def train():
    data_loaders = play_time_data_loader.Data_Loaders()

    train_loader = data_loaders.train_loader
    test_loader = data_loaders.test_loader

    # model = LinearRegression(3, 1)
    # optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    # criterion = torch.nn.MSELoss()

    model_lin = LinearRegression(4, 1)
    model_non_lin = NonLinear(4, 100, 1)
    optimizer_lin = torch.optim.Adam(model_lin.parameters(), lr=0.001)
    optimizer_non_lin = torch.optim.Adam(model_non_lin.parameters(), lr=0.001)
    criterion = torch.nn.MSELoss()

    num_epochs = 100
    losses = []

    for epoch in tqdm.tqdm(range(num_epochs), desc="Training"):
        # model.train()
        model_lin.train()
        model_non_lin.train()
        train_loss_lin = 0
        train_loss_non_lin = 0

        for idx, sample in enumerate(train_loader):
            target_output = sample['output']

            optimizer_lin.zero_grad()
            output_lin = model_lin(sample['input'])
            loss_lin = criterion(output_lin, target_output.unsqueeze(1))
            train_loss_lin += loss_lin.item()
            loss_lin.backward()
            optimizer_lin.step()

            optimizer_non_lin.zero_grad()
            output_non_lin = model_non_lin(sample['input'])
            loss_non_lin = criterion(output_non_lin, target_output.unsqueeze(1))
            train_loss_non_lin += loss_non_lin.item()
            loss_non_lin.backward()
            optimizer_non_lin.step()
        
        train_loss_lin = train_loss_lin/len(train_loader)
        train_loss_non_lin = train_loss_non_lin/len(train_loader)
        test_loss_lin = model_lin.evaluate(model_lin, test_loader, criterion)
        test_loss_non_lin = model_non_lin.evaluate(model_non_lin, test_loader, criterion)

        print('\ntrain_loss_lin after epoch', epoch, "is", train_loss_lin)
        print('train_loss_non_lin after epoch', epoch, "is", train_loss_non_lin)
        print('test_loss_lin after epoch', epoch, "is", test_loss_lin)
        print('test_loss_non_lin after epoch', epoch, "is", test_loss_non_lin)

if __name__ == "__main__":
    train()
        



