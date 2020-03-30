# 整合官方和常用示例
# https://api.mongodb.com/python/current/py-modindex.html

import datetime
import multiprocessing
import ssl
import urllib.parse
from pprint import pprint

import gridfs
import pymongo
import pytz
from bson import CodecOptions, json_util
from bson.code import Code
from bson.objectid import ObjectId
from bson.son import SON
from pymongo import (DeleteMany, InsertOne, MongoClient, ReplaceOne, UpdateOne,
                     WriteConcern, errors)

client = MongoClient(host="192.168.2.15", port=27017)

all_databases = client.list_database_names()
pprint(all_databases)
# using dictionary style access
db = client["AdminConfigDB"]

all_collections = db.collection_names()

pprint(all_collections)
# using nomal style
collection = db.arc_AdminConf

# pprint(collection.find_one({}))


# for collection in collection.find({"flush":False}).sort("productId"):
#     pprint(collection)

# 以product_id升序创建索引
# create_index = collection.create_index([('product_id', pymongo.ASCENDING)], unique=True)

# 打印集合索引
for index in collection.list_indexes():
    pprint(index)

# 打印集合索引信息
# pprint(sorted(list(collection.index_information())))

db2 = client.TestData
collection2 = db2.things
# result = collection2.insert_many([{"x": 1, "tags": ["dog", "cat"]},
#                                   {"x": 2, "tags": ["cat"]},
#                                   {"x": 2, "tags": ["mouse", "cat", "dog"]},
#                                   {"x": 3, "tags": []}])
# pprint(result.inserted_ids)

# Aggregation Framework示例
# pipeline = [
#         {"$unwind": "$tags"},
#         {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
#         {"$sort": SON([("count", -1), ("_id", -1)])}]

# pprint(list(collection2.aggregate(pipeline)))

# Map/Reduce示例
# mapper = Code(
#     """
#               function () {
#                     this.tags.forEach(function(z) {
#                       emit(z, 1);
#                     });
#                   }
#                """
# )

# reducer = Code(
#     """
#                    function (key, values) {
#                      var total = 0;
#                      for (var i = 0; i < values.length; i++) {
#                        total += values[i];
#                      }
#                      return total;
#                    }
#                """
# )

# result = collection2.map_reduce(mapper, reducer, "map_reduce_result")
# for doc in result.find():
#     pprint(doc)

# results = collection2.map_reduce(
#         mapper, reducer, "myresults", query={"x": {"$lt": 2}})
# for doc in results.find():
#     pprint(doc)

# 认证示例
# username = urllib.parse.quote_plus('user')
# password = urllib.parse.quote_plus('pass/word')
# client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))

# version3.7支持SCRAM-SHA-256
# client = MongoClient('example.com',
#                          username='user',
#                          password='password',
#                          authSource='the_database',
#                          authMechanism='SCRAM-SHA-256')
# mongodb uri连接方式
# uri = "mongodb://user:password@example.com/?authSource=the_database&authMechanism=SCRAM-SHA-256"
# client = MongoClient(uri)
# mongodb-x509认证
# client = MongoClient('example.com',
#                      username="<X.509 derived username>",
#                      authMechanism="MONGODB-X509",
#                      ssl=True,
#                      ssl_certfile='/path/to/client.pem',
#                      ssl_cert_reqs=ssl.CERT_REQUIRED,
#                      ssl_ca_certs='/path/to/ca.pem')

# 复制一个数据库
# client.admin.command('copydb', fromdb='src_db_name', todb='dst_db_name', fromhost='src_host_ip')

# 批量插入
# _id对于大多数高写入量的应用程序而言，对于插入的文档本身没有_id字段时，在插入时自动创建代价较高。inserted_ids表示按提供_id的顺序插入文档
# collection2.insert_many([{'x': i} for i in range(10000)]).inserted_ids
# print(collection2.count_documents({}))

# 批量删除
# collection2.delete_many({'x':{"$gte": 3}})

# bulk write，混合批量写入
# 添加write_concern 写关注
# collection2 = db2.get_collection('things', write_concern=WriteConcern(w=2, wtimeout=10))
# try:
#   result = collection2.bulk_write([
#       DeleteMany({}),  # Remove all documents from the previous example.
#       InsertOne({'_id': 1}),
#       InsertOne({'_id': 2}),
#       InsertOne({'_id': 3}),
#       UpdateOne({'_id': 1}, {'$set': {'foo': 'bar'}}),
#       UpdateOne({'_id': 4}, {'$inc': {'j': 1}}, upsert=True),
#       ReplaceOne({'j': 1}, {'j': 2})])
# except errors.BulkWriteError as bwe:
# pprint(bwe.details)
# pprint(result.bulk_api_result)


# 日期时间和时区(mongodb默认假定时间以UTC)
# result = db2.objects.insert_one({"last_modified": datetime.datetime.utcnow()})

# tz_aware选项，该选项启用“感知” datetime.datetime对象.即知道其所在时区的日期时间
# result = db2.demo.insert_one( {'date': datetime.datetime(2019, 11, 28, 14, 0, 0)})
# db2.demo.find_one()['date']
# datetime.datetime(2019, 11, 28, 14, 0)
# options = CodecOptions(tz_aware=True)
# db2.get_collection('demo', codec_options=options).find_one()['date']

# 使用时区保存日期时间
# 存储datetime.datetime指定时区的对象，即tzinfo属性不是None时，PyMongo会将这些日期时间自动转换为UTC
# pacific = pytz.timezone('Asia/Shanghai')
# aware_datetime = pacific.localize( datetime.datetime(2019, 11, 28, 14, 0, 0))
# result = db2.demo.insert_one({"date_tz": aware_datetime})
# datetime.datetime(2019, 11, 28, 14, 0)

# 地理空间索引示例
# https://api.mongodb.com/python/current/examples/geo.html

# GridFS示例
# 每个GridFS实例都是使用特定Database实例创建的，并将在特定实例上运行
# db = MongoClient().gridfs_example
# fs = gridfs.GridFS(db)
# 将数据写入gridfs,put()在GridFS中创建一个新文件，并返回文件文档"_id"密钥的值
# data = fs.put(b"hello world")
# get()方法取回文件内容,get()返回类似文件对象，调用read()方法获取文件内容
# content = fs.get(data).read()
# 除了将str作为GridFS文件放置外，还可以放置任何类似文件的对象（带有read() 方法的对象）。GridFS将自动处理按块大小的段读取文件。还可以将其他属性作为关键字参数添加到文件中
# b = fs.put(fs.get(a), filename="foo", bar="baz")
# out = fs.get(b)
# out.read()
# out.filename
# out.bar
# out.upload_date

# 可拖尾游标，客户端用尽游标中所有结果后自动关闭游标，但对于上限集合(copped集合)可以使用可拖尾的游标
# https://api.mongodb.com/python/current/examples/tailable.html


# 自定义类型
"""
https://api.mongodb.com/python/current/examples/custom_type.html

为了编码自定义类型，必须首先为该类型定义类型编解码器
用户在定义类型编解码器时必须从以下基类中进行选择：
* TypeEncoder：将其子类化以定义将自定义Python类型编码为已知BSON类型的编解码器。用户必须实现 python_type属性/属性和transform_python方法。

* TypeDecoder：将其子类化以定义将特定BSON类型解码为自定义Python类型的编解码器。用户必须实现bson_type属性/属性和transform_bson方法。

* TypeCodec：此方法的子类以定义可以对自定义类型进行编码和解码的编解码器。用户必须实现 python_type和bson_type属性/属性以及 transform_python和transform_bson方法。

自定义类型的类型编解码器仅需要定义如何将 Decimal实例转换为 Decimal128实例，反之亦然

from bson.decimal128 import Decimal128
from bson.codec_options import TypeCodec
class DecimalCodec(TypeCodec):
    python_type = Decimal    # the Python type acted upon by this type codec
    bson_type = Decimal128   # the BSON type acted upon by this type codec
    def transform_python(self, value):
        # Function that transforms a custom type value into a type that BSON can encode
        return Decimal128(value)
    def transform_bson(self, value):
        # Function that transforms a vanilla BSON type value into our custom type
        return value.to_decimal()
decimal_codec = DecimalCodec()

# 开始对自定义类型对象进行编码和解码之前，我们必须首先将相应的编解码器告知PyMongo。这是通过创建一个TypeRegistry实例来完成
# 以使用任意数量的类型编解码器实例化类型注册表。一旦实例化，注册表是不可变的，将编解码器添加到注册表的唯一方法是创建一个新的注册表
from bson.codec_options import TypeRegistry
type_registry = TypeRegistry([decimal_codec])

# 使用CodecOptions实例定义一个实例，type_registry并使用它来获取一个Collection理解Decimal数据类型的对象

未完待续......

"""


# mongodb跨数据库查询、跨表(集合)、跨服务器查询都可根据以下方式修改
# 查询data下product集合以条件gaId为1不重复的paId
# 使用此paId作为查询pa下pa_info集合以条件pa_id等于paId且v为1的文档
# data = client.data
# product = data.product

# pa = client.pa
# pa_info = pa.pa_info

# pipeline = [
#     {"$match": {"gaId": 1}},
#     {"$sort": {"paId": -1}},
#     {"$group": {"_id": "$paId"}},
#     {"$project": {"paId": 1.0}},
# ]

# cursor = pa_info.aggregate(pipeline, allowDiskUse=False)
# try:
#     for doc in cursor:
#         doc_value = doc['_id']
#         pa_result = pa_info.find({"pa_id": doc_value, "v":1})
#         for pa_doc in pa_result:
#             # 查询到的结果写入到其他集合
#             result_insert = collection2.insert_many([pa_doc])
#         # pass
# finally:
#     client.close()

# 父进程和每个子进程必须创建自己的MongoClient实例
# Each process creates its own instance of MongoClient.
# def func():
#     db = pymongo.MongoClient().mydb
#     # Do something with db.

# proc = multiprocessing.Process(target=func)
# proc.start()
