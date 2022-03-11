__author__ = 'MorganFish 1037502595@qq.com'
__doc__ = """妖王牌小学生数学口算出题程序 2022-2-22"""
from random import randint
sym = [' + ', ' - ']
fobj = open('Math.txt', 'w')
def base_exei_oneline(pmin, pmax, mmin, mmax, multimin, multimax, divmin, divmax):
	"""
pmin,pmax:加数、被加数最小最大值
mmin,mmax:减法转换成加法后，加数、被加数最小最大值
multimin,multimax:乘数、被乘数最小最大值
divmin,divmax:除法转换成乘法后，乘数、被乘数最小最大值
"""
	plus = str(randint(pmin, pmax)).rjust(2) + ' + ' + str(randint(pmin, pmax)).rjust(2) + ' ='
	minus1 = randint(mmin, mmax)
	minus2 = randint(mmin, mmax)
	minussum = minus1 + minus2
	minus = str(minussum).rjust(2) + ' - ' + str(minus1).rjust(2) + ' ='
	multi1 = randint(multimin, multimax)
	multi2 = randint(multimin, multimax)
	multi = str(multi1).rjust(2) + ' x ' + str(multi2).rjust(2) + ' ='
	div1 = randint(divmin, divmax)
	div2 = randint(divmin, divmax)
	divmulti = div1 * div2
	div = str(divmulti).rjust(2) + ' /' + str(div1).rjust(2) + ' ='
	lineitem = [plus, minus, multi, div]
	line = (18 * ' ').join(lineitem)
	print(line)
	fobj.writelines(line + '\r\n')

def base_exeicise():
	for col in range(10):
		base_exei_oneline(1, 20, 1, 50, 1, 9, 1, 9)

def type1_str(summin=1, summax=100):
	"""
summin,summax:允许总和的最小最大值
"""
	sym1 = sym[randint(0, 1)]
	sym2 = sym[randint(0, 1)]
	if sym1 == ' + ' and sym2 == ' + ':
		sum_ = randint(summin + 2, summax)
		first = randint(summin, sum_ - 2)
		second = sum_ - first
		second = randint(summin, second - 1)
		third = sum_ - first - second
	elif sym1 == ' + ' and sym2 == ' - ':
		sum_ = randint(summin + 1, summax)
		first = randint(summin, sum_ - 1)
		second = sum_ - first
		third = randint(summin, sum_)
	elif sym1 == ' - ' and sym2 == ' + ':
		first = randint(summin + 1, summax)
		second = randint(summin, first)
		third = randint(first - second, summax)
	elif sym1 == ' - ' and sym2 == ' - ':
		first = randint(summin + 2, summax)
		second = randint(summin, first)
		third = first - second
		third = randint(summin, third)
	arithmetic = str("first").rjust(2) + sym1 + str("second").rjust(2) + sym2 + str("third").rjust(2)
	print(arithmetic)
	return arithmetic

def type2_str(multimin=1, multimax=9, summin=1, summax=100):
	"""
multimin,multimax:乘数、被乘数最小最大值
summin,summax:允许总和的最小最大值
"""
	sym1 = sym[randint(0, 1)]
	second = randint(multimin, multimax)
	third = randint(multimin, multimax)
	multi = second * third
	if sym1 == ' + ':
		first = randint(summin, summax - multi)
	else:
		first = randint(multi, summax)
	arithmetic = str(first).rjust(2) + sym1 + str(second).rjust(2) + ' x ' + str(third).rjust(2)
	print(arithmetic)
	return arithmetic

def type3_str(multimin=1, multimax=9, summin=1, summax=100):
	"""
multimin,multimax:乘数、被乘数最小最大值
summin,summax:允许总和的最小最大值
"""
	sym1 = sym[randint(0, 1)]
	second = randint(multimin, multimax)
	third = randint(multimin, multimax)
	multi = second * third
	if sym1 == ' + ':
		first = randint(summin, multi)
		second = multi - first
	else:
		second = randint(summin, summax - multi)
		first = multi + second
	arithmetic = '(' + str(first).rjust(2) + sym1 + str(second).rjust(2) + ')' + ' / ' + str(third).rjust(2)
	print(arithmetic)
	return arithmetic

def oneday_homework():
	base_exeicise()
	plus1 = type1_str()
	plus2 = type1_str()
	plus3 = type2_str()
	plus4 = type3_str()
	plus5 = type3_str()
	line = [plus1, plus2, plus3]
	lines = (29 * ' ').join(line)
	print(lines)
	fobj.writelines(lines + '\r\n' * 4)
	line = [plus4, plus5]
	lines = (29 * ' ').join(line)
	print(lines)
	fobj.writelines(lines + '\r\n' * 4)
	fobj.writelines(r'用时______分钟           对______题（共45题）           家长签名：')

oneday_homework()
fobj.writelines('\r\n' * 6)
oneday_homework()
fobj.close()
