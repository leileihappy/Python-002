#! /bin/sh

# 在crontab -e中添加此脚本
# 执行抓取脚本
scrapy crawl zdmtop
# 执行分析脚本
python3 rowdata.py
