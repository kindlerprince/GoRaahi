# Web Integrated Transport Support System  
>Read the the Report.pdf file to get the clarity about the software  
It requires the multinode hadoop cluster and spark with hdfs properly
configured to  
> Also set the evironment variables in bashrc file properly  
**The user name of all the cluster must be same** _but hostnames are different_  
>Add all the hostname in /etc/hosts and and map them to their static IP's

### Prerequisites
- Java installed and Path Variables are set  
- Python3 installed
- Basic networking tools in Ubuntu like net-tools
- Hadoop Install in multinode cluster mode(say on 4 PCs)
- PySpark install in multinode cluster mode with configured with hadoop (make changes in .xml files of hadoop)
- Spark SQL also installed
- SSH key generation
- To use public key authentication, the public key must be copied to a server and installed in an authorized_keys file.  

## Install Django

#### Setting virutal environment
- Follow this link to create virtual environment [Virtual Env](
https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04)
- **Installing pip**  
`$ sudo apt-get install python3-pip`  
`$ virtualenv env`  
`env/bin/activate`  
`$ pip3 install Django`  
- **Installing selenium Web Driver**  
`$ pip3 install selenium`
- **Download ChromeDriver**  
`$ wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip`  
`$ unzip chromedriver_linux64.zip`  
You have to set this path properly in crawling
- **Installing Beautiful Soup**  
`$ pip3 install beautifulsoup4`  
- **Installing HTML parser**  
`$ pip3 install lxml`  

## Hadoop Multinode cluster Setup  
> *Note: The whole hadoop installation procedure must be done in master as well as in all slaves.*  

* **Add entries in the hosts file**  
 1. MASTER-IP master  
 2. SLAVE02-IP slave01
 3. SLAVE03-IP slave02
 4. SLAVE04-IP slave03

* **Install Java**  
 - Add repository  
`$ sudo add-apt-repository ppa:webupd8team/java`
 - update the source list  
 `$ sudo apt update`
 - Install Java  
 `$ sudo apt-get install oracle-java8-installer`
* **Confgure SSH**
 - Install open SSH server-client  
 `$ sudo apt-get install openssh-server openssh-client`  
 `$ sudo apt-get install rsync`    
 - Generate Key Pairs  
 `$ ssh-keygen -t rsa -P ""`  
 - Configure passwordless SSH  
 copy the content of .ssh/id_rsa.pub(of master) to .ssh/authorized_keys(of all the slaves as well as  master)  
 - Check by SSH to all the slaves
    1. ssh slave01
    2. ssh slave02
    3. ssh slave03  

## Install Apache Hadoop
* **Download Hadoop**  
`$ wget -c https://archive.apache.org/dist/hadoop/core/hadoop-2.6.0/hadoop-2.6.0.tar.gz`  
* **Extract the tar file**  
`$ sudo tar -zxvf hadoop-2.6.0.tar.gz`  
* **move the hadoop directory to /usr/local/hadoop**  
`$ sudo mv hadoop-2.6.0 /usr/local/hadoop`  

## bashrc Configuration
- open ~/.bashrc file and append these  
`$ vi ~/.bashrc`
### Hadoop Variables
`export JAVA_HOME=/usr/lib/jvm/java-8-oracle`  
`export HADOOP_HOME=/usr/local/hadoop`  
`export PATH=$PATH:$HADOOP_HOME/bin`  
`export PATH=$PATH:$HADOOP_HOME/sbin`  
`export HADOOP_MAPRED_HOME=$HADOOP_HOME`  
`export HADOOP_COMMON_HOME=$HADOOP_HOME`  
`export HADOOP_HDFS_HOME=$HADOOP_HOME`  
`export YARN_HOME=$HADOOP_HOME`  
`export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native`  
`export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"`  
`export LD_LIBRARY_PATH=/usr/local/hadoop/lib/`  
### SET HBASE_HOME
`export HBASE_HOME=/usr/local/hbase-1.2.2`
`export PATH=$PATH:$HBASE_HOME/bin`
### SET SPARK_HOME
`export SPARK_HOME=/usr/local/spark`
`export PATH=$PATH:$SPARK_HOME/bin`
### Default version of Python in pyspark
`export PYSPARK_PYTHON=/usr/bin/python3`

## Hadoop Configuration    
**for master and slaves files are there in repository**  
`$ cd $HADOOP_HOME/etc/hadoop`  
- **edit hadoop-env.sh**  
file is uploaded above in repository  
- **edit core-site.xml**  
file is uploaded above in repository  
- **edit hdfs-site.xml**  
file is uploaded above in repository  
- **edit mapred-site.xml**  
`$ sudo cp mapred-site.xml.template mapred-site.xml`  
file is uploaded above in repository  
- **edit yarn-site.xml**  
file is uploaded above in repository  
-  **edit salves**  
Edit configuration file slaves (located in HADOOP_HOME/etc/hadoop) and add following entries:  
`$ vi $HADOOP_HOME/etc/hadoop/slaves`
 1. slave01
 2. slave02  
 3. slave03  

## Start the Hadoop Cluster
- `$ sudo mkdir -p /usr/local/hadoop/hadoop_data/hdfs/namenode`  
- `$ sudo mkdir -p /usr/local/hadoop/hadoop_data/hdfs/datanode`  
- `$ sudo chown user:user -R /usr/local/hadoop/`  
- **format the namenode**  
`$ hdfs namenode -format`  
- **start all the daemons**   
`$ start-all.sh`

## Install Spark
- **Download Spark**   
`$ Download latest version of Spark`
- **Extract**  
`$ tar xvf spark-2.3.0-bin-hadoop2.7.tgz`  
- **Move software files**
`$ sudo mv spark-2.3.0-bin-hadoop2.7 /usr/local/spark`

> *Note: The whole spark installation procedure must be done in master as well as in all slaves.*  

## Spark Master Configuration
Do the following procedures only in master.  
- **Edit spark-env.sh**  
Move to spark conf folder and create a copy of template of spark-env.sh and rename it.

    `$ cd /usr/local/spark/conf`  
    `$ cp spark-env.sh.template spark-env.sh`  
Now edit the configuration file spark-env.sh.  
`$ sudo vim spark-env.sh`  
And set the following parameters.  
`export SPARK_MASTER_HOST='<MASTER-IP>'`  
`export JAVA_HOME=<Path_of_JAVA_installation>`  
- **Add Workers**  
Edit the configuration file slaves in (/usr/local/spark/conf).  
    `$ sudo vim slaves`  
And add the following entries.
    1. master
    2. slave01
    3. slave02
    4. slave03

## Start Spark Cluster
- To start the spark cluster, run the following command on master.

    `$ /usr/local/spark/sbin/start-all.sh`

- To stop the spark cluster, run the following command on master.  
    `$ /usr/local/spark/sbin/stop-all.sh`  
