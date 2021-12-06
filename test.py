import pyupbit

access = "VjWBodSBEqdT5YOrKBxZxTPoiwVBsgM34hk4ze1t"
secret = "V3KOjp9ZB4x5Wcyas9tyxqpE8vuNDUuWVpZuGxdy"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-UPP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회