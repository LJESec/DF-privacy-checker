#!/usr/bin/env python
# -*- encoding: utf8 -*-
#
import SimpleHTTPServer
import SocketServer


import csv
import locale
import math
import threading
import time
from csv import reader
#locale.setlocale(locale.LC_ALL, 'en_US.utf8')
#locale.setlocale(locale.LC_ALL, 'de_DE')

csv.field_size_limit(100000000)

f= open("entfiles_raw_BE_transformed.csv","w+")

f3= open("entfiles_test_data_transformed.csv","w+")

foutput= open("heatmap_file_comparison.csv","w+")

#thx https://stackoverflow.com/questions/18424228/cosine-similarity-between-2-number-lists
def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    returnvalue = 0
    denominator = 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    denominator = math.sqrt(sumxx*sumyy)
    if (denominator == 0):
        returnvalue = 0
    else:
        returnvalue = sumxy/math.sqrt(sumxx*sumyy)
    return returnvalue

	
	
	
	
	
	
	
	
###
###
###
###
###
###
###
###
###
###
###
# read csv file as a list of lists
with open('entfiles_raw_BE.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj)
	
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    
    i = 0# 
	
    col_filname = ""
    col_date = ""
    col_size = ""
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    q5 = 0
    q6 = 0
    q7 = 0
    q8 = 0
    q9 = 0
    q10 = 0
	
    while i < len(list_of_rows)  :
        #print( len(list_of_rows) ) 
        
        for row in list_of_rows[i]:
            #print(i);
            #print(  row.split(';')  )

            #print(sizeofList)
            columvalue =  row.split(';')
            # get size of row
            sizeofList = len( columvalue  )	
	        # get size of entroy values by deducting 3 (filenane, date, size)
            sizeofEntropyValues = sizeofList - 3
            blocksofentropies = long(sizeofEntropyValues / 10)
            # print(sizeofEntropyValues)
            #print(sizeofEntropyValues)
	        #print(list_of_rows)
            col_filname = columvalue[0]
            col_date = columvalue[1]
            col_size = columvalue[2]
            if(sizeofEntropyValues > 1 and blocksofentropies > 1):
                j = 4
                calc_durchschnitt = 0.0
                calc_durchschnitt_counter = 0
                first = 1
                no = 0
                while j < sizeofList - 1:
                    #print(sizeofList)
                    calc_durchschnitt_counter += 1
                    # print(columvalue[j])
                    #if(  (isinstance( columvalue[j] , float) ) == True  ):
                        #j += 1
                    #if type(columvalue[j]) == str :
                    #    j += 1
                    #    continue 
                    calc_durchschnitt = calc_durchschnitt + float(columvalue[j])

                    # print( columvalue[j])
                    # schreibe ergebnisse
                    if ( (j % blocksofentropies ) == 0 ): #and first != 1
                        first = 0
                        no += 1                
                        # calc_durchschnitt = calc_durchschnitt + 11111
                        #write result
                        if (no == 1):
                            q1 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q1)
                        if (no == 2):
                            q2 = (calc_durchschnitt / calc_durchschnitt_counter)
                        if (no == 3):
                            q3 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q3)
                        if (no == 4):
                            q4 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q4)
                        if (no == 5):
                            q5 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q5)
                        if (no == 6):
                            q6 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q6)
                        if (no == 7):
                            q7 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q7)
                        if (no == 8):
                            q8 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q8)
                        if (no == 9):
                            q9 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q9)
                        if (no == 10):
                            q10 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q10)
                        # setze ergebnisse wieder zurück
                        calc_durchschnitt = 0
                        calc_durchschnitt_counter = 0

                    j += 1

        #output_string =  str( col_filname   ) + ";" + str( col_date   ) + ";" + str(col_size   )  +   ";" +            str(q1).replace('.', ',')    + ";" + str(q2).replace('.', ',') + ";" + str(q3).replace('.', ',') + ";" + str(q4).replace('.', ',')  + ";" + str(q5).replace('.', ',')  + ";" + str(q6).replace('.', ',')  + ";" + str(q7).replace('.', ',')  + ";" + str(q8).replace('.', ',')  + ";" + str(q9).replace('.', ',')  + ";" + str(q10).replace('.', ',') 
        output_string =  str( col_filname   ) + ";" + str( col_date   ) + ";" + str(col_size   )  +   ";" +            str(q1)    + ";" +     str(q2)   + ";" +        str(q3)   + ";" + str(q4)      + ";" + str(q5)          + ";" + str(q6)  + ";" + str(q7)     + ";" + str(q8)  + ";" + str(q9)  + ";" +  str(q10) 

		#print(output_string)


        #v1,v2 = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10], [2, 54, 13, 15, 8, 2, 54, 13, 15, 8]
        #print(v1, v2, cosine_similarity(v1,v2))
        #print('{0:.,2f}'.format(q1   ))
        #print(q1"{num:,d}")
        #my_number = 4385893.382939491
        #my_string = '{:,.2f}'.format(my_number)
        #print(my_string)
        f.write( output_string + "\r\n" )
        col_filname = ""
        col_date = ""
        col_size = ""
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        q5 = 0
        q6 = 0
        q7 = 0
        q8 = 0
        q9 = 0
        q10 = 0
        i += 1

f.close()

		
		
		
		

		
		
		
###
###
###
###
###
###
###
###
###
###
###
# read csv file as a list of lists
with open('entfiles_test_data.csv', 'r') as read_objB:
    # pass the file object to reader() to get the reader object
    csv_readerB = csv.reader(read_objB)
	
    # Pass reader object to list() to get a list of lists
    list_of_rowsB = list(csv_readerB)
    
    i = 0# 
	
    col_filname = ""
    col_date = ""
    col_size = ""
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    q5 = 0
    q6 = 0
    q7 = 0
    q8 = 0
    q9 = 0
    q10 = 0
	
    while i < len(list_of_rowsB)  :
        #print(wordList[i]) 
        
        for row in list_of_rowsB[i]:

            #print(  row.split(';')  )

            #print(sizeofList)
            columvalue =  row.split(';')
            # get size of row
            sizeofList = len( columvalue  )	
	        # get size of entroy values by deducting 3 (filenane, date, size)
            sizeofEntropyValues = sizeofList - 3
            blocksofentropies = long(sizeofEntropyValues / 10)
            # print(sizeofEntropyValues)
            #print(sizeofEntropyValues)
	        #print(list_of_rows)
            col_filname = columvalue[0]
            col_date = columvalue[1]
            col_size = columvalue[2]
            if(sizeofEntropyValues > 1 and blocksofentropies > 1):
                j = 4
                calc_durchschnitt = 0.0
                calc_durchschnitt_counter = 0
                first = 1
                no = 0
                while j < sizeofList - 1:
                    #print(sizeofList)
                    calc_durchschnitt_counter += 1
                    # print(columvalue[j])
                    #if(  (isinstance( columvalue[j] , float) ) == True  ):
                        #j += 1
                    #if type(columvalue[j]) == str :
                    #    j += 1
                    #    continue 
                    calc_durchschnitt = calc_durchschnitt + float(columvalue[j])

                    # print( columvalue[j])
                    # schreibe ergebnisse
                    if ( (j % blocksofentropies ) == 0 ): #and first != 1
                        first = 0
                        no += 1                
                        # calc_durchschnitt = calc_durchschnitt + 11111
                        #write result
                        if (no == 1):
                            q1 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q1)
                        if (no == 2):
                            q2 = (calc_durchschnitt / calc_durchschnitt_counter)
                        if (no == 3):
                            q3 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q3)
                        if (no == 4):
                            q4 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q4)
                        if (no == 5):
                            q5 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q5)
                        if (no == 6):
                            q6 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q6)
                        if (no == 7):
                            q7 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q7)
                        if (no == 8):
                            q8 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q8)
                        if (no == 9):
                            q9 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q9)
                        if (no == 10):
                            q10 = (calc_durchschnitt / calc_durchschnitt_counter)
                            #print(q10)
                        # setze ergebnisse wieder zurück
                        calc_durchschnitt = 0
                        calc_durchschnitt_counter = 0

                    j += 1

        #output_string =  str( col_filname   ) + ";" + str( col_date   ) + ";" + str(col_size   )  +               str(q1).replace('.', ',')    + ";" + str(q2).replace('.', ',') + ";" + str(q3).replace('.', ',') + ";" + str(q4).replace('.', ',')  + ";" + str(q5).replace('.', ',')  + ";" + str(q6).replace('.', ',')  + ";" + str(q7).replace('.', ',')  + ";" + str(q8).replace('.', ',')  + ";" + str(q9).replace('.', ',')  + ";" + str(q10).replace('.', ',') 
        #print(output_string)
        output_string =  str( col_filname   ) + ";" + str( col_date   ) + ";" + str(col_size   )  +   ";" +            str(q1)    + ";" +     str(q2)   + ";" +        str(q3)   + ";" + str(q4)      + ";" + str(q5)          + ";" + str(q6)  + ";" + str(q7)     + ";" + str(q8)  + ";" + str(q9)  + ";" +  str(q10) 


        #v1,v2 = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10], [2, 54, 13, 15, 8, 2, 54, 13, 15, 8]
        #print(v1, v2, cosine_similarity(v1,v2))
        #print('{0:.,2f}'.format(q1   ))
        #print(q1"{num:,d}")
        #my_number = 4385893.382939491
        #my_string = '{:,.2f}'.format(my_number)
        #print(my_string)
        f3.write( output_string + "\r\n" )
        col_filname = ""
        col_date = ""
        col_size = ""
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        q5 = 0
        q6 = 0
        q7 = 0
        q8 = 0
        q9 = 0
        q10 = 0
        i += 1
		
f3.close()
	
	
	
	

	



#print('###################################################')
		
#time.sleep(10) # 10 sekunden warten 
# open file in read mode
#with open('entfiles_test_data_transformed.csv', 'r') as read_objaa:
#    # pass the file object to reader() to get the reader object
#    csv_reader = reader(read_objaa)
#    # Iterate over each row in the csv using reader object
#    for row in csv_reader:
#        # row variable is a list that represents a row in csv
#        print(row)
		
		
		
		
		
		

print ("group,variable,value")
foutput.write( "group,variable,value" + "\r\n" )

with open('entfiles_test_data_transformed.csv', 'r') as read_objx:
    # pass the file object to reader() to get the reader object
    csv_readerx = csv.reader(read_objx)
	
    # Pass reader object to list() to get a list of lists
    list_of_rowsx = list(csv_readerx)
    
    i = 0# 
    #print(  len(list_of_rowsx )  )
	
    while i < len(list_of_rowsx ) :
        # print(list_of_rowsx[i]) 
        
        for row in list_of_rowsx[i]:
            columvalue =  row.split(';')
            # get size of row
            sizeofList = len( columvalue  )	
            #print(sizeofList)
            # print(sizeofEntropyValues)
            #print(sizeofEntropyValues)
	        #print(list_of_rows)
			
            #col_filname = columvalue[0]
            #col_date = columvalue[1]
            #col_size = columvalue[2]
            #print ( columvalue[0] )
			



            with open('entfiles_raw_BE_transformed.csv', 'r') as read_objy:
                # pass the file object to reader() to get the reader object
                csv_reader3 = csv.reader(read_objy)
                # Pass reader object to list() to get a list of lists
                list_of_rows2 = list(csv_reader3)
                #print (list_of_rows2  )
                h = 0
            
                while h < len(list_of_rows2) :
                    #print(list_of_rows2[h]) 
                    x = 0
                    for row2 in list_of_rows2[h] :
                        #if(x == 10):
                        #    continue
                        columvalue2 =  row2.split(';')
                        # get size of row
                        sizeofList2 = len( columvalue2  )	
                        #print(sizeofList2)
                        # print(sizeofEntropyValues)
                        #print(sizeofEntropyValues)
	                    #print(list_of_rows)
            
                        #col_filname = columvalue[0]
                        #col_date = columvalue[1]
                        #col_size = columvalue[2]
                        v1,v2 = [ float(columvalue2[3]), float(columvalue2[4]), float(columvalue2[5]), float(columvalue2[6]), float(columvalue2[7]), float(columvalue2[8]), float(columvalue2[9]), float(columvalue2[10]), float(columvalue2[11]), float(columvalue2[12])],              [            float(columvalue[3]), float(columvalue[4]), float(columvalue[5]), float(columvalue[6]), float(columvalue[7]), float(columvalue[8]), float(columvalue[9]), float(columvalue[10]), float(columvalue[11]), float(columvalue[12])    ]
                        #print(v1,v2)
                        #print str(  cosine_similarity(v1,v2)  ).replace('.', ',') +";",
                        print( str(columvalue2[0]) + ","     + str(columvalue[0]) + ","      + str(  cosine_similarity(v1,v2)  )  )
                        foutput.write(  str(columvalue2[0]) + ","     + str(columvalue[0]) + ","      + str(  cosine_similarity(v1,v2)  ) + "\r\n" )
                        #x = x +1
                    h = h +1



        # v1,v2 = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10], [2, 54, 13, 15, 8, 2, 54, 13, 15, 8]
        # print(v1, v2, cosine_similarity(v1,v2))
        i += 1
foutput.close()
		
		
		
PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("#####################################")
print("# ")
print "# [x] File comparison completed." 
print("# ")
print "# [x] Serving at port", PORT
print("# ")
print("# [*] Open the following URL in your Browser:")
print("#     http://127.0.0.1:8000/heatmap_file_comparison_d3.html")
print("# ")
print("#####################################")
httpd.serve_forever()
