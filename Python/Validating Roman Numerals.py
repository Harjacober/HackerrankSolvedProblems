thousand = '(M{0,3})'
hundred = '(C[MD]|D?(C{0,3}))'
ten = '(|X?L|L?(X{0,3})|XC)'
digit = '(I?V|V?(I{0,3})|IX)'
regex_pattern = r'({}{}{}{}$)'.format(thousand,hundred,ten,digit)	# Do not delete 'r'.

