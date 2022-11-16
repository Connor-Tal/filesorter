fileName = 'test.txt'
character = input('what character marks the end of a line?')
with open(fileName, 'r') as file:
        data = file.read()
        data = data.replace('\n', '')
        data = data.replace('.', '.\n')

with open(fileName, 'w') as file:
        file.write(' ')
        file.write(data)
        file.close()