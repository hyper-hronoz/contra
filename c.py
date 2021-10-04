sheduleFile = open("./schedule.txt", "r").read()

destination, time = "Richmond 09:15".split(" ")

schedule_array = []

current_user_time = int(time.split(":")[0]) * 60 + int(time.split(":")[-1])

amount_of_towns = 0
nearest_time = 0
minimal = 0
nearest_time_string = ""

time_array = []

for line in sheduleFile.split("\n"):
    line = line.split(" ")
    schedule_array.append([line[0], line[-1]])

for array in schedule_array:
    if (array[0] == destination):
        amount_of_towns += 1
        time_array.append( int(array[-1].split(":")[0]) * 60 + int(array[-1].split(":")[-1]) )

for time in sorted(time_array):
    if time >= current_user_time and nearest_time_string == "":
        nearest_time_string = str(time // 60) + ":" + str(time - (time // 60) * 60)
        minimal = time - current_user_time

print(amount_of_towns)
print(nearest_time_string)
print(minimal)
