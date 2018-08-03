#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-02 10:18:27
# @Author  : sue (2315172434@qq.com)
# @Link    : http://www.sevencolorhhy.com
# @Version : $Id$

import os
import requests
import json

url='https://api.weixin.qq.com/card/update?access_token=12_tRbtsCqO1TU_8t6hq9PbNGKnDrXgdXBLaVjRsr7a-7_NTDuaeMeMiC7hrFlE_EfbwptZ7GkgRqMtnHnxJSQB1oGQykESSyzFuzdsLRPvnIdkW8U8TO8ndvV29AYf1NO5J3LzVRJilE1UtyWLPIUgACADWI'

#para="'card_id':'pdgaDwWrXpLSncmhNYr5z5dXEx9M','member_card': {'base_info': {'begin_timestamp':'1530719999','end_timestamp':'1546358399'}"
# para={"card_id":"pdgaDwWrXpLSncmhNYr5z5dXEx9M",
#         "member_card": {
      
#        
# 					
#                }
#      }
para={'card_id':'pdgaDwWrXpLSncmhNYr5z5dXEx9M',
	'member_card':{
		 'base_info':{
		 	'begin_timestamp':'1530719999',
			'end_timestamp':'1546358399'
		 }
	}
}
jsonpara=json.dumps(para)
print(jsonpara)

result=requests.post(url,json=jsonpara)
result.encoding='utf-8'
print(result.text)