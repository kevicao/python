text = """

<table> #token separted by space, always at first position
	<table>
	line inside table
	</table>. #highest level only

</table>

this is not a tabale
"""


def replace_table(text):
	List = text.split('\n')

	count = 0
	res = []
	for line in List:
		tmp = line.split(' ')
		if tmp[0] == '<table>':
			count += 1
		elif tmp[0] == '</table>':
			count -= 1
		elif count == 0:
			res.append(line)

		if tmp[0] == '</table>' and count == 0:
			res.append('[TABLE]' + tmp[1:])

	return '\n'.join(res)


text = """

today is sunny<table> this is a table #token separted by space, always at first position
	<table>
	line inside table
	</table>. #highest level only

</table>this is a table

this is not a tabale
"""


'[TABLE] this is a table'


def replace_table(text):
	table = find_table(text)

	count = 0
	res = ''
	flag = 0
	for x in table:
		if x[1] == 1:
			count += 1
			if count == 1:
				res = res + (text[flag:x[0]])
				flag = x[0]  + 7
		elif x[1] == 2:
			count -= 1
			if count == 0:
				res = res + '[TABLE]'
				flag = x[0]  + 8

	return res + text[flag:]

def find_table(string):

	table = []
	for i in range(len(string)):
		if string[i] == '<':
			if string[i:i+7] == '<table>':
				table.append((i, 1))
			elif string[i:i+8] == '</table>':
				table.append((i,2))

	return table

replace_table('today is sunny<table> this is table<table>nested table </table> </table>outside table')




# may not be separted by space