#!/bin/bash

nmap -sT -sV -sO <addr> -p 3306, > /dev/null -oG MySqlScan

cat MySqlScan | grep open > MySqlScan2

cat MySqlScan2

