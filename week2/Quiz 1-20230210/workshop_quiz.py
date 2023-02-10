payrate = float(input("Input your payrate in pounds: \n"))
workhour = int(input("Input your work hour in hours: \n"))

if workhour > 8:
    total_pay = payrate * (workhour-8) * 1.5 + 8 * payrate
    print(f'You have worked over 8 hours!\n Your first 8 hours payrate is: {payrate:.2f} \n Your last {workhour-8:2d} hours work payrate is {payrate*1.5:.2f} \n Your total working hour is: {workhour:2d} \n Your total pay is: {total_pay:.2f}')
else:
    total_pay = payrate * workhour
    print(f'Your payrate is: {total_pay/workhour:.2f} \n Your working hour is: {workhour:2d} \n Your total pay is: {total_pay:.2f}')

