## 可以生成下载链接

import datetime
import calendar
base_url = "https://coastwatch.pfeg.noaa.gov/erddap/files/jplMURSST41mday/{}-GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc"
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)
while start_date <= end_date:
    year = start_date.year
    month = start_date.month
    _, days_in_month = calendar.monthrange(year, month)
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = (start_date + datetime.timedelta(days=days_in_month - 1)).strftime("%Y%m%d")
    url = base_url.format(f"{start_date_str}{end_date_str}")
    print(year,month)
    print(url)

    start_date = start_date.replace(day=1) + datetime.timedelta(days=days_in_month)
