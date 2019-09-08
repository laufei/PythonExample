# coding: utf-8
import json
def get_dict_allkeys(dic):
		"""
		多维/嵌套字典数据无限遍历，获取json返回结果的所有key值集合
		"""
		key_list = []

		dict_a = json.loads(dic)
		if isinstance(dict_a, dict):
			for k, v in dict_a.items():
				key_list.append(k)
				get_dict_allkeys(v)
		elif isinstance(dict_a, list):
			for item in dict_a:
				if isinstance(item, dict):
					for k, v in item.items():
						key_list.append(k)
						get_dict_allkeys(v)
		return key_list

# 测试
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

print(get_dict_allkeys(dict01))
