import csv,os, numpy, math
from itertools import islice
import datetime

title = ['SECNUM', 'HWY_ID', 'AADTA', 'PCT_TRUCKA', 'YEAR', 'PAVETYPE', 'PQI', 'RQI', 'SR', 'AVG_IRI', 'LENGTH', 'PNTCNT', 'INC_INJ', 'NON_INC_INJ', 'POS_INJ', 'FATAL', 'PRO_DAM', 'NV', 'year_2003', 'year_2004', 'year_2005', 'year_2006', 'year_2007', 'year_2008', 'year_2009', 'year_2010', 'year_2011', 'year_2012', 'year_2013', 'bituminous_1', 'bituminous_2', 'Weekend', 'Curve', 'Grade', 'Hillcrest', 'Sag', 'Wet', 'Snow', 'SLR', 'Rushhour']

def summarize():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = '/Users/toshiyokoo/Desktop/08_result'
	outputFile = open(os.path.join(root_path,filename[:-4]+'.csv'),'a')
	writer = csv.writer(outputFile, lineterminator='\n')
	print >> outputFile, ','.join(title)
	for row in islice(reader, 1, None):	
		list = []
		secnum = str(row[0])
		id = str(row[1])
		aadta = str(row[2])
		truck = str(row[3])
		year = str(row[4])
		pavetype = str(row[5])
		pqi = str(row[6])
		rqi = str(row[7])
		sr = str(row[8])
		iri = str(row[9])
		length = str(row[10])
		pntcnt = str(row[11])
		inc_inj = str(row[12])
		non_inc_inj = str(row[13])
		pos_inj = str(row[14])
		fatal = str(row[15])
		pro_dam = str(row[16])
		nv = str(row[17])
			
		#Dummy variable (Year)
		num_year = int(row[4])
		year_2003 = 0
		year_2004 = 0
		year_2005 = 0
		year_2006 = 0
		year_2007 = 0
		year_2008 = 0
		year_2009 = 0
		year_2010 = 0
		year_2011 = 0
		year_2012 = 0
		year_2013 = 0
		#year_2014 = 0
		if num_year == 2003:
			year_2003 = 1
		elif num_year == 2004:
			year_2004 = 1
		elif num_year == 2005:
			year_2005 = 1
		elif num_year == 2006:
			year_2006 = 1
		elif num_year == 2007:
			year_2007 = 1
		elif num_year == 2008:
			year_2008 = 1
		elif num_year == 2009:
			year_2009 = 1
		elif num_year == 2010:
			year_2010 = 1
		elif num_year == 2011:
			year_2011 = 1
		elif num_year == 2012:
			year_2012 = 1
		elif num_year == 2013:
			year_2013 = 1
		elif num_year == 2014:
			dummy = 1
		else:
			year_2003 = 99
			year_2004 = 99
			year_2005 = 99
			year_2006 = 99
			year_2007 = 99
			year_2008 = 99
			year_2009 = 99
			year_2010 = 99
			year_2011 = 99
			year_2012 = 99
			year_2013 = 99
		
		Year_2003 = str(year_2003)
		Year_2004 = str(year_2004)
		Year_2005 = str(year_2005)
		Year_2006 = str(year_2006)
		Year_2007 = str(year_2007)
		Year_2008 = str(year_2008)
		Year_2009 = str(year_2009)
		Year_2010 = str(year_2010)
		Year_2011 = str(year_2011)
		Year_2012 = str(year_2012)
		Year_2013 = str(year_2013)
		
		#Dummy variable (pavement type)
		pavetype = str(row[5])
		bituminous_1 = 0
		bituminous_2 = 0
		if pavetype == 'BAB':
			bituminous_1 = 1
		elif pavetype == 'BFD':
			bituminous_1 = 1
		elif pavetype == 'BOB':
			bituminous_1 = 1
		elif pavetype == 'BOC':
			bituminous_2 = 1
		elif pavetype == 'CD':
			dummy = 0
		elif pavetype == 'CRC':
			dummy = 0
		elif pavetype == 'CU':
			dummy = 0	
		else:
			bituminous_1 = 99
			bituminous_2 = 99
			
		Bituminous_1 = str(bituminous_1)
		Bituminous_2 = str(bituminous_2)
		
		#Dummy variable (day of week)
		d_weekend = 0
		sunday = int(row[18])
		if sunday > 0:
			d_weekend = 1
		saturday = int(row[24])
		if saturday > 0:
			d_weekend = 1
			
		#Dummy variable (horizontal alignment)
		d_straight = 0
		d_curve = 0
		straight = int(row[25])
		if straight > 0:
			d_straight = 1
		curve = int(row[26])
		if curve > 0:
			d_curve = 1
			
		#Dummy variable (vertical alignment)
		d_level = 0
		d_grade = 0
		d_hillcrest = 0
		d_sag = 0
		level = int(row[27])
		if level > 0:
			d_level = 1
		grade = int(row[28])
		if grade > 0:
			d_grade = 1
		hillcrest = int(row[29])
		if hillcrest > 0:
			d_hillcrest = 1
		sag = int(row[30])
		if sag > 0:
			d_sag = 1
		
		#Dummy variable (road surface)
		d_wet = 0
		d_snow = 0
		wet = int(row[31])
		if wet > 0:
			d_wet = 1
		snow = int(row[32])
		if snow > 0:
			d_snow = 1
		
		#Dummy variable (SLR)
		d_slr = 0
		march = int(row[35])
		if march > 0:
			d_slr = 1
		april = int(row[36])
		if april > 0:
			d_slr = 1
		may = int(row[37])
		if may > 0:
			d_slr = 1
		
		#Dummy variable (time)
		d_rushhour = 0	
		am6 = int(row[51])
		if am6 > 0:
			d_rushhour = 1
		am7 = int(row[52])
		if am7 > 0:
			d_rushhour = 1
		am8 = int(row[53])
		if am8 > 0:
			d_rushhour = 1
		pm3 = int(row[60])
		if pm3 > 0:
			d_rushhour = 1
		pm4 = int(row[61])
		if pm4 > 0:
			d_rushhour = 1
		pm5 = int(row[62])
		if pm5 > 0:
			d_rushhour = 1
		pm6 = int(row[63])
		if pm6 > 0:
			d_rushhour = 1

		
		list.extend([secnum, id, aadta, truck, year, pavetype, pqi, rqi, sr, iri, length, pntcnt, inc_inj, non_inc_inj, pos_inj, fatal, pro_dam, nv, Year_2003,Year_2004,Year_2005,Year_2006,Year_2007,Year_2008,Year_2009,Year_2010,Year_2011,Year_2012,Year_2013, Bituminous_1,Bituminous_2, d_weekend, d_curve, d_grade, d_hillcrest, d_sag, d_wet, d_snow, d_slr, d_rushhour])
		writer.writerow(list)
		list = []
		
	inputFile.close()
	print filename

path = "/Users/toshiyokoo/Desktop/aadce"
for filename in os.listdir(path):
	global filename
	summarize()
