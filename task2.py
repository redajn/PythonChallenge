my_file = open("text.txt", 'r', encoding='utf8')
my_string = my_file.read().split(' ')
result = ''
for i in my_string:
    if len(i) > 6:
       i = (i.title())
    result = result + i + " "
print (result)

my_file = open('result.txt', 'w+', encoding='utf8')
my_file.write(result)
my_file.close()