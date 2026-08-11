#!/bin/bash
# Install Hadoop single node cluster and run WordCount MapReduce application

# Step 1: Install OpenJDK 7/8
sudo apt-get update
sudo apt-get install -y openjdk-7-jdk openjdk-7-jre

# Step 2: Configure SSH
sudo apt-get install -y openssh-server
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Step 3: Extract Hadoop Tar
sudo tar -xzvf hadoop-2.7.0.tar.gz -C /usr/local/lib/
sudo chown -R hadoop:hadoop /usr/local/lib/hadoop-2.7.0

# Step 4: Setup Environment Variables
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export HADOOP_INSTALL=/usr/local/lib/hadoop-2.7.0
export PATH=$PATH:$HADOOP_INSTALL/bin:$HADOOP_INSTALL/sbin

# Step 5: Format Namenode and Start Services
hdfs namenode -format
start-dfs.sh
start-yarn.sh
jps

# Step 6: Compile and Run WordCount
bin/hadoop com.sun.tools.javac.Main WordCount.java
jar cf wc.jar WordCount*.class
bin/hadoop jar wc.jar WordCount /user/joe/wordcount/input /user/joe/wordcount/output
bin/hadoop fs -cat /user/joe/wordcount/output/part-r-00000
