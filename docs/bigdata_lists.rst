大数据应用列表
================

Kafka
------
Kafka是一种高吞吐量的分布式发布订阅消息系统，它可以处理所有的动作流数据。
它通过O(1)的磁盘数据结构提供消息的持久化，这种结构对于即使数以TB的消息存储也能够保持长时间的稳定性能。
拥有高吞吐量即使是非常普通的硬件，Kafka也可以支持每秒数百万的消息。
同时Kafka支持通过服务器和消费机集群来分区消息。

安装关键字
~~~~~~~~~~~~
.. code-block:: bash

    -s bigdata -ba kafka 或者 --server bigdata --bigdata-app kafka


话题（topic）
~~~~~~~~~~~~~~
.. code-block:: bash

    # 创建话题
    sudo ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

    # 检查话题
    sudo ./bin/kafka-topics.sh --list --zookeeper localhost:2181

    # 删除话题
    sudo ./bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic test

运行生产者（producer）
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    sudo ./bin/kafka-console-producer.sh --broker-list <IP Address>:9092 --topic test

运行消费者（consumer）
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    sudo ./bin/kafka-console-consumer.sh --bootstrap-server <IP Address>:9092 --topic test --from-beginning

Kafka安装配置
~~~~~~~~~~~~~~~~~
- 安装路径：/opt/kafka
- bin目录: /opt/kafka/bin
- zookeeper配置文件：/opt/kafka/config/zookeeper.properties
- kafka配置文件：/opt/kafka/config/server.properties