# Installation
[text](https://kafka.apache.org/downloads)<br>
1. Install Binary downloads.<br>
2. tar xvf kafka_2.12-3.8.0.tgz<br>
3. rename the folder kafka_2.12-3.8.0 to kafka.<br>
4. cd ~ <br>
5. nano .bashrc<br>
6. At very bottom add <b>export PATH="/path/kafka/bin:$PATH"</b><br>
7. source ~/.bashrc [For Reload path variables]<br>
8. In /kafka create a dir named <b>data</b> and under that dir create <b>zookeeper</b>
and <b>server</b> named dirs.<br>
9. Go to vim path/kafka/config/zookeeper.properties and add <b>dataDir=/path/kafka/data/zookeeper
</b><br>.
10. Go to vim path/kafka/config/server.properties and add <b>log.dirs=/path/kafka/data/server
</b><br>.

# Create a Topic<br>

### Syntax
```sh
kafka-topics.sh --create --topic <your_topic_name> --bootstrap-server localhost:9092 --partitions <num_partitions> --replication-factor <num_replicas>
```
<br>

### Example
```sh
kafka-topics.sh --create --topic test_topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```
<br>

### Verify the Topic Creation
```sh
kafka-topics.sh --list --bootstrap-server localhost:9092
```
<br>

# Start Zookeeper

1. Go to bin dir in kafka.<br>
2. ./zookeeper-server-start.sh /path/kafka/config/zookeeper.properties [If You provide path of kafka/bin to .bashrc like above installation method , you can just hit <b>zookeeper-server-start.sh /path/kafka/config/zookeeper.properties</b> from anywhere.]<br>

# Start Kafka Server

1. Go to bin dir in kafka.<br>
2. ./kafka-server-start.sh /path/kafka/config/server.properties [If You provide path of kafka/bin to .bashrc like above installation method , you can just hit <b>kafka-server-start.sh /path/kafka/config/server.properties</b> from anywhere.]<br>