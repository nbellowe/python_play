import os,re,json
dir= 'C:/Users/Nathan/study/'
def check_(words,search):
	for word in words:
		if any(word in searchitem for searchitem in search):
			return True
	return False

def test(filename,search): #iterates through file
	sep='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	print filename, 'parsed'
	temp =[]
	with open(filename,'r') as f:
		print 'chr', len(open(filename,'r').read())
		missed=0
		found=0
		for line in f:
			words = line.strip().lower().split()
			if check_(words,search):
				temp.append(line)
				found+=1
			else:
				missed+=1
	print 'found',found
	print 'missed',missed
	print sep
	return temp
def go(dir=dir):
	search = open(dir+'terms').readlines() #array of lines
	search = [x.strip().lower() for x in search]
	search.append('christian')
	#print search
	ls = dict() #global ls
	for root, dirs, files in os.walk(dir): #walk directory recursively
	    for f in files:
	        fullpath = os.path.join(root, f)
	        if os.path.splitext(fullpath)[1] == '.txt':
	            ls[fullpath] =test(fullpath,search)
	final = []
	for key,file in ls.iteritems():
		print key, '~----~', len(file)
		linenumber=0
		for line in file:
			linenumber=linenumber+1
			date = ''
			for x in line:
				if x.isdigit():
					date+=x
					continue
				else:
					if x is '-' and len(date) is 0:
						date+=x
					else:
						break
			if date == '':
				continue
			final.append(['DATE: ', date, '\t\tLINE: ', line.strip(), '\n'])
	#print final
	t = sorted(final, key=lambda x: int(x[1]))
	f=open(dir+'out','wb')
	for line in t:
		f.write(''.join(line))

if __name__ == '__main__':
	go()



