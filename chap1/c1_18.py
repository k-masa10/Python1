price=input('料金を入力 >>')
price=int(price)
number=input('人数を入力 >>')
number=int(number)
payment=price/number
payment=str(payment)
print('お支払いは'+payment+'円です')