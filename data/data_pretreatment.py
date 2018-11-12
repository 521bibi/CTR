data = open('ad_demo.txt', 'rb')

train = open('train.csv', 'wb')
test = open('test.csv', 'wb')

count = 0
train_sets_rate = 0.8

for i in data.readlines():
    count += 1
print ("total lines: {}".format(count))

data.seek(0)

for key, line in enumerate(data.readlines()):
    if key <= count * train_sets_rate:
        train.write(line)
    else:
        test.write(line)

print ("train sets: {},test sets: {}".format(count * train_sets_rate, count * (1 - train_sets_rate)))
