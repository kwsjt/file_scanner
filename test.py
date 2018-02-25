import os
import sys
import getpass

def size_of(num, suffix='B'):
    for unit in ['','K','M','G','T']:
        if abs(num) < 1000.0:
            return "%3.1f%s%s" % (num, " " + unit, suffix)
        num /= 1000.0

def scan(d):
	top_10 = []
	i = 0
	for root, dirs, files in os.walk(d, topdown=False):
   		for name in files:
   			try:
   				file_size = os.path.getsize(os.path.join(root, name))
   				top_10.append((file_size, name))
				top_10.sort(reverse = True)
				while len(top_10) > 10:
					top_10.pop()
			except OSError:
				pass

	fi = open("biggest_file.txt", "w+")

	print "Top 10 Files in", d
	
	for index, i in enumerate(top_10, 1):
		fi.write("{}.\t{} -> {}\n\n".format(index, i[1], size_of(i[0])))
		print i[1], "->", size_of(i[0])
	fi.close()

def main():
	s = "/media/" + getpass.getuser()
	lis = ["/home"]
	lis.append(os.listdir(s))
	print lis
	inp = raw_input()
	if inp == '/home':
		scan('/home')
	else:
		d = os.path.join(s, inp)
		scan(d)


if __name__=="__main__":
	main()