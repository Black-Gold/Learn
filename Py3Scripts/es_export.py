from elasticsearch import Elasticsearch
import json


# 如有报错：Result window is too large, from + size must be less than or equal to: [10000]
# 执行以下修改：【不再使用此方式，防止内存溢出，使用如下的scroll api处理】
# curl -XPUT "http://192.168.2.15:9200/index/_settings" -d '{ "index" : { "max_result_window" : 1000000 } }'

# 定义数据写入的文件路径
root_path = "D:/xxx.json"


def record_docs(root_path, record):
    with open(root_path, "a", encoding="utf-8") as file:
        file.write(record)
        file.close()


#  定义配置
host = "192.168.2.15:9200"
# index = "index"
index = "index"
scroll = "1m"
size = 1000
body = {
    "query": {"match_all": {}},
}


es = Elasticsearch(hosts=host)

# es.indices.refresh(index="index")

# 利用json.dumps处理hits数据,将返回str类型


def process_hits(hits):
    for item in hits:
        # print(json.dumps(item["_source"], indent=2))
        # print(json.dumps(item["_source"]))
        record_docs(root_path, json.dumps(item["_source"]))


# 检查index是否存在
if not es.indices.exists(index=index):
    print("index：" + index + "不存在")
    exit()

# 数据总量大于等于1000时，用scroll api搜索
data_scroll = es.search(index=index, scroll=scroll, size=size, body=body)

# 数据总量少于1000时，将使用此搜索方式
data = es.search(index=index, size=size, body=body)

# 获取scroll id
scroll_id = data_scroll["_scroll_id"]

# 获取匹配文档数
# scroll_size = len(data["hits"]["hits"])
# 获取匹配文档总数
scroll_size = data["hits"]["total"]
print("匹配到文档总数为：" + str(scroll_size) + "\n")

if scroll_size > 0 and scroll_size < 1000:
    process_hits(data["hits"]["hits"])
elif scroll_size >= 1000:
    while scroll_size > 0:
        # print("处理中ing......")
        # 滚动处理之前，先处理当前匹配项
        process_hits(data_scroll["hits"]["hits"])
        data_scroll = es.scroll(scroll_id=scroll_id, scroll=scroll)

        #  更新scroll id
        scroll_id = data_scroll["_scroll_id"]
        #  获取最后一次scroll的数量
        scroll_size = len(data_scroll["hits"]["hits"])
