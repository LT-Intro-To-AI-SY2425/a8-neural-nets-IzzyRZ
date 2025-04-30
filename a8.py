from neural import *
# print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")
# nn = NeuralNet(2,8,1)

# training_data = [
#     ([1, 1], [0]), 
#     ([1, 0], [1]), 
#     ([0, 1], [1]), 
#     ([0, 0], [0])
#     ]

# nn.train(training_data)
# print(nn.test_with_expected(training_data))

partyNet = NeuralNet(5,16,1)

party_training = [
    ([0.9,0.6,0.8,0.3,0.1],[1]),
    ([0.8,0.8,0.4,0.6,0.4],[1]),
    ([0.7,0.2,0.4,0.6,0.3],[1]),
    ([0.5,0.5,0.8,0.4,0.8],[0]),
    ([0.3,0.1,0.6,0.8,0.8],[0]),
    ([0.6,0.3,0.4,0.3,0.6],[0])
]

party_testing = [
    ([1,1,1,0.1,0.1]),
    ([0.5,0.2,0.1,0.7,0.7]),
    ([0.8,0.3,0.3,0.3,0.8]),
    ([0.8,0.3,0.3,0.8,0.3]),
    ([0.9,0.8,0.8,0.3,0.6])
]

partyNet.train(party_training)
print(partyNet.test(party_testing))
    