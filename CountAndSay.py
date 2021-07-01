def countAndSay(n):
	if n == 1:
		return '1'
	result = ''
	s = countAndSay(n - 1)

	last_digit = s[0]
	digit_num = 1
	for c in s[1:]:
		if c == last_digit:
			digit_num += 1
		else:
			result += (str(digit_num) + last_digit)
			last_digit = c
			digit_num = 1
	result += (str(digit_num) + last_digit)
	return result
