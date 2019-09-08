# coding: utf-8

def get_target_value(key, dic, tmp_list):
	"""
	:param key: 目标key值
	:param dic: JSON数据
	:param tmp_list: 用于存储获取的数据
	:return: list
	"""
	if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
		return '输入的参数应该是一个dict或者list对象!'

	if key in dic.keys():
		tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
	else:
		for value in dic.values():  # 传入数据不符合则对其value值进行遍历
			if isinstance(value, dict):
				get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
			elif isinstance(value, (list, tuple)):
				_get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
	return tmp_list

def _get_value(key, val, tmp_list):
	for val_ in val:
		if isinstance(val_, dict):
			get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
		elif isinstance(val_, (list, tuple)):
			_get_value(key, val_, tmp_list)   # 传入数据的value值是列表或者元组，则调用自身

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