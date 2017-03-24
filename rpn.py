#!/usr/bin/env python3

import operator
import timeit

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,

}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		start = timeit.default_timer()
		result = calculate(input('rpn calc> '))
		print("Result:", result)
		end = timeit.default_timer()
		print("This calculation took: ", end - start)

if __name__ == '__main__':
	main()
