# file_name=open("file_name.txt", "r+")# r or r+ or a or w or a for append and x for create
# print(file_name.readable())
# print(file_name.read())
# print(file_name.readline())
# print(file_name.readline())
# print(file_name.readlines()[2])
# for line in file_name:
#         print(line)
# print(file_name.writable())
# file_name.write("I am an Engineer")
# print(file_name.readlines())
# file_name.close()
import csv
my_file = open("file1.txt", "w")
my_file.write("Hello World")
my_file.close()


with open("ex.csv", 'a') as file:
    writer = csv.writer(file)
    reader = csv.reader(file)
    line = "hello world"
    writer.writerow((line,))
