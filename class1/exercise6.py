import yaml
import json

#Create list
my_list = ["cars", "airplanes", {"food":["ham", "burger", "cheese"], "city":["Vancouver", "NewYork"]}]
my_list[-1]['sports'] = 'soccer'
my_list[-1]['sports'] = 'basketball'
my_list[-1]['attribs'] = range(7)


#Write list to file using yaml (in expanded form)
with open('my_list_file.yml', 'w') as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

#Write list to file using json
with open('my_list_file.json', 'w') as f:
    json.dump(my_list, f)
