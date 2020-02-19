import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url) #r 响应对象
print("Status code:", r.status_code) #响应对象包含一个名为status_code的属性，它让我们知道请求是否成功了（状态码200表示请求成功）

# 将API响应存储在一个变量中
response_dict = r.json()#API返回JSON格式的信息,使用方法json()将这些信息转换为一个Python字典
print("Total repositories:", response_dict['total_count']) #GitHub总共包含多少个Python仓库

# 处理结果
#print(response_dict.keys())


# 探索有关仓库的信息
repo_dicts = response_dict['items']  #与'items'相关联的值是一个列表，其中包含很多字典，而每个字典都包含有关一个Python仓库的信息
print("Number of items:", len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Get the project description, if one is available.
    description = repo_dict['description']
    if not description:
        description = "No description provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        } #注意：最后有逗号

    # 规避 由于网络原因部分未获取到时，plot_dict 为 None，导致 chart.render_to_file('python_repos.svg') 报错
    # AttributeError: 'NoneType' object has no attribute 'decode'

    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config() #创建了一个Pygal类Config的实例
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14 #副标签（x轴上的项目名以及y轴上的大部分数字）字体大小
my_config.major_label_font_size = 18 #设置主标签（y轴上为5000整数倍的刻度）字体大小
my_config.truncate_label = 15   #truncate（被截短的）使用truncate_label将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名）
my_config.show_y_guides = False  #隐藏图表中的水平线
my_config.width = 1000 #设置了自定义宽度，让图表更充分地利用浏览器中的可用空间

chart = pygal.Bar(my_config, style=my_style)
#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False) #让标签绕x轴旋转45度（ x_label_rotation=45），并隐藏了图例（ show_legend=False），
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos3.svg')



'''
#print("Repositories returned:", len(repo_dicts))  #打印repo_dicts的长度，以获悉我们获得了多少个仓库的信息。


# 研究第一个仓库
#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict)) #打印这个字典包含的键数
#for key in sorted(repo_dict.keys()):
#    print(key)

#print("\nSelected information about first repository:")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name']) #项目的名称
    print('Owner:', repo_dict['owner']['login'])  #项目所有者是用一个字典表示的,使用键owner来访问表示所有者的字典，再使用键key来获取所有者的登录名
    print('Stars:', repo_dict['stargazers_count']) #打印项目获得了多少个星的评级
    print('Repository:', repo_dict['html_url']) #项目在GitHub仓库的URL
    print('Created:', repo_dict['created_at']) #项目创建时间
    print('Updated:', repo_dict['updated_at']) #最近一次更新时间
    print('Description:', repo_dict['description']) #打印仓库的描述
'''



