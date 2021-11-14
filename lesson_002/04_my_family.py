#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Mother', 'Father', 'Grandmother', 'Grandfather']


# список списков приблизителного роста членов вашей семьи
my_family_height = [[my_family[0], 160], [my_family[1], 180], [my_family[2], 158], [my_family[3], 175]]
    # ['имя', рост],


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(my_family_height[1][0] + '\'s height is', my_family_height[1][1], 'cm')
print('Total height of my family is', (my_family_height[0][1]
                                     + my_family_height[1][1]
                                     + my_family_height[2][1]
                                     + my_family_height[3][1]), 'cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
