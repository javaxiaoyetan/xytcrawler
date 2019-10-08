> 软件环境

python 2.7 + scrapy 1.7.3 

> 爬虫对象 

中国天气网  http://www.weather.com.cn

> 数据项

```
// 执行该建表语句
CREATE TABLE `weather` (
  `weather_date` date DEFAULT NULL COMMENT '天气时间',
  `province` varchar(30) DEFAULT NULL COMMENT '省',
  `city` varchar(30) DEFAULT NULL COMMENT '城市',
  `day` varchar(20) DEFAULT NULL COMMENT '白天天气',
  `day_temperature` varchar(30) DEFAULT NULL COMMENT '白天气温',
  `night` varchar(20) DEFAULT NULL COMMENT '晚上天气',
  `night_temperature` varchar(20) DEFAULT NULL COMMENT '晚上气温',
  `sunrise` varchar(20) DEFAULT NULL COMMENT '日出',
  `sunset` varchar(20) DEFAULT NULL COMMENT '日落时间',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

```


> 备注

scrapy 入门项目 

爬取荆州、盐城、上海、北京四个地方的天气,持久化mysql数据库.

> 执行

scrapy crawl weather