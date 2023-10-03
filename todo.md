    Consumer Service
    -> createConsumer()

    Order Service
        -> createOrder()
            Restaurant Service
            -> findAvailableRestaurants()
            Kitchen Service
            -> checkStock()
        -> orderStatusAccepted()
            Kitchen Service
            -> orderReadyForPickUp()
                Delivery Service
                -> noteUpdatedLocation()
                -> noteDeliveryPickedUp() 
                -> noteDeliveryDelivered()
        -> orderStatusDelivered()