# Typically in a cross-border payment, we first provide the customer with an estimation or quote of the FX rate, which the customer follows up optionally with a payment execution request, should the quote be acceptable.  Because we utilize a FX exchange to execute the payment, the quote must be based on the orders present in the exchange.

# In this exercise, we will be writing a quote function for purchasing XRP with USD.

# A limit order has two components –  a limit price in USD and a quantity to sell in XRP.   Given list of these sell orders, create a function that calculates the amount of XRP you can purchase with a given amount of USD.

# double calculateXrpQuote(LimitOrders[] orders, double usdAmount);

# sellOrders = [
#      LimitOrder(0.25, 10.00),  // price (USD), quantity (XRP)
#      LimitOrder(0.50, 20.00),
#      LimitOrder(0.75, 5.00),
# ];

# Note the Following Requirements:

# The function should raise an error or an exception if there is insufficient XRP for sale for the USD amount provided.
# The function should not accept zero or negative amounts.
# The list of sell orders is pre-sorted in terms of desirability -- lower priced orders appear before higher priced orders.
# You may purchase all or a portion of the XRP for sale in a given order.
# You must purchase all of the XRP for a given order before moving on to the next.


# Additional test cases:

# calculateXrpQuote(sellOrders, -1.0);   // error
# calculateXrpQuote(sellOrders, 0.0);    // error
# calculateXrpQuote(sellOrders, 1.25);  // 5.0
# calculateXrpQuote(sellOrders, 0.625);  // 2.5
# calculateXrpQuote(sellOrders, 2.5);    // 10.0
# calculateXrpQuote(sellOrders, 5.0);    // 15.0 ====> 2.5 => 10 ==== 2.5===5 ==> 10 + 5 ==> 15
# calculateXrpQuote(sellOrders, 500.0);  // error


def calculateXrpQuote(LimitOrders, usdAmount):
    if usdAmount <= 0:
        return None
    total_amount = 0

    for items in LimitOrders:
        total_amount += items[0] * items[1]
    if usdAmount > total_amount:
        return None
    xrp_count = 0
    temp_total = 0
    for orders in LimitOrders:

        temp_count = usdAmount / orders[0]
        if temp_count > orders[1]:
            xrp_count += orders[1]
            usdAmount = usdAmount - (xrp_count * orders[0])
        else:
            if usdAmount > 0:
                xrp_count += usdAmount / orders[0]
                usdAmount = usdAmount - (xrp_count * orders[0])

    return xrp_count


orders = [
    [0.25, 10.00],
    [0.50, 20.00],
    [0.75, 5.00],
]

print(calculateXrpQuote(orders, -1))
print(calculateXrpQuote(orders, 0))
print(calculateXrpQuote(orders, 0.625))  # 2.5
print(calculateXrpQuote(orders, 1.25))
print(calculateXrpQuote(orders, 2.5))
print(calculateXrpQuote(orders, 5.0))  # 15
print(calculateXrpQuote(orders, 500))