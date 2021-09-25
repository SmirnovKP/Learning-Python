catalog_item = {
	"type":"phone",
	"vendor":"Apple",
	"model":"Iphone 12"
	"price":37,5
}

print(catalog_item)

catalog_item['audio_jack']=False
catalog_item['price'] = 70
print (catalog_item['price'])
item_name = catalog_item['vendor']+' '+catalog_item['model']

Print(catalog_item[‘discount’])

catalog_item.get('discount', 'Скидок нет!')

'model' in catalog_item
'discount' not in catalog_item
'discount' in catalog_item

del catalog_item[‘price’]