1.neo4j的下载安装
社区版下载
https://neo4j.com/download-center/#community
开发文档：https://neo4j.com/docs/cypher-manual/current/clauses/match/
启动命令
neo4j.bat console
开始启动会有个设置密码的环节

2.安装py2neo
pip install py2neo即可
py2neo的简单使用
https://www.cnblogs.com/edkong/p/16167542.html
py2neo官方文档：
https://py2neo.org/v5/matching.html#relationship-matching

3.如何获得基金的数据以及选择
tushare:http://tushare.org/macro.html#id5
baostock:http://baostock.com/baostock/index.php/%E9%A6%96%E9%A1%B5

基金数据：
http://fund.eastmoney.com/js/fundcode_search.js
基金详情：
https://fund.eastmoney.com/pingzhongdata/980003.js


4.
基金详情
节点和关系的创建

测试：
node_name=Node("基金名称",name ='英大国企改革主题股票') 

node_lpy=Node("test1",name ='test1')

    
r2 = Relationship(node_code,'test1',node_lpy)
graph.create(r2)

node = node_matcher.match("基金名称").where(name='英大国企改革主题股票').first()

relationship = list(relationship_matcher.match(None, r_type='test1'))


match (n:基金名称) return count(n)

match (n:基金名称) return count(distinct n.name)

MATCH (n:Tag)
WITH n.name AS name, COLLECT(n) AS nodelist, COUNT(*) AS count
WHERE count > 1
CALL apoc.refactor.mergeNodes(nodelist) YIELD node
RETURN node

match (a)-[r]->(b) with a,b, count(*) as c where c>1 return a.name, b.name, c LIMIT 100000;

node_lpy=Node("someone",name ='someone')
MATCH (root {name:"易方达天天理财货币B"}) 
CREATE UNIQUE (root)-[:LOVES]-(node_lpy) 
RETURN someone 

MATCH
  (charlie:player {name: 'shikar Dhawan'}),
  (oliver:player {name: 'Kumar Sangakkara'})
MERGE (charlie)-[r:FATHER]-(oliver)
RETURN r


CREATE(Dhawan:player{id:001, name: "shikar Dhawan", YOB: 1995, POB: "Delhi"}) 
CREATE(Jonathan:player {id:002, name: "Jonathan Trott", YOB: 1981, POB: "CapeTown"}) 
CREATE(Sangakkara:player {id:003, name: "Kumar Sangakkara", YOB: 1977, POB: "Matale"}) 
CREATE(Rohit:player {id:004, name: "Rohit Sharma", YOB: 1987, POB: "Nagpur"}) 
CREATE(Virat:player {id:005, name: "Virat Kohli", YOB: 1988, POB: "Delhi"}) 

--name: 易方达天天理财货币B
MATCH
  (charlie:基金名称 {name: '易方达天天理财货币B'}),
  (oliver:原费率 {name: '0.80'})
MERGE (charlie)-[r:原费率]-(oliver)
RETURN r

node1 = node_matcher.match("基金名称").where(name='易方达天天理财货币B')
node2 = node_matcher.match("player").where(name='Virat Kohli').first()
r3 = Relationship(node1,'基金经理',node2)
