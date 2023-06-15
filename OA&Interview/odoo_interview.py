"""Usecases: 

ST1 is made of ST2 and ST4,
ST2 is made of CO1 and ST3.
ST4 is made of CO2


- Sample Input Product Data:
- We do not know how many products we may have but the data structure will be consistent:
    
products = {
    'CO1' : {
        'type' : 'CONSU',
        'on_hand_qty': -1.0,
        'components': {}
    },
    'CO2' : {
        'type' : 'CONSU',
        'on_hand_qty': -1.0,
        'components': {}
    },
    'ST4' : {
        'type' : 'STOCK',
        'on_hand_qty': 100.0,
        'components': {
            'CO2': 4.0, 
        }
    },
    'ST3' : {
        'type' : 'STOCK',
        'on_hand_qty': 7.0,
        'components': {
        }
    },
    'ST2' : {
        'type' : 'STOCK',
        'on_hand_qty': 10.0,
        'components': {
            'CO1': 3.0, 
            'ST3': 2.0, 
        }
    },
    'ST1' : {
        'type' : 'STOCK',
        'on_hand_qty': 0.0,
        'components': {
            'ST2': 1.0,
            'ST4': 6.0, 
            "ST3", 3.0       
        }
    },
}

Expected Result for Manufacturable Stockable Quantity:
    
stockable_products = {
    'ST1' : 13.0,
    'ST2' : 3.0,
    'ST3' : 0.0, 
    'ST4' : -1.0,  
}
Your solution goes below :"""
from collections import defaultdict
def get_stockable_products(products):
  stackable_products = defaultdict(int) # key: stackable components, value: the amount
  consu_products = []
  for component in stackable_products.keys():
    if products[component]['type'] == "STOCK":
      stackable_products[component] = products[component]['on_hand_qry']
    if len(products[component]['components']) == 0:
      stackable_products[component] = 0
    if  products[component]['type'] == 'CONSU':
      consu_products.append(component)
  
  for stockable, quantity_on_hand in stackable_products.items():
    # deal with cases like ST3
    if quantity_on_hand == 0:
      continue 
    # deal with cases like ST4
    if all(products[stockable]["components"].keys() in consu_products):
      quantity_on_hand = -1.0
    # general cases like st1 and st2 
    else:
      # get the compnents dict
      needed_products_dict = products[stockable]["components"]
      for product, needed_quantity in needed_products_dict.items():
        if product in consu_products:
          continue
        else:
          # only construct the component if having enough components
          if stackable_products[product] > needed_quantity:
            amount = stackable_products[product]//needed_quantity
            stackable_products[product] -= amount*needed_quantity
            quantity_on_hand += amount 
          else:
            continue
          
  return stackable_products
      
    
  
  