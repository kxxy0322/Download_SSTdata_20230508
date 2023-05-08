# Download_SSTdata_20230508
这个代码可以用来下载全球的海表温度的数据。This code can be used to download global sea surface temperature data.

## 数据网址
https://coastwatch.pfeg.noaa.gov/erddap/files/
https://coastwatch.pfeg.noaa.gov/erddap/files/jplMURSST41mday/

## 数据说明
精度为0.01度
数据时间是2002年至今
月数据

## 代码功能
1、可以自定义开始和结束时间，注意开始时间为需要下载的月份的1号，结束时间为结束月份的最后一天。
2、添加延迟，防止被识别成爬虫

## 注意事项
1、需要翻
2、网址不稳定，会出现某些月份漏下载的情况，可以配合link.py文件进行补充。
3、link.py是直接生成下载链接的代码，复制下载链接到网页可以直接下载文件。
