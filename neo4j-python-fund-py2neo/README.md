利用数据抽取，加载到neo4j数据库中构建相关知识图谱

运行环境：  
python3.6.5  
windows11 
具体包依赖可以参考文件requirements.txt
```
pip install -r requirements.txt
``` 

1.neo4j的下载安装
社区版
https://neo4j.com/download-center/#community
启动命令
neo4j.bat console
开始启动会有个设置密码的环节

2.安装py2neo
pip install py2neo即可


3.如何获得基金的数据
基金数据：
http://fund.eastmoney.com/js/fundcode_search.js
基金详情：
https://fund.eastmoney.com/pingzhongdata/980003.js


4.