def select_best_driver(order, drivers):

    best_driver = None
    best_score = float("inf")

    for driver in drivers:

        # 1. Driver must be available
        if driver["status"] != "AVAILABLE":
            continue

        # 2. Maximum 3 orders per driver
        if len(driver["current_orders"]) >= 3:
            continue

        # 3. Driver must be within 5 km
        if driver["distance"] > 5:
            continue

        # 4. Same area gets priority
        if driver["area"].lower() == order["area"].lower():
            area_penalty = 0
        else:
            area_penalty = 100

        # 5. Greedy score
        score = driver["distance"] + area_penalty

        # Select the driver with minimum score
        if score < best_score:
            best_score = score
            best_driver = driver

    return best_driver



order = {
    "order_id": 101,
    "area": "FC Road"
}


drivers = [

    {
        "driver_id": 1,
        "name": "Driver 1",
        "status": "AVAILABLE",
        "area": "FC Road",
        "distance": 2.5,
        "current_orders": []
    },

    {
        "driver_id": 2,
        "name": "Driver 2",
        "status": "AVAILABLE",
        "area": "JM Road",
        "distance": 1.5,
        "current_orders": []
    },

    {
        "driver_id": 3,
        "name": "Driver 3",
        "status": "BUSY",
        "area": "FC Road",
        "distance": 1.0,
        "current_orders": []
    },

    {
        "driver_id": 4,
        "name": "Driver 4",
        "status": "AVAILABLE",
        "area": "FC Road",
        "distance": 4.0,
        "current_orders": [
            90,
            91,
            92
        ]
    }
]




selected_driver = select_best_driver(order, drivers)



if selected_driver:

    print("===================================")
    print(" GREEDY DRIVER ASSIGNMENT")
    print("===================================")

    print("Order ID       :", order["order_id"])
    print("Order Area     :", order["area"])

    print("Selected Driver:",
          selected_driver["name"])

    print("Driver ID      :",
          selected_driver["driver_id"])

    print("Driver Area    :",
          selected_driver["area"])

    print("Distance       :",
          selected_driver["distance"], "km")

    print("Current Orders :",
          len(selected_driver["current_orders"]))

    print("Status         :",
          selected_driver["status"])

    print("===================================")

else:

    print("===================================")
    print(" NO DRIVER AVAILABLE")
    print("Order has been placed in waiting queue.")
    print("===================================")