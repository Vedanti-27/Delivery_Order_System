# Order Assignment Service
# Delivery Order Assignment System

from queue import Queue
from datetime import datetime


# Waiting orders
waiting_queue = Queue()


def assign_order(order, drivers):
    """
    Assign an order to the best available driver.

    Project conditions:
    1. One order cannot be assigned twice.
    2. Driver must be AVAILABLE.
    3. Driver can have maximum 3 orders.
    4. Driver should be within 5 km.
    5. Prefer same area/road.
    6. If no driver is available, order goes to queue.
    """

    # ---------------------------------------------
    # CONDITION 1: Check duplicate assignment
    # ---------------------------------------------

    if order["status"] == "ASSIGNED":
        return {
            "success": False,
            "message": "Order is already assigned."
        }

    # ---------------------------------------------
    # Find suitable drivers
    # ---------------------------------------------

    suitable_drivers = []

    for driver in drivers:

        # CONDITION 2:
        # Driver must be available

        if driver["status"] != "AVAILABLE":
            continue

        # CONDITION 3:
        # Maximum 3 orders per driver

        if len(driver["current_orders"]) >= 3:
            continue

        # CONDITION 4:
        # Driver must be within 5 km

        if driver["distance"] > 5:
            continue

        suitable_drivers.append(driver)

    # ---------------------------------------------
    # No driver available
    # ---------------------------------------------

    if not suitable_drivers:

        order["status"] = "WAITING"

        waiting_queue.put(order)

        return {
            "success": False,
            "message": "No driver available. Order added to waiting queue.",
            "order_id": order["order_id"]
        }

    # ---------------------------------------------
    # GREEDY DRIVER SELECTION
    # ---------------------------------------------

    best_driver = None
    best_score = float("inf")

    for driver in suitable_drivers:

        # Prefer same area/road

        if driver["area"].lower() == order["area"].lower():
            area_penalty = 0
        else:
            area_penalty = 100

        # Greedy score

        score = driver["distance"] + area_penalty

        if score < best_score:

            best_score = score
            best_driver = driver

    # ---------------------------------------------
    # ASSIGN ORDER
    # ---------------------------------------------

    best_driver["current_orders"].append(
        order["order_id"]
    )

    # Change driver status

    best_driver["status"] = "BUSY"

    # Change order status

    order["status"] = "ASSIGNED"

    # Store assignment information

    assignment = {

        "order_id": order["order_id"],

        "driver_id": best_driver["driver_id"],

        "assigned_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "status": "ASSIGNED"
    }

    return {

        "success": True,

        "message": "Order assigned successfully.",

        "assignment": assignment
    }


# ==================================================
# TEST DATA
# ==================================================

if __name__ == "__main__":

    # ---------------------------------------------
    # Order
    # ---------------------------------------------

    order = {

        "order_id": 101,

        "customer_id": 25,

        "area": "FC Road",

        "status": "NEW"
    }


    # ---------------------------------------------
    # Drivers
    # ---------------------------------------------

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

            "distance": 3.5,

            "current_orders": []
        },

        {
            "driver_id": 3,

            "name": "Driver 3",

            "status": "BUSY",

            "area": "FC Road",

            "distance": 1.5,

            "current_orders": [
                90,
                91
            ]
        },

        {
            "driver_id": 4,

            "name": "Driver 4",

            "status": "AVAILABLE",

            "area": "FC Road",

            "distance": 6.0,

            "current_orders": []
        }
    ]


    # ---------------------------------------------
    # ASSIGN ORDER
    # ---------------------------------------------

    result = assign_order(
        order,
        drivers
    )


    # ---------------------------------------------
    # DISPLAY RESULT
    # ---------------------------------------------

    print()
    print("====================================")
    print("       ORDER ASSIGNMENT")
    print("====================================")

    print("Order ID :", order["order_id"])

    print("Status   :", order["status"])

    print("------------------------------------")

    if result["success"]:

        assignment = result["assignment"]

        print("Message  :", result["message"])

        print(
            "Driver ID:",
            assignment["driver_id"]
        )

        print(
            "Assigned:",
            assignment["assigned_at"]
        )

    else:

        print("Message :", result["message"])

    print("====================================")