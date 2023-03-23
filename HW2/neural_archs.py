import torch


# NOTE: In addition to __init__() and forward(), feel free to add
# other functions or attributes you might need.
class DAN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        # Done: Declare DAN architecture
        super(DAN, self).__init__()
        self.layer1 = torch.nn.Linear(input_size, hidden_size)
        self.layer2 = torch.nn.Linear(hidden_size, hidden_size//2)
        self.layer3 = torch.nn.Linear(hidden_size//2, output_size)
        self.relu = torch.nn.LeakyReLU()

    def forward(self, x):
        # Done: Implement DAN forward pass
        # print(x.shape)
        x = torch.mean(x, dim=1)
        # print(x.shape)
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        x = self.layer3(x)
        return x


class RNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1, bidirectional=False):
        # Done: Declare RNN model architecture
        super(RNN, self).__init__()
        self.rnn = torch.nn.RNN(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional)
        self.layer_fc = torch.nn.Linear(hidden_size * (2 if bidirectional else 1), output_size)

    def forward(self, x):
        # TODO: Implement RNN forward pass
        x, _ = self.rnn(x)
        # print(x.shape)
        x = x[:, -1, :]
        # print(x.shape)
        x = self.layer_fc(x)
        # print(x.shape)
        return x


class LSTM(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1, bidirectional=False):
        # Done: Declare LSTM model architecture
        super(LSTM, self).__init__()
        self.lstm = torch.nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional)
        self.layer_fc = torch.nn.Linear(hidden_size * (2 if bidirectional else 1), output_size)


    def forward(self, x):
        # Done: Implement LSTM forward pass
        _, (h_n, _) = self.lstm(x)
        x = h_n[-1, :, :]
        if self.lstm.bidirectional:
            x = torch.cat(
                (h_n[-2, :, :], h_n[-1, :, :]),
                dim=-1
            )
        else:
            x = h_n[-1, :, :]
        x = self.layer_fc(x)
        return x