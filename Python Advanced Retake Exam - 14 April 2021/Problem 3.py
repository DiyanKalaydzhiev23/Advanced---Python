def flights(*info):
    info = list(info)
    flights_dict = {}

    for _ in range(len(info)):
        destination = info.pop(0)

        if destination != "Finish":
            passengers = int(info.pop(0))
            if destination in flights_dict:
                flights_dict[destination] += passengers
            else:
                flights_dict[destination] = passengers
        else:
            break

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
