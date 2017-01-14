import codecs
f = codecs.open('C:\\Users\\arahansa\\PycharmProjects\\untitled\\st_basic\\07_파일읽기\\buy_list.txt', 'r', "utf-8")

lines = f.readlines()

for line in lines :
    print(line, end="")

#nline = line.split('\n')[0]
#print(nline)