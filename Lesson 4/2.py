#!/usr/bin/python3

d = dict()
d['Black'] = (0, 0, 0)
d['Silver'] = (192, 192, 192)
d['White'] = (255, 255, 255)
d['Fuchsia'] = (255, 0, 255)
d['Purple'] = (128, 0, 128)
d['Red'] = (255, 0, 0)
d['Maroon'] = (128, 0, 0)
d['Yellow'] = (255,255,0)
d['Orange'] = (255,165,0)
d['Olive'] = (128, 128, 0)
d['Lime'] = (0, 255, 0)
d['Green'] = (0, 128, 0)
d['Aqua'] = (0,255,255)
d['Teal'] = (0, 128, 128)
d['Blue'] = (0,0,255)
d['Navy'] = (0, 0, 128)

print('Основные цвета:')
for key, value in d.items():
    print(key, ':', value)