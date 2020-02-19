
import csv
from matplotlib import  pyplot as plt
from datetime import  datetime

filename = 'sitka_weather_07-2014.csv'
#with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。
with open(filename) as f:
    reader = csv.reader(f)  #创建一个与该文件相关联的阅读器（ reader）对象
    #reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
    header_row = next(reader) #next(reader)返回文件中的下一行,这里只是得到了头文件
#    print(header_row)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1]) #将字符类型转化为int类型
        highs.append(high)
    print(highs)


#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

#绘制图形格式
plt.title("Daliy high temperatures, July 2014", fontsize = 24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  #调用了fig.autofmt_xdate()来绘制斜的日期标签，
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



#enumerate()来获取每个元素的索引及其值
#for index, column_header in enumerate(header_row):
#   print(index, column_header)