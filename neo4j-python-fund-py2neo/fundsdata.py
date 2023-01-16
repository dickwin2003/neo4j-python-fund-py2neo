# -*- coding: utf-8 -*-
import requests
import base64
from py2neo import Node, Graph, Relationship, NodeMatcher

from pandas.io.json import json_normalize
import json
import pandas as pd

url = "http://fund.eastmoney.com/js/fundcode_search.js"
r = requests.get(url).text
#print(r.text)
#ss = r.encode('ascii').decode('unicode_escape') #强制转化unicode编码，将此str转化为bytes

str=(r.replace("var r =", "").replace(";", ""))
#print(r[2])

js=json.loads(str)

#格式化
data_table = pd.DataFrame(js)
print(len(data_table))
print(data_table.values[1][0])

#导出excel
data_table.to_excel('./Funds.xlsx',index = False)    

"""建立连接"""
#link = Graph("http://127.0.0.1//:7474", username="xxx", password="xxx")
link = Graph(password="stick-cliff-fossil-float-leopard-5502")
graph = link
matcher = NodeMatcher(link)

graph.delete_all()


for row in data_table.itertuples():
    node_code=Node("基金代码",name =row[1]) 
    node_py=Node("简拼",name =row[2]) 
    node_name=Node("基金名称",name =row[3]) 
    node_type = matcher.match("类型").where(name =row[4]).first()
        #print(node2)
    if node_type is None:
        node_type=Node("类型",name =row[4]) 

    #node_type=Node("类型",name =row[4]) 
    node_lpy=Node("全拼",name =row[5]) 

    graph.create(node_code)
    graph.create(node_py)
    graph.create(node_name)
    graph.create(node_type)
    graph.create(node_lpy)
    #print(row[4])
    r1 = Relationship(node_name,'代码',node_code)
    graph.create(r1)
    r2 = Relationship(node_name,'简拼',node_py)
    graph.create(r2)
    r3 = Relationship(node_name,'类型',node_type)
    graph.create(r3)
    r4 = Relationship(node_name,'全拼',node_lpy)
    graph.create(r4)

    #print(row[3])
