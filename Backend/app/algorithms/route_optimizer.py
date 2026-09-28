from itertools import permutations


def calculate_route_distance(start, route, distances):
    """
    Calculate total distance for a route.

    start     = Restaurant
    route     = order of customers
    distances = distance between locations
    """

    total_distance = 0
    current_location = start

    for customer in route:

        total_distance += distances[
            (current_location, customer)
        ]

        current_location = customer

    return total_distance


def optimize_route(restaurant, customers, distances):
    """
    Find the route with minimum total distance.

    Maximum customers in one batch = 3.
    """

    # Maximum 3 customers per driver
    if len(customers) > 3:
        raise ValueError(
            "A driver can have a maximum of 3 customers."
        )

    best_route = None
    shortest_distance = float("inf")

    # Generate all possible customer sequences
    possible_routes = permutations(customers)

    for route in possible_routes:

        distance = calculate_route_distance(
            restaurant,
            route,
            distances
        )

        # Select shortest route
        if distance < shortest_distance:

            shortest_distance = distance
            best_route = route

    return best_route, shortest_distance


# --------------------------------------------------
# TEST DATA
# --------------------------------------------------

restaurant = "Restaurant"

customers = [
    "Customer_A",
    "Customer_B",
    "Customer_C"
]


# Distance between locations
#
# In your final project, these distances can come
# from Dijkstra's shortest-path calculation.

distances = {

    ("Restaurant", "Customer_A"): 4,
    ("Restaurant", "Customer_B"): 7,
    ("Restaurant", "Customer_C"): 5,

    ("Customer_A", "Customer_B"): 2,
    ("Customer_A", "Customer_C"): 3,

    ("Customer_B", "Customer_A"): 2,
    ("Customer_B", "Customer_C"): 4,

    ("Customer_C", "Customer_A"): 3,
    ("Customer_C", "Customer_B"): 4
}


# --------------------------------------------------
# RUN ROUTE OPTIMIZATION
# --------------------------------------------------

best_route, shortest_distance = optimize_route(
    restaurant,
    customers,
    distances
)


# --------------------------------------------------
# DISPLAY RESULT
# --------------------------------------------------

print("===================================")
print("       ROUTE OPTIMIZATION")
print("===================================")

print("Starting Point :", restaurant)

print("Customers      :")
for customer in customers:
    print("                 ", customer)

print("-----------------------------------")

print("Optimized Route:")

print(restaurant, end="")

for customer in best_route:
    print(" ->", customer, end="")

print()

print("-----------------------------------")

print("Total Distance :", shortest_distance, "km")

print("===================================")