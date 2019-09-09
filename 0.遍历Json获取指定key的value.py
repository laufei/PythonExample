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
				_get_value(key, value, tmp_list)
	return tmp_list

def _get_value(key, val, tmp_list):
	for val_ in val:
		if isinstance(val_, dict):
			get_target_value(key, val_, tmp_list)
		elif isinstance(val_, (list, tuple)):
			_get_value(key, val_, tmp_list)

def get_all_keys(dic, res_list):
	if not isinstance(dic, dict) or not isinstance(res_list, list):
		return '输入的参数类型错误!'

	for k, v in dic.items():
		res_list.append(k)
		if isinstance(v, dict):
			get_all_keys(v, res_list)
		elif isinstance(v, (list, tuple)):
			_get_keys(v, res_list)
	return res_list

def _get_keys(val, res_list):
	for val_ in val:
		if isinstance(val_, dict):
			get_all_keys(val_, res_list)
		elif isinstance(val_, (list, tuple)):
			_get_keys(val_, res_list)

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
			"Ca": 3,
			"Cb": 4
		}, {
			"Ca": 5,
			"Cb": 6
		}]
	}'''

	dict03 = '''{
	"a": 1,
	"b": 2,
	"c": {
		"d": [{
			"e": [{
				"f": [{
					"v": [{
							"g": 6
						},
						[{
								"g": 7
							},
							[{
								"g": 8
							}]
						]
					]
				}, "m"]
			}]
		}, "h", {
			"g": [10, 12]
		}]
	}
}'''

	import json
	d1 = json.loads(dict01)
	print(get_target_value("Cb", d1, []))
	print(get_all_keys(d1, []))

	d3 = json.loads(dict03)
	print(get_target_value("g", d3, []))
	print(get_all_keys(d3, []))
