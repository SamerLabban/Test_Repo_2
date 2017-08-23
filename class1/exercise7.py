import yaml
import json
from pprint import pprint as pp

with open("my_list_file.yml") as f:
    new_list = yaml.load(f)

print "Below is the YAML file:"
pp(new_list)

with open("my_list_file.json") as f:
	new_list = json.load(f)

print "\nBelow is the JSON file:"
pp(new_list)


