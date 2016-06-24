import os
import json
import re

def get_struct(json_data):
	ret = ""
	if isinstance(json_data, list):
		if len(json_data) > 1:
			if isinstance(json_data[0], dict) or isinstance(json_data[0], list):
				return get_struct(json_data[0])
			else:
				return ""
		return ""
	#print "type:{}, json_data:{}".format(type(json_data), )
	for key in json_data:
		if isinstance(json_data[key], bool):
			ret += '{{"name":"{}", "mode":"{}", "type":"{}"}},'.format(key, "NULLABLE", "BOOLEAN")
			continue

		if isinstance(json_data[key], str) or isinstance(json_data[key], unicode) :
			ret += '{{"name":"{}", "mode":"{}", "type":"{}"}},'.format(key, "NULLABLE", "STRING")
			continue

		if isinstance(json_data[key], int):
			ret += '{{"name":"{}", "mode":"{}", "type":"{}"}},'.format(key, "NULLABLE", "INTEGER")
			continue

		if isinstance(json_data[key], float):
			ret += '{{"name":"{}", "mode":"{}", "type":"{}"}},'.format(key, "NULLABLE", "FLOAT")
			continue

		if isinstance(json_data[key], dict):
			ret += '{{"name":"{}", "mode":"{}", "type":"{}", "fields":[{}]}},'.format(key, "NULLABLE", "RECORD", get_struct(json_data[key]))
			continue
		
		if isinstance(json_data[key], list):
			ret += '{{"name":"{}", "mode":"{}", "type":"{}", "fields":[{}]}},'.format(key, "REPEATED", "RECORD", get_struct(json_data[key]))
			continue
	return ret[:-1]

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]
	
def remove_comments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    return string
	
if __name__ == '__main__':
	dir_path = './json/'
	out_path = './bq_schema/'
	for filename in listdir_fullpath(dir_path):
		if filename.endswith(".json"):
			with open(filename) as data_file:
				data = str(data_file.read())
				data = remove_comments(data)
				data = json.loads(data)
				result = "[ "
				result += get_struct(data)
				result += " ]"
				basename = os.path.basename(filename)
				output_name = os.path.splitext(basename)[0]+'.schema'
				if not os.path.exists(out_path):
				    os.makedirs(out_path) 
				f = open(out_path + output_name, 'w')
				f.write(result)
				f.close()
			
	#json_data = '{"timestampValue":{"seconds":1480291200},"variants":[{"id":"4930635cf5d843eabc74ef8bb6ff7a29","product_id":"f71407577bb6479993bd09fcd9413039","retail_price":351.09736607491345,"type":{"color":"Turquoise","size":"M"}},{"id":"18f4f000403b439b99e3397ab90bf83a","product_id":"85779bec89c14bc78f3a56103a87854b","retail_price":882.9315997833187,"type":{"color":"Pink","size":"M"}}]}'
	#obj = json.loads(json_data)
