import pyupbit

access =
secret =       # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-UPP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회