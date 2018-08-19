s = ''' this is a string
that spans
multiple lines'''
print('\n line')  # newline followed by "line"
print(r'\n line') # avoid escape character substitution

s = "Python"
print(s[2])  # print third character of string s
print(s + str(123))  # concatenate s with "123"
print(s.replace('P', 'p'))  # replace 'P' in s with 'p'

# Example: formatting using the format method
import math
print('Formatting in {} is simple and powerful'.format('Python'))
print('Refer to {1} by {0}'.format('index', 'fields'))
print('Use {name} too'.format(name='keyword arguments'))
print('Rounding: pi = {:.3}'.format(math.pi))
print('Attributes: pi = {0.pi:.3}'.format(math))
print('And {0[1][0]} more!'.format(['so', ['much', ['more']]]))

# Example: formatting using the % operator
value = '%'
print('Formatting using the %s operator is error-prone.' % value)
print('Values must be specified %s %s.' % ('in', 'order'))
value = ('a', 'tuple')
# Wrap value as (value,); otherwise we get a TypeError
print('If a value is %s, things get complicated!' % (value,))
value = {'data': 'dictionary'}
print('Using a %(data)s key works though.' % value)
print('Rounding: pi = %.3f and e = %.3f.' % (math.pi, math.e))
print('%% has to be escaped when formatting.' % ())

# Example: formatting using the Template class
from math import pi
from string import Template as T # aliased for brevity

print(T('$id work').substitute(id='Keyword arguments'))
print(T('$id works too').substitute({'id': 'A dictionary'}))
print(T('Note the ${id}').substitute(id='differences'))
print(T('pi = ${id}').substitute(id=pi))
print(T('$$ has to be escaped').substitute())

# Example: formatting using literal string interpolation
value = 'string interpolation'
print(f'The use of {value} is awesome!') # more readable
print(f"Another PI example: pi = {pi:.3f}")
