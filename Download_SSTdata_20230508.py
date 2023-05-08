import datetime
import urllib.request
import calendar
import os
import random
import time

base_url = "https://coastwatch.pfeg.noaa.gov/erddap/files/jplMURSST41mday/{}-GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc"
save_dir = "D:/SST"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

start_date = datetime.date(2021, 4, 1)
end_date = datetime.date(2021, 12, 31)

while start_date <= end_date:
    year = start_date.year
    month = start_date.month
    _, days_in_month = calendar.monthrange(year, month)
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = (start_date + datetime.timedelta(days=days_in_month - 1)).strftime("%Y%m%d")
    url = base_url.format(f"{start_date_str}{end_date_str}")
    print(url)
    filename = f"{year}_{month}.nc"
    save_path = os.path.join(save_dir, filename)  # 修改文件保存路径

    print(f"正在下载 {filename} ...")

    try:
        urllib.request.urlretrieve(url, save_path)
    except urllib.error.URLError as e:
        print(f"下载出错：{e.reason}")
        continue

    delay_time = random.uniform(6, 12)
    # 延迟一段时间，避免请求过于频繁导致被封禁IP
    time.sleep(delay_time)

    start_date = start_date.replace(day=1) + datetime.timedelta(days=days_in_month)
