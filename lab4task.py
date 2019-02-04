#task1
import string

fp=open('emma.txt')
name=fp.read()
for line in name.split():
	word=line.strip(string.punctuation)
	print(word.lower())
#task2
import string

fp=open('mybook.txt')
name=fp.read()

def print_book():
	count=0
	mydict=dict()
	for line in name.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		print(myword)	
		count=count+1
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1

	print('The total no of words in the book is:',count)
	print(mydict)
	print('The different no of words in the book is:',len(mydict))

print_book()

#task3
import string

fp=open('mybook.txt')
name=fp.read()

def print_book():
	count=0
	mydict=dict()
	for line in name.split():
		word=line.strip(string.punctuation)
		myword=word.lower()
		print(myword)	
		count=count+1
		if myword not in mydict:
			mydict[myword]=1
		else:
			mydict[myword]+=1

	print('The total no of words in the book is:',count)
	print(mydict)
	print('The different no of words in the book is:',len(mydict))
	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))
	mylist.sort(reverse=True)
	print(mylist)
	for freq,word in mylist[:20]:
		print(word,freq,sep='\t')


print_book()
#task4
import string

fp=open('emma.txt')
name=fp.read()
fp1=open('words.txt')
name1=fp1.read()

def print_book(book):
	mydict=dict()
	for line in book.split():
		word=line.strip(string.punctuation)
		if word not in mydict:
			mydict[word]=1
		else:
			mydict[word]+=1
	return mydict


def subtract(d1,d2):
        res=dict()
        for key in d1:
                if key not in d2:
                        res[key]=None
        return res

hist=print_book(name)
words=print_book(name1)
diff=subtract(hist,words)

print('The words in book that is not in words file are:')
for word in diff:
	print(word,sep='\n')













#	print('The different no of words in the book is:',len(mydict))
"""	mylist=[]
	for key,value in mydict.items():
		mylist.append((value,key))
	mylist.sort(reverse=True)
	print(mylist)
	for freq,word in mylist[:20]:
		print(word,freq,sep='\t') """
#task6
import os

def print_file(dir):
        for path in os.listdir():
                if os.path.isfile(path):
                        print(path)
print_file('.')



def print_dir(dirname):
        for name in os.listdir(dirname):
                path = os.path.join(dirname,name)
                if os.path.isfile(path):
                        print(path)
                else:
                        walk(path)
print_dir('.')




#task7
def sed(pattern,replace,filein,fileout):
        try:
                fin=open(filein,'r')
                fout=open(fileout,'w')
        except:
                print('sorry something went wrong!')

        for line in fin:
                line=line.replace(pattern,replace)
                fout.write(line)
        fin.close()
        fout.close()

pattern='pattern'
replace='replace'

filein='testfile.txt'
fileout=filein+'.replaced'

sed(pattern,replace,filein,fileout)




