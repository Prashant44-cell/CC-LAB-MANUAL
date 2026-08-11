# Experiment 7: Install Hadoop Single Node Cluster & Run WordCount

## Aim:
To find the procedure to set up the one node Hadoop cluster and run simple applications like wordcount.

## Steps:
1. Install Java JDK and SSH Server.
2. Download and extract `hadoop-2.7.0.tar.gz`.
3. Configure `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml`, `mapred-site.xml`.
4. Format HDFS Namenode (`hdfs namenode -format`).
5. Start HDFS and YARN daemons (`start-dfs.sh`, `start-yarn.sh`).
6. Compile `WordCount.java` and execute MapReduce job on HDFS cluster.
