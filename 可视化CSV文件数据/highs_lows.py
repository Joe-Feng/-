import csv
from matplotlib import  pyplot as plt
from datetime import  datetime

filename = 'sitka_weather_2014.csv'
#with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。
with open(filename) as f:
    reader = csv.reader(f)  #创建一个与该文件相关联的阅读器（ reader）对象
    #reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
    header_row = next(reader) #next(reader)返回文件中的下一行,这里只是得到了头文件
#    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1]) #将字符类型转化为int类型
        highs.append(high)

        low = int(row[3])
        lows.append(low)
    print(highs)


#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
#有几个y轴图像，要写几行plt.plot()
#alpha指定颜色的透明度。 Alpha值为0表示完全透明， 1（默认设置）表示完全不透明。
plt.plot(dates, highs, c='red', alpha = 0.5)
plt.plot(dates, lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
#向fill_between()传递了一个x值系列： 列表dates，还传递了两个y值系列： highs和lows。
# 实参facecolor指定了填充区域的颜色，
# 我们还将alpha设置成了较小的值0.1，让填充区域将两个数据系列连接起来的同时不分散观察者的注意力。


#绘制图形格式
plt.title("Daliy high and low temperatures - 2014", fontsize = 24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  #调用了fig.autofmt_xdate()来绘制斜的日期标签，
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



#enumerate()来获取每个元素的索引及其值
#for index, column_header in enumerate(header_row):
#   print(index, column_header)