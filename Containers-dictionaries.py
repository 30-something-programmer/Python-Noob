
#Dictionaries are MUTABLE and do not store data in order
#Dictionaries are defined by its NAME, the KEYS and the VALUES
#The KEYS must be immutable!!! i.e. tuples CAN be dict keys

#Creation
my_dict = dict()
my_dict = {}

#Mapping
my_dict['key'] = 'value'
my_dict['cat'] = 'Link'
my_dict['Apple':'Red',"Banana":'Yellow']
my_dict['Dracula':'Stoker',
    '1984':'Orwell'
    'The Trial':'Kafka']


#calling
my_dict['key']

#Checking for entries - can only find KEYS; not values!
'Apple' in my_dict
'Grape' not in my_dict

#Remove an entry
del my_dict['The Trial']

