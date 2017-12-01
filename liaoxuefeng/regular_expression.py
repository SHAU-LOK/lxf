
import re

# \s 匹配一个空格(或者Tab)
# \d{3,8} 3-8个数字
# [0-9a-zA-Z\_] 匹配一个数字，字母或者下划线

if __name__ == '__main__':
    # 是否匹配
    print(re.match(r'^\d{3}-\d{3,8}$', '010-39489'))
    # >>> True

    # 切分字符串
    print(re.split(r'\s+', 'a b  c'))
    # >>> ['a', 'b', 'c']
    print(re.split(r'[\s\,]+', 'a,b, c   d'))
    # >>> ['a', 'b', 'c', 'd']

    # 分组 group(0)原始字符串, group(1),group(2)...表示第1,2个子串
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print(bool(m))
    # >>> True
    print(m.group(0))
    # >>> '010-12345'
    print(m.group(1))
    # >>> '010'
    print(m.group(2))
    # >>> '12345'

    # 贪婪匹配
    print(re.match(r'^(\d+)(0*)$', '102333000').groups())
    # >>> ('102333000', '')
    # 必须采用非贪婪匹配
    print(re.match(r'^(\d+?)(0*)$', '1023000').groups())
    # >>> ('1023', '000')
    



