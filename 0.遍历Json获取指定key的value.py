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

def get_all_keys(dic, res_list):
	if not isinstance(dic, dict) or not isinstance(res_list, list):
		return '输入的参数类型错误!'

	for k, v in dic.items():
		res_list.append(k)
		if isinstance(v, dict):
			get_all_keys(v, res_list)
		elif isinstance(v, (list, tuple)):
			for vv in v:
				get_all_keys(vv, res_list)
	return res_list

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

	dict02 = '''
{
	"a": 5,
	"recommend_summoner_skill_tips": "闪现：向指定方向位移一段距离",
	"text_price": "",
	"be_restrained_hero": [{
			"hero_id": "3",
			"name": "赵云",
			"icon": "http://pictest.wankacn.com/2017-04-26_59005ecc2eda6.png"
		},
		{
			"hero_id": "24",
			"name": "宫本武藏",
			"icon": "http://pictest.wankacn.com/2017-04-26_59005ee432c52.png"
		},
		{
			"hero_id": "39",
			"name": "韩信",
			"icon": "http://pictest.wankacn.com/2017-04-26_59005eff2e35f.png"
		}
	],
	"rec_inscriptions": [{
		"title": "four",
		"list": [{
				"name": "阳炎",
				"icon": "http://pictest.wankacn.com/2017-04-27_5901c32aec40d.png",
				"attrs": "法术攻击+2.5|法术穿透+1.4",
				"level": "4"
			}, {
				"text": 10
			},
			{
				"name": "渴血",
				"icon": "http://pictest.wankacn.com/2017-04-27_5901c33051946.png",
				"attrs": "法术攻击+1.4|法术吸血+0.8%|法术防御+1.6",
				"level": "4"
			},
			{
				"name": "侵蚀",
				"icon": "http://pictest.wankacn.com/2017-04-27_5901c3367da4c.png",
				"attrs": "法术攻击+0.9|法术穿透+3.8",
				"level": "4"
			}
		]
	}, {
		"title": "five",
		"list": [{
				"name": "圣人",
				"icon": "http://pictest.wankacn.com/2017-04-27_5901c32b7c6eb.png",
				"attrs": "法术攻击+5.3",
				"level": "5"
			}, {
				"name": "轮回",
				"icon": "http://pictest.wankacn.com/2017-04-27_5901c3325134d.png",
				"attrs": "法术攻击+2.4|法术吸血+1%",
				"level": "5"
			},
			{
				"name": "怜悯",
				"icon": "http://pictest.wankacn.com/2017-04-27_5901c3384f95c.png",
				"attrs": "冷却缩减-1%",
				"level": "5"
			}
		]
	}],
	"skill_list": [{
			"attrs": [],
			"intro": "被动",
			"mana_cost": "",
			"cd": "",
			"tags": "法术",
			"name": "冰封之心",
			"icon": "http://pic.wankacn.com/2017-08-28_59a37c3ac17e6.png"
		},
		{
			"attrs": ["基础伤害|400|480|560|640|720|800"],
			"intro": "主升",
			"mana_cost": "80",
			"cd": "5",
			"tags": "法术/控制",
			"name": "凋零冰晶",
			"icon": "http://pic.wankacn.com/2017-08-28_59a37c3de40b4.png"
		}, {
			"attrs": ["基础伤害|250|280|310|340|370|400",
				"冷却时间|10|9.2|8.4|7.6|6.8|6"
			],
			"intro": "副升",
			"mana_cost": "80",
			"cd": "8",
			"tags": "法术/控制",
			"name": "禁锢寒霜",
			"icon": "http://pic.wankacn.com/2017-08-28_59a37c4140712.png"
		},
		{
			"attrs": ["基础伤害|300|375|450", "冷却时间|50|45|40"],
			"intro": "有大点大",
			"mana_cost": "150",
			"cd": "50",
			"tags": "法术/控制",
			"name": "凛冬已至",
			"icon": "http://pic.wankacn.com/2017-08-28_59a37c4495707.png",
			"text": "what"
		}
	],
	"skill_tips": "使用凋零冰晶使对方减速后再其移动方向的前方一小段距离使用禁锢寒霜。接着立刻贴近使用凛冬已至，配合被动对敌方打出成吨伤害",
	"hero_id": "40",
	"half_img": "http://pic.wankacn.com/2017-08-28_59a3840dd8625.png",
	"ticket_price": "588",
	"type": ["2"],
	"big_img": "http://pic.wankacn.com/2017-08-28_59a38313260bb.png",
	"restrained_hero": [{
			"hero_id": "10",
			"name": "刘禅",
			"icon": "http://pictest.wankacn.com/2017-04-26_59005ed4dfde6.png"
		},
		{
			"hero_id": "23",
			"name": "典韦",
			"icon": "http://pictest.wankacn.com/2017-04-26_59005ee344db8.png"
		},
		{
			"hero_id": "48",
			"name": "亚瑟",
			"icon": "http://pictest.wankacn.com/2017-04-26_59005f0e9459e.png"
		}
	],
	"gold_price": "8888",
	"levels": {
		"attack": "3",
		"skill": "10",
		"survival": "2",
		"difficulty": "6"
	},
	"name": "王昭君",
	"hero_tips": "灵巧走位。尽量不要离敌方太近和太远，太近容易被贴身打击。太远冰冻住以后还没过去对方就解冻了。最好是等待别人与我方火并不能抽身离开时使用禁锢寒霜，给对方一个意想不到的绝望",
	"equip_choice": [{
			"title": "KPL职业出装",
			"list": [{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166adc5c9.jpeg",
					"equip_id": "40"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_59031675e2f15.jpeg",
					"equip_id": "75"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166b10ebe.jpeg",
					"equip_id": "41"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166b83498.jpeg",
					"equip_id": "43"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166c6d0eb.jpeg",
					"equip_id": "48"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166c96be0.jpeg",
					"equip_id": "49",
					"text2": "what"
				}
			]
		},
		{
			"title": "KPL职业出装",
			"list": [{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166ab272c.jpeg",
					"equip_id": "39"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_59031676397b3.jpeg",
					"equip_id": "76"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166adc5c9.jpeg",
					"equip_id": "40"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166b10ebe.jpeg",
					"equip_id": "41"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166b5c100.jpeg",
					"equip_id": "42"
				},
				{
					"icon": "http://pictest.wankacn.com/2017-04-28_5903166c96be0.jpeg",
					"equip_id": "49"
				}
			]
		}, {
			"title": "强力消耗装",
			"list": [{
				"icon": "http://pictest.wankacn.com/2017-04-28_5903166c42ac0.jpeg",
				"equip_id": "47"
			}, {
				"icon": "http://pictest.wankacn.com/2017-04-28_59031676397b3.jpeg",
				"equip_id": "76"
			}, {
				"icon": "http://pictest.wankacn.com/2017-04-28_5903166bda9f0.jpeg",
				"equip_id": "45"
			}, {
				"icon": "http://pictest.wankacn.com/2017-04-28_5903166b10ebe.jpeg",
				"equip_id": "41"
			}, {
				"icon": "http://pictest.wankacn.com/2017-04-28_5903166bb25f7.jpeg",
				"equip_id": "44"
			}, {
				"icon": "http://pictest.wankacn.com/2017-04-28_5903166c96be0.jpeg",
				"equip_id": "49"
			}]
		}
	]

}
	'''

	import json
	d1 = json.loads(dict01)
	print(get_target_value("Bpp", d1, []))
	print(get_target_value("Cb", d1, []))
	print(get_all_keys(d1, []))
	d2 = json.loads(dict02)
	print(get_target_value("be_restrained_hero", d2, []))
	print(get_target_value("equip_choice", d2, []))
	print(get_all_keys(d2, []))
