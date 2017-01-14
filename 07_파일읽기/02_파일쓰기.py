import codecs

# 일반
# f = open('c:\\Users\\Jason\\Desktop\\sel_list.txt', 'wt')

f = codecs.open('C:\\Users\\arahansa\\PycharmProjects\\untitled\\st_basic\\07_파일읽기\\sel_list.txt', 'w', "utf-8")

f.write('삼성전자\n')
f.write('SK하이닉스\n')
f.close()

print("Complete")