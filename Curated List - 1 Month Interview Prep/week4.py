# def fibGen(): 
#     a, b = 0, 1 
#     while True: 
#         yield a 
#         a, b = b, b + a 

# # fib = fibGen() 
# # for i in range(30): 
# #     print(next(fib), end=" ")

# def extract(fname): 
#     with open(fname, "r") as f:
#         for line in f: 
#             yield line 

# def count_rows(): 
#     count = 0 
#     for row in extract("C:\\Users\\samee\\Desktop\\py-projects\\Stock_Data.csv"): 
#         count += 1
#     return count 

# # print(f"Total rows in file: {count_rows()}")

# # reader = extract("C:\\Users\\samee\\Desktop\\py-projects\\Stock_Data.csv")

# # print(next(reader))
# # print(next(reader))
# # print(next(reader))


# import logging 

# logging.basicConfig(filename="logs.log", 
#                     format="%(asctime)s %(message)s",
#                     filemode="w")

# logger = logging.getLogger() 
# logger.setLevel(logging.DEBUG) 

# logger.debug("debug message, relax") 
# logger.info("fyi")
# logger.warning("i'm warning you")
# logger.error("something is wrong")
# logger.critical("please stop")



import requests 
url = "https://www.coingecko.com/coins/price_percentage_change?ids=1,100,10365,1047,1089,1094,11610,11636,1167,11939,12124,12151,12171,12504,12559,12645,12817,12882,13442,14495,1481,16547,16558,17980,18519,18834,2,2069,20764,2518,25751,26375,26455,26580,27045,279,28046,28205,28452,28478,28600,28624,28848,2912,29850,30061,30980,31069,31079,31401,31967,32440,325,33033,33094,33117,33345,33613,33669,3370,33800,34188,35021,35023,36291,36530,3688,3695,39580,39699,39925,39926,39969,40132,40143,4128,4380,44,4463,453,4960,5,50882,52622,52721,52804,53705,53746,54035,54342,54558,54977,5681,6319,66154,66660,67053,67164,67224,67570,69,7310,7598,780,8183,825,8418,877,975,9956&vs_currency=usd"
url2 = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
url3 = "https://cdn.jsdelivr.net/gh/prebid/currency-file@1/latest.json"
resp = requests.get(url3) 
data = resp.json() 

print(data)