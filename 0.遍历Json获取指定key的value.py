# coding: utf-8

def get_target_value(key, dic, tmp_list):
	if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
		return '输入的参数类型错误!'

	if key in dic.keys():
		tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
	else:
		for value in dic.values():  # 传入数据不符合则对其value值进行遍历
			if isinstance(value, dict):
				get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
			elif isinstance(value, (list, tuple)):
				for v in value:
					get_target_value(key, v, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
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