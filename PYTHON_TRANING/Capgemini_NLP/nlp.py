import csv
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import wordnet
from macpath import split
from nltk.internals import ReadError
lmtzr = WordNetLemmatizer()
import re
import datetime
import pprint
data={}
deal={}

stopwords=[]

###############################################################################################(reading files)

stopwords=[]
with open('mystopwords.csv','rt') as fp:
	reader = csv.reader(fp)
	for line in reader:
		stopwords+=line
	#print (stopwords)
		
con={}
with open('contraction.csv','rt') as fp:
	reader=csv.reader(fp)
	next(reader)
	for line in reader:
		con[line[0].lstrip()]=line[1].lstrip()
	#print (con)
################################################################################################

#####################################################(tree navigation)

def tree_travel_1(tree_obj_1,tree_data_1,stopwords):
	for e in list(tree_obj_1):
		if isinstance(e,nltk.tree.Tree):
			return tree_travel_1(e,tree_data_1,stopwords)
		else:
			if e[0] not in stopwords:
				tree_data_1+=[e[0]]	
				
############################################

def tree_travel(tree_obj,tree_data,stopwords,final_data_person):

	for e in list(tree_obj):
		#print(e[0])
		if isinstance(e,nltk.tree.Tree):
			return tree_travel(e,tree_data,stopwords,final_data_person)
		else:
			if e[0] not in stopwords:
				tree_data+=[e[0]]
				
###############################################################################################(date removal)

month_new=[datetime.datetime.strptime(str(i),'%m').strftime('%b') for i in range(1,13)]
#print (month_new)
month=[datetime.datetime.strptime(str(i),'%m').strftime('%B') for i in range(1,13)]
day=[datetime.datetime.strptime(str(i),'%m').strftime('%A') for i in range(1,8)]
all_month_day=[]
for temp in day:
	for temp1 in month:
		all_month_day+=[temp+', '+temp1]
	
#print (all_month_day)
################################################################################################

output_phrase={}
final_string={}
noun_phrases={}
verb_phrases={}
person={}
final_data_person=[]
final_data={}
final_data_different=[]
count = 1
with open(r'C:\PythonWorkSpace\NLP\service.csv','rt') as fp:
	reader = csv.reader(fp)
	for line in reader:
		#print (line)
		#inc_data = line.split(',')
		key1 = line[0]
		data[key1] =[line[1]]
		deal[key1]=line[-1]

		data_new=[]
		for temp in data[key1]:
			#print (temp)
			data_new+=[t.strip() for t in re.split('Subject|Status Note|Work Log|-{4,}|_{4,}|={4,}',temp)]
	
		data_new1=[]
		#print (data_new)
		for temp in data_new:
			a=re.sub('-{4,}|_{4,}|={4,}',' ',temp)
	
			for temp1 in all_month_day:
				if temp1 in a:
					a = re.sub(temp1+' [0-9]+',' ',a)
			
			for temp1 in month_new:
				if temp1 in a:
					a = re.sub(temp1+' +[0-9]+, +[0-9]+',' ',a)
					a = re.sub(temp1+' [0-9]+',' ',a)

		########################################################################(removing signatures and from to etc)
			a=re.sub(r'From:[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Thank you,[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Thank you.[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Thank you [\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Thanks,[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Thanks.[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Thanks [\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Regards,[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Regards.[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Regards [\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Best Regards,[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Best Regards.[\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Best Regards [\s\w\W]+[:]*',' ',a,flags=re.I)

			a=re.sub(r'Hello[\s\w]+[,],',' ',a,flags=re.I)

			#a=re.sub(r'Hello[\s\w\W]+.',' ',a)
			a=re.sub(r'Hello[\s\w]+-',' ',a,flags=re.I)

			a=re.sub(r'hello[\s\w]+[,]',' ',a,flags=re.I)

			#a=re.sub(r'hello[\s\w\W]+.',' ',a)
			a=re.sub(r'hello[\s\w]+-',' ',a,flags=re.I)

			
			#a=re.sub(r'Hi[\s\w\W]+,',' ',a)
			#a=re.sub(r'Hi[\s\w\W]+.',' ',a)
			a=re.sub(r'Hi[\s\w]+-',' ',a,flags=re.I)
			a=re.sub(r'hi[\s\w]+[,]',' ',a,flags=re.I)

			
			#a=re.sub(r'hi[\s\w\W]+,',' ',a)
			#a=re.sub(r'hi[\s\w]+-',' ',a,re.I)
			#print(a)
			#print("2121212121212121212121212121221")
	#############################################################(time removal)
	
			a=re.sub(r'[0-9]+:[0-9]+ AM',' ',a,re.I)
			a=re.sub(r'[0-9]+:[0-9]+ PM',' ',a,re.I)
			
	#############################################################(email removal)
	
			a=re.sub(r'[\w\.-_0-9]+@[\w\.-]+',' ',a)
			
	#########################################################################(city_state_zip removal)	
	
			a=re.sub(r'[a-zA-Z]+, [a-zA-Z]{2} - ([0-9]{5} | [0-9]{9})',' ',a)
			
	#########################################################################(phonenumber removal)
			
			a=re.sub(r'[0-9]+-[0-9]+-[0-9]+',' ',a)
			a=re.sub(r'([0-9]+) [0-9]+-[0-9]+',' ',a)
			
			a=re.sub(r'[0-9]+-[0-9]+',' ',a)
			a=re.sub(r'[0-9]+.[0-9]+.[0-9]+',' ',a)
			
	############################################################################(url removal)
	
			a=re.sub(r'^https?:\/\/.*[\r\n]*', ' ', a, flags=re.MULTILINE)
			a=re.sub(r'^http?:\/\/.*[\r\n]*', ' ', a, flags=re.MULTILINE)
			
	############################################################################(numbers removal)
	
			a=re.sub('(^| )([0-9]+)( |$)',' ',a)
			
	#######################################################################################(special characters removal)
	
			a=re.sub(r'[^a-zA-Z0-9"_"," "-]',' ', a)
			
	#######################################################################################(extra white spaces removal)		
	
			a=re.sub(r' +',' ',a)
			
			data_new1+=[a]
		
		#print (data_new1)
	########################################################################################(removing title name)
	
		data_new5=[]
		pattern=['Dr.','Mr.','Mrs.','Ms.']
		for temp in data_new1:
			for temp1 in pattern:
				if temp1 in temp:
					temp = re.sub(temp1+' [a-zA-Z0-9]+',' ',temp)
			
			data_new5+=[temp]
		#print (data_new5)		
		
		data_new6=[]
		for temp in data_new5:
			data_new6+=[re.sub(r' [0-9]+ ',' ',temp)]
		#print (data_new6)
		
		data_new7=[]
		for temp in data_new6:
			data_new7+=[re.sub(r' +',' ',temp)]
	
	#################################################################(working on abber and con) 
		#print (data_new7)
		data_new3=[]
		for temp in data_new7:
			for key in con:
				temp=re.sub('\\b'+key+'\\b',con[key],temp)
			data_new3+=[temp]
		#print (data_new3)
	##################################################################(comma spacer)
	
		data_new4=[]
		for temp in data_new3:
			strtemp=''
			for temp1 in temp.split(','):
				strtemp+=temp1+', '
			data_new4+=[strtemp]	
		#print (data_new4)
		#################################################
		
		
		temp_string=''.join(data_new4)
		final_string[key1]=temp_string
	
		#print (final_string)
	#####################################################(tokenization and part of speech tagging)
	
		sents = sent_tokenize(temp_string)
		tokens = word_tokenize(temp_string)
		#print (str(sents))
		#print (str(tokens))
		tagged_sent = pos_tag(tokens)
		
		
		#print (str(tagged_sent))
		
		def get_wordnet_pos(pos_tag):
			if pos_tag[1].startswith('J'):
				#return (pos_tag[0], wordnet.ADJ)
				return (pos_tag[0], "ADJ")
			elif pos_tag[1].startswith('V'):
				#return (pos_tag[0], wordnet.VERB)
				return (pos_tag[0], 'VERB')
			elif pos_tag[1].startswith('N'):
				return (pos_tag[0], wordnet.NOUN)
				#return (pos_tag[0], 'NOUN')
			elif pos_tag[1].startswith('R'):
				#return (pos_tag[0], wordnet.ADV)
				return (pos_tag[0], 'ADV')
			else:
				return (pos_tag[0], wordnet.NOUN)
				#return (pos_tag[0], 'NOUN')
	
		lemma=[]
		for t in tagged_sent:
			try:
				lemma+=[(lmtzr.lemmatize(t[0],get_wordnet_pos[t[1][:2]]))]
				
			except:
				lemma+=[(lmtzr.lemmatize(t[0]))]		
		#print (str(lemma))
		tagged_sent_lemma=pos_tag(lemma)
		#print (tagged_sent_lemma)
		tagged_sent_new=nltk.ne_chunk(tagged_sent_lemma)
		
		#print (str(tagged_sent_new))
	#######################################################################(defining grammar)
	
		tagged = tagged_sent_new
	
		grammar = r"""
		NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
		PP: {<IN><NP>}               # Chunk prepositions followed by NP
		VP: {<VB.*><NP|PP>+} # Chunk verbs and their arguments
		CLAUSE: {<NP><VP>}           # Chunk NP, VP
	  	"""
		
	#######################################################################(Regular expression based Parsing)
	
		cp = nltk.RegexpParser(grammar)
		
	#######################################################################(output parse tree)
	
		result = cp.parse(tagged)
		
		output_phrase[key1]=result
	
		#print (result)
	###############################################################
	
		temp_list=[]
		for subtree in result.subtrees():
			if subtree.label()=='PERSON':
				tree_data_1=[]
				tree_travel_1(subtree,tree_data_1,stopwords)
				temp_list+=[' '.join((e for e in list(tree_data_1)))]
		
		person[key1]=temp_list
		#print (person)
	#################################################################
	
		for t in person[key1]:
			#print(t)
			if len(t)>0:
				final_data_person+=[[t]]
		#print (final_data_person)	
	#################################################################print("\n# Print noun phrases only")
	
		temp_list=[]
		for subtree in result.subtrees():
			if subtree.label()=='NP':
				tree_data=[]
				tree_travel(subtree,tree_data,stopwords,final_data_person)
				temp_list+=[' '.join((e for e in list(tree_data)))]
		
		noun_phrases[key1]=temp_list
	
	###############################################################print("\n# Print verb phrases only")
	
		temp_list=[]
		for subtree in result.subtrees():
			if subtree.label()=='VP':
				tree_data=[]
				tree_travel(subtree,tree_data,stopwords,final_data_person)
				temp_list+=[' '.join((e for e in list(tree_data)))]
	
	
		verb_phrases[key1]=temp_list
		
	##############################################################################################################################	
		key2 = str(count) + '_' + str(key1)
		test = []
		for t in noun_phrases[key1]:
			if len(t)>0:
				test+=[[t]]
				final_data[count] = test
		for t in verb_phrases[key1]:
			if len(t)>0:
				test+=[[t]]
				final_data[count] = test
				#final_data+=[[t]]
		
		#return(final_data)
		count += 1
	print (final_data)
