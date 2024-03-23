# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)
        
        ##Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                adapter[field_name]= value[0].strip()
                
        ## Category & Product Type --> switch to lowercase
        lowercase_keys = ['category', 'product_type'] #specify specific keys\items
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()
            
        ## Price --> convert to float
        price_keys = ['price']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '') #replace the pound sign with the rand sign
            adapter[price_key] = float(value)
            adapter[price_key] = adapter[price_key] * 24.0
            adapter[price_key] = str(adapter[price_key])
            adapter[price_key] = "R" + adapter[price_key]
            
        
        return item 
