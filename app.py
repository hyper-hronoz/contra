travel_file = open("./travel.txt", mode="r").read()
wishes_file = open("./wishes.txt", mode="r").read()

answer = []

train_to_destination_dict = {
    
}

# creating dict of key value 
for train_destination in travel_file.split("\n"):
    train_destination = train_destination.split(" ")
    train_to_destination_dict[train_destination[0]] = train_destination[1:-1]

# get all notaml data

for wish in wishes_file.split("\n"):
    for key in train_to_destination_dict.keys():
        if (wish in train_to_destination_dict[key]):
            answer.append(key)

    
for i in answer:
    print(i)

# print(train_to_destination_dict)

# print(travel_file, wishes_file)