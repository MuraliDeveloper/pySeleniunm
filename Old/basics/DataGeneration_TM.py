import random
import string
f1=open('tm.txt', 'w')
f1.write('{"value":[')
for month in range(6,7):
	for date in range(1,2):
		for hour in range(0,24):
			for minute in range(0,60):
				for second in range(0,60):
				   #f1.write('\n{"_time": "2020-%02d-%02dT%02d:%02d:%02d.000Z","P1": "%s","P2": "%s","P3": "%s","P4": "%s","P5": "%s.%d"},' %(month,date,hour,minute,second,"".join([random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(3)]),"".join([random.choice(string.digits) for _ in range(2)]),"".join([random.choice(string.digits) for _ in range(2)]),random.choice(["true","false"]),"".join([random.choice(string.digits) for _ in range(2)]),second))
				   f1.write('\n{"_time": "2020-%02d-${d}T%02d:%02d:%02d.000Z","P1": "${__RandomString(3,abcdefghijklmnopqrstuvwxyz,modelId1)}","P2": "${__RandomString(2,123456789,modelId1)}","P3": "${__RandomString(2,123456789,modelId1)}","P4": "true","P5": "${__RandomString(2,123456789,modelId1)}.0"},' % (month, hour, minute, second))
f1.write('\n ]}')
f1.close()
print("done")



