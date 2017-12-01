from label import create_label
from extract import Extractor
#from dataStore import insert_into_db

test_doc = ['travel-nontravel/tr2.txt']
list_of_label = create_label(test_doc)
size_of_test_doc = len(test_doc)
extractor = Extractor()
for index in range(size_of_test_doc):
	if list_of_label[index]==1:
		path = test_doc[index]
		extractor.setPath(path)
		user_name = extractor.findUserName()#emailid
		date = extractor.findDate()
		time = extractor.findTime()
		address = extractor.findAddress()	
		print date
		print time
		print address

		#insert_into_db(user_name,date,time,address) 
