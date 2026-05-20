import csv, dateutil, os
from itertools import islice
from dateutil import parser
import datetime

title = ['SECNUM', 'HWY_ID', 'AADTA', 'PCT_TRUCKA', 'YEAR', 'PAVETYPE', 'PQI', 'RQI', 'SR', 'AVG_IRI', 'LENGTH', 'PNTCNT', 'INC_INJ', 'NON_INC_INJ', 'POS_INJ', 'FATAL', 'PRO_DAM', 'NV', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Straight', 'Curve', 'Level', 'Grade', 'Hillcrest', 'Sag', 'Wet', 'Snow', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', '12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm']
def insideMap():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = '/Users/toshiyokoo/Desktop/07_result'
	#outputFile = open(os.path.join(root_path,"pavement_quality_2003")+'.csv','a') #change year
	outputFile = open(os.path.join(root_path,filename[:-4]+'.csv'),'a')
	writer = csv.writer(outputFile, lineterminator='\n')
	print >> outputFile, ','.join(title)
	
	PavementFile = open("/Users/toshiyokoo/Desktop/5133/2000-2015_M-Record_History.csv",'rU')
	idlist = csv.reader(PavementFile)
	PavementFile.seek(0)
	for row in islice(idlist, 1, None):
		year = int(row[14])
		if year == int(filename[5:9]):		#change year
			list = []
			secnum = str(row[0])
			num = int(float(str(row[0])))
			id = str(row[1])
			aadta = str(row[12])
			truck = str(row[13])
			year = str(row[14])
			pavetype = str(row[18])
			pqi = str(row[19])
			rqi = str(row[20])
			sr = str(row[21])
			iri = str(row[22])
			length = float(str(row[7])) - float(str(row[6]))
		
			#default
			pntcnt = 0
			inc_inj = 0
			non_inc_inj = 0
			pos_inj = 0
			fatal = 0
			pro_dam = 0
			nv = 0
			
			sunday = 0
			monday = 0
			tuesday = 0
			wednesday = 0
			thursday = 0
			friday = 0
			saturday = 0
			
			straight = 0
			curve = 0
			level = 0
			grade = 0
			hillcrest = 0
			sag = 0
			#other_type = 0
			
			wet = 0
			snow = 0
			#other_surface = 0
			
			january = 0
			february = 0
			march = 0
			april = 0
			may = 0
			june = 0
			july = 0
			august = 0
			september = 0
			october = 0
			november = 0
			december = 0
			
			am12 = 0
			am1 = 0
			am2 = 0
			am3 = 0
			am4 = 0
			am5 = 0
			am6 = 0
			am7 = 0
			am8 = 0
			am9 = 0
			am10 = 0
			am11 = 0
			pm12 = 0
			pm1 = 0
			pm2 = 0
			pm3 = 0
			pm4 = 0
			pm5 = 0
			pm6 = 0
			pm7 = 0
			pm8 = 0
			pm9 = 0
			pm10 = 0
			pm11 = 0
		
			inputFile.seek(0)
			for lim in islice(reader, 1, None):
				hw_num = int(float(str(lim[10])))
				if hw_num == num:
					crash_sev = str(lim[1])
					if crash_sev == 'A':
						inc_inj += 1	#INCAPACITATING INJURY
					elif crash_sev == 'B':
						non_inc_inj += 1	#NON-INCAPACITATING INJURY
					elif crash_sev == 'C':
						pos_inj += 1	#POSSIBLE INJURY
					elif crash_sev == 'K':
						fatal += 1	#FATAL
					elif crash_sev == 'N':
						pro_dam += 1	#PROPERTY DAMAGE
					elif crash_sev == 'X':
						nv += 1	#NV
					#length = str(lim[114])
					pntcnt = str(lim[11])
				
					#day_of_week
					day_of_week = str(lim[4])
					if day_of_week == '1': #Sunday
						sunday += 1
					elif day_of_week == '2': #Monday
						monday += 1
					elif day_of_week == '3': #Tuesday
						tuesday += 1
					elif day_of_week == '4': #Wednesday
						wednesday += 1
					elif day_of_week == '5': #Thursday
						thursday += 1
					elif day_of_week == '6': #Friday
						friday += 1
					elif day_of_week == '7': #Saturday
						saturday += 1
					
					#road_type
					road_type = str(lim[6])
					if road_type == '1':
						straight += 1
						level += 1
					elif road_type == '2':
						straight += 1
						grade += 1
					elif road_type == '3':
						straight += 1
						hillcrest += 1
					elif road_type == '4':
						straight += 1
						sag += 1
					elif road_type == '5':
						curve += 1
						level += 1
					elif road_type == '6':
						curve += 1
						grade += 1
					elif road_type == '7':
						curve += 1
						hillcrest += 1
					elif road_type == '8':
						curve += 1
						sag += 1
					#else:
					#	other_type += 1
						
					#road_surface
					road_surface = str(lim[8])
					if road_surface == '2':
						wet += 1
					elif road_surface == '6':
						wet += 1
					elif road_surface == '7':
						wet += 1
					elif road_surface == '3':
						snow += 1
					elif road_surface == '4':
						snow += 1
					elif road_surface == '5':
						snow += 1
					#else:
					#	other_surface += 1
					
					#month of date
					date = str(lim[0])
					d = datetime.datetime.strptime(date, '%m/%d/%y')
					month = d.month
					if month == 1:
						january += 1
					elif month == 2:
						february += 1
					elif month == 3:
						march += 1
					elif month == 4:
						april += 1
					elif month == 5:
						may += 1
					elif month == 6:
						june += 1
					elif month == 7:
						july += 1
					elif month == 8:
						august += 1
					elif month == 9:
						september += 1
					elif month == 10:
						october += 1
					elif month == 11:
						november += 1
					elif month == 12:
						december += 1	
					
					#time
					time = str(lim[3])
					hour = time[:-2]
					if hour == '1':
						am1 += 1
					elif hour == '2':
						am2 += 1
					elif hour == '3':
						am3 += 1
					elif hour == '4':
						am4 += 1
					elif hour == '5':
						am5 += 1
					elif hour == '6':
						am6 += 1
					elif hour == '7':
						am7 += 1
					elif hour == '8':
						am8 += 1
					elif hour == '9':
						am9 += 1
					elif hour == '10':
						am10 += 1
					elif hour == '11':
						am11 += 1
					elif hour == '12':
						pm12 += 1
					elif hour == '13':
						pm1 += 1
					elif hour == '14':
						pm2 += 1
					elif hour == '15':
						pm3 += 1
					elif hour == '16':
						pm4 += 1
					elif hour == '17':
						pm5 += 1
					elif hour == '18':
						pm6 += 1
					elif hour == '19':
						pm7 += 1
					elif hour == '20':
						pm8 += 1
					elif hour == '21':
						pm9 += 1
					elif hour == '22':
						pm10 += 1
					elif hour == '23':
						pm11 += 1
					elif hour == '99':
						error = 1
					else:
						am12 += 1
			list.extend([secnum, id, aadta, truck, year, pavetype, pqi, rqi, sr, iri, length, pntcnt, inc_inj, non_inc_inj, pos_inj, fatal, pro_dam, nv, sunday, monday, tuesday, wednesday, thursday, friday, saturday, straight, curve, level, grade, hillcrest, sag, wet, snow, january, february, march, april, may, june, july, august, september, october, november, december, am12, am1, am2, am3, am4, am5, am6, am7, am8, am9, am10, am11, pm12, pm1, pm2, pm3, pm4, pm5, pm6, pm7, pm8, pm9, pm10, pm11])
			writer.writerow(list)
			list = []			
	inputFile.close()

path = "/Users/toshiyokoo/Desktop/aadbz"
for filename in os.listdir(path):
	global filename
	insideMap()