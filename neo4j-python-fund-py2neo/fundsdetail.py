# -*- coding: utf-8 -*-
import requests
import base64
import re
from py2neo import Node, Graph, Relationship, NodeMatcher

from pandas.io.json import json_normalize
import json
import pandas as pd

#print(r.find('html'))
link = Graph(password="stick-cliff-fossil-float-leopard-5502")
graph = link
matcher = NodeMatcher(link)

def printme( str ):
    str02= re.findall(str+'.*?;',r,flags=0)
    str03 =str02[0].replace(" ", "")
    return (str03[str03.index('="')+2:str03.index('";')]) 

for i in range(100000):
    code=str(i).zfill(6)
    url="https://fund.eastmoney.com/pingzhongdata/"+code+".js"
    r = str(requests.get(url).text)

    if(r.find('html')==-1):
        node1 = matcher.match("基金名称").where(name=printme('fS_name = ')).first()
        node2 = matcher.match("原费率").where(name=printme('fund_sourceRate=')).first()
        #print(node2)
        if node2 is None:
            node2=Node("原费率",name =printme('fund_sourceRate=')) 
        #print(node2)
        node3 = matcher.match("现费率").where(name=printme('fund_Rate=')).first()
        if node3 is None:
            node3=Node("现费率",name =printme('fund_Rate=')) 
        node4 = matcher.match("最小申购金额").where(name=printme('fund_minsg=')).first()
        if node4 is None:
            node4=Node("最小申购金额",name =printme('fund_minsg=')) 
        node5 = matcher.match("近一年收益率").where(name=printme('syl_1n=')).first()
        if node5 is None:
            node5=Node("近一年收益率",name =printme('syl_1n='))  

        node6 = matcher.match("近6月收益率").where(name=printme('syl_6y=')).first()
        if node6 is None:
            node6=Node("近一年收益率",name =printme('syl_6y='))     

        node7 = matcher.match("近三月收益率").where(name=printme('syl_3y=')).first()
        if node7 is None:
            node7=Node("近三月收益率",name =printme('syl_3y='))    

        node8 = matcher.match("近一月收益率").where(name=printme('syl_1y=')).first()
        if node8 is None:
            node8=Node("近一月收益率",name =printme('syl_1y='))         

        r1 = Relationship(node1,'原费率',node2)
        graph.create(r1)
        r2 = Relationship(node1,'现费率',node3)
        graph.create(r2)       
        r3 = Relationship(node1,'最小申购金额',node4)
        graph.create(r3)       
        r4 = Relationship(node1,'近一年收益率',node5)
        graph.create(r4)        
        r5 = Relationship(node1,'近6月收益率',node6)
        graph.create(r5)        
        r6 = Relationship(node1,'近三月收益率',node7)
        graph.create(r6)       
        r7 = Relationship(node1,'近一月收益率',node8)
        graph.create(r7)