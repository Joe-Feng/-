import json
import pygal.maps.world  #注意这里已经不是书上的pygal了
from pygal.style import RotateStyle as rs, LightColorizedStyle as lcs
from country_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f) # pop_data为列表形式，列表中每个元素为字典

#打印每个国家2010年的人口数量
cc_populations = {} #创建一个包含人口数量的字典
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population =int(float(pop_dict['Value']))
        #Python不能直接将包含小数点的字符串'1127437398.85751'转换为整数
        #为消除这种错误，我们先将字符串转换为浮点数，再将浮点数转换为整数：
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
            #print(code + ": " + str(population))
        #else:
         #   print('ERROR - ' + country_name)


# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = rs('#336699', base_style=lcs)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population2.svg')


