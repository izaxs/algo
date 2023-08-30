# You are given an array of orders like this:

# [["Buy", 20, "AAPL", "$10"], ["Sell", 19, "AAPL", "$9"], ...]

# Assume there is no sales commission and they are in chronological order. If a buy order is placed and there are sell orders, then fill the buy order using the sell orders based on price from lowest to highest.
# If a sell order is placed and there are buy orders, then fill the sell order using the buy orders based on price from highest to lowest.

# Return the total profit that will go to sellers using these rules.

# Follow up:
# The rules have changed. Now when buy order comes, you fill it using the earliest remaining sell order whose price is <= buy order price. For sell orders, you fill them using the earliest remaining buy orders whose price is >= the sell order price.