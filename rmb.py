# coding=utf-8

"""
注意：由于中文乱码问题，输出时请先decode("utf8")，例如你要输出ans = "零圆", print ans.decode("utf8").
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示
"""


a = 123456
number = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
digit = ['圆','拾','佰','仟','万']
money = []


def convert(a):
	a = str(a)
	length = len(a)
	if a[0] == '-':
		money.append('')
		a = a[1:]
		length -= 1
	for i, j in enumerate(a):
		if length - 5 - i > 0:
			money.append(number[int(j)])
			money.append(digit[length - 5 - i])
		elif length == 0:
			money.append('')
		else:
			money.append(number[int(j)])
			money.append(digit[length - 1 - i])
	return money


print ''.join(convert(a)).decode('utf8')
