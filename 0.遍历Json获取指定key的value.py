# coding: utf-8

def get_target_value(key, dic, tmp_list):
	if not isinstance(dic, dict) or not isinstance(tmp_list, list):
		return '输入的参数类型错误!'

	if key in dic.keys():
		tmp_list.append(dic[key])
	else:
		for value in dic.values():
			if isinstance(value, dict):
				get_target_value(key, value, tmp_list)
			elif isinstance(value, (list, tuple)):
				for v in value:
					get_target_value(key, v, tmp_list)
	return tmp_list

if __name__ == "__main__":
	dict01 = '''{
		"A": 1,
		"B": {
			"Bkk": {
				"Bnn": 111,
				"Bpp": "ppoii"
			},
			"Byy": "123aa",
			"Buu": "777aa"
		},
		"C": [{
			"Ca": 1,
			"Cb": 2
		}, {
			"Caa": 3,
			"Cbb": 4
		}, {
			"Caaa": 5,
			"Cbbb": 6
		}]
	}'''

	import json
	d = json.loads(dict01)
	print(get_target_value("Bpp", d, []))
	print(get_target_value("Cb", d, []))