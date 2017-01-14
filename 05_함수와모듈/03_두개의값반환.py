def cal_upper_lower(price):
    offset = price * 0.3
    upper = price + offset
    lower = price - offset
    return (upper, lower)


(upper, lower) = cal_upper_lower(10000)

print(upper, lower)