# Example to execute fab function from a file list. Firts, read pass the function read_hosts to read the file and after pass the function that you want to execute

cat servers-centos7.txt |fab read_hosts restart_apache -P
