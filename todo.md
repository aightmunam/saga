Order Service
-> createOrder()
    Consumer Service
    -> validateCustomer()
    Restaurant Service
    -> confirmOpenRestaurant()
    Kitchen Service
    -> confirmStock()
Order Service
-> orderStatusAccepted()
    Kitchen Service
    -> preparingFood()
Order Service
-> orderStatusPreparing()

Kitchen Service
-> foodReadyForPickup()

Order Service
-> orderStatusReady()