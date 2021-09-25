#Function VAT
def get_vat(payment, persent=20):
	try:
		payment = float(payment)
		vat = payment / 100 * persent
		vat = round(vat, 2)
		return "Sum VAT: {}".format(vat)
	except TypeError:
		return "Can't count. Check data!"

result = get_vat(400, 15)
print(result)