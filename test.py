import pyupbit

access = "8fdKhUQdikizHtYeJgw9mo1QvJx8c5lhzpq0KnRq"          # 본인 값으로 변경
secret = "2KC2Q8sqV7NLD0JD8uhATHjdJXsJOz6A1aBXMcxl"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-SAND"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회