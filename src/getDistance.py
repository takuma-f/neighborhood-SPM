# coding: UTF-8

def getDistance(pattern, record):
	# レコード一つに含まれるパターンの距離を返す
	pass

if __name__ == '__main__':
	result    = 0
	distance  = 0
	pdistance = 0
	firsthit  = False
	pattern = [       "Eat",       "Tea",       "Bar"]
	record  = ["Play","Eat","Shop","Tea","Play","Bar"]

	for x in pattern:
		for y in record:
			if x == y:
				temp      = record.index(y) - pattern.index(x)
				distance  = temp - pdistance
				pdistance = temp
				if firsthit == False:
					distance = 0
					firsthit = True
				result += distance
	print result