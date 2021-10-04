import sys

# destination, time = input().split(" ")
destination, time = "Richmond 09:15".split(" ")

user_hours, user_minutes = time.split(":")
user_current_time = int(user_hours) * 60 + int(user_minutes)
sheduleFile = open("./schedule.txt", "r").read()

schedule_array = []


for line in sheduleFile.split("\n"):
    line = line.split(" ")
    schedule_array.append([line[0], line[-1]])

amount_of_town = 0
string_minimal_time = ""
minutes_before = 0

time_array = sorted([(int(i[-1].split(":")[0]) * 60 + int(i[-1].split(":")[-1])) for i in schedule_array])

print(user_current_time)
print(time_array)

for array in schedule_array:
    if array[0] == destination:
        amount_of_town += 1

    for i in time_array:
        if (i > user_current_time and string_minimal_time == ""):
            string_minimal_time = str(i // 60) + ":" + str(i - (i // 60) * 60)
            if ()
    # hours, minutes = array[-1].split(":")
    # current_schedule_minutes = int(hours) * 60 + int(minutes)
    # if (current_schedule_minutes >= user_current_time and maximal_time < current_schedule_minutes):
    #     maximal_time = int(hours) * 60 + int(minutes)
    #     string_minimal_time = hours + ":" + minutes
    #     minutes_before = int(user_hours) + int(user_minutes)

# for  in schedule_array:

    
    

print(amount_of_town, string_minimal_time)
# print(amount_of_town)