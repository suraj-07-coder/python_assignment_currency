import suraj_a1
old=input('Enter original currency:')
new=input('Enter desired currency:')
amt=float(input('Enter original amount:'))

# do not modify the following code
#if the source currency is not valid , quit

if(not(suraj_a1.is_currency(old))):
	print(old,"is not a valid currency")
	quit()

#if the target currency is not valid , quit

if(not(suraj_a1.is_currency(new))):
	print(new,"is not a valid currency")
	quit()
else:
	print('you can exchange',amt,old,'for' ,suraj_a1.exchange(old,new,amt),new)