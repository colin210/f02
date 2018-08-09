import json
import pickle

yuanzu = ('y1', 'y1', 'y2','y3')
liebiao = ['LL1', 'L2', 'L3']
zidian = {'D1': 'D1info',
          'D2': 'D2info'
          }
# g = lambda x: x*2
# print(g(2))
# g1 = lambda x, v: x*v
# print(g1(2,3))

# l1 = [1, 3, 5]
# l2 = [2, 4, 6]
# for a, b in zip(l1, l2):
#     print(a, b)

#字典遍历
# for k, v  in zidian.items():
#     print(k , v)
#
# for k in zidian:
#     print(k, zidian[k])
#
# for v in zidian.values():
#     print(v)

# if 'D11' in zidian:
#     zidian['D11']='D1old'
# else:
#     zidian['D11']='D1new'
#
# print(zidian['D11'])



# 列表操作方式
# 增删改遍历
# liebiao.append('L4')
# liebiao.remove('L2')
# liebiao[0] = 'LLLL0'
#
# for i in liebiao:
#     print(i, len(i))
# for i in range(len(liebiao)):
#     print(liebiao[i])
# print(max(liebiao))
# # 元祖转列表
# yuanzutolist = list(yuanzu)
# print(yuanzutolist)
# print(liebiao[0])





# 元祖操作方式
#两种遍历
# for i in yuanzu:
#     print(i)
#
# for i in range(len(yuanzu)):
#     print(yuanzu[i])
# 个数
# print(yuanzu.count('y1'))
# 由元素找位置
# print(yuanzu.index('y1'))
# 由位置找元素
# print(yuanzu[2])


#JSON只能处理基本数据类型。pickle能处理所有Python的数据类型。
#JSON用于各种语言之间的字符转换。pickle用于Python程序对象的持久化或者Python程序间对象网络传输，
# dumps 对象     dump到文件

# jy = json.dumps(yuanzu)
# print(json.loads(jy))
# print(jy)
#
# with open(r'a.txt', 'w+') as f:
#     json.dump(yuanzu, f)
#
# with open(r'a.txt', 'r') as f:
#     print(json.load(f))


