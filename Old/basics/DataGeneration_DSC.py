import random
import string

"""
standard
f1 = open('week7.txt', 'w')
f1.write('"Values":[')
for month in range(7,8):
		for date in range(11,12):
			for hour in range(0,24):
				for minute in range(0,60):
					for second in range(0,60):
					   f1.write('\n{"_time": "2020-%02d-%02dT%02d:%02d:%02d.000Z","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX1": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX2": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX3": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX4": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX5": "%s.%d"},' %(month,date,hour,minute,second,"".join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(3)]),"".join([random.choice(string.digits) for _ in range(2)]),"".join([random.choice(string.digits) for _ in range(2)]),random.choice(["true","false"]),"".join([random.choice(string.digits) for _ in range(2)]),second))
f1.write('\n ]}')
f1.close()
print("done")
"""

f1 = open('RES.txt', 'w')
f1.write('"Values":[')
for month in range(6,7):
		for date in range(1,2):
			for hour in range(0,24):
				for minute in range(0,60):
					for second in range(0,60):
					   f1.write('\n{"_time": "2020-%02d-${d}T%02d:%02d:%02d.000Z","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX1": "${__RandomString(3,abcdefghijklmnopqrstuvwxyz,modelId1)}","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX2": "${__RandomString(2,123456789,modelId1)}","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX3": "${__RandomString(2,123456789,modelId1)}","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX4": "true","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX5": "${__RandomString(2,123456789,modelId1)}.0"},' %(month,hour,minute,second))
f1.write('\n ]}')
f1.close()
print("done")

"""
day=1
for month in range(6,7):
		for date in range(1,31):
			f1 = open('day'+str(day)+'.txt', 'w')
			day=day+1
			f1.write('"Values":[')
			for hour in range(0,24):
				for minute in range(0,60):
					for second in range(0,60):
					   f1.write('\n{"_time": "2020-%02d-%02dT%02d:%02d:%02d.000Z","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX1": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX2": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX3": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX4": "%s","PRPIDM1EMB5YACN24IRKJUGO9G3W5NX5": "%s.%d"},' %(month,date,hour,minute,second,"".join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(3)]),"".join([random.choice(string.digits) for _ in range(2)]),"".join([random.choice(string.digits) for _ in range(2)]),random.choice(["true","false"]),"".join([random.choice(string.digits) for _ in range(2)]),second))
			f1.write('\n ]}')
			f1.close()
print("done")
"""




