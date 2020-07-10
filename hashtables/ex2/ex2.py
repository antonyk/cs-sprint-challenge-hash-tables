#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

    lookup = {}
    route = []
    # build the lookup
    for _, v in enumerate(tickets):
        lookup[v.source] = v.destination

    flight = lookup['NONE']
    while flight != 'NONE':
        route.append(flight)
        flight = lookup[flight]

    route.append('NONE')

    return route


if __name__ == "__main__":

    tickets = [
        Ticket("PIT", "ORD"),
        Ticket("XNA", "SAP"),
        Ticket("SFO", "BHM"),
        Ticket("FLG", "XNA"),
        Ticket("NONE", "LAX"),
        Ticket("LAX", "SFO"),
        Ticket("SAP", "SLC"),
        Ticket("ORD", "NONE"),
        Ticket("SLC", "PIT"),
        Ticket("BHM", "FLG")
    ]


    print(reconstruct_trip(tickets, 10))
