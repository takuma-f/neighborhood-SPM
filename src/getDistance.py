# coding: UTF-8
def getDistance(pattern, record):
    # レコード一つに含まれるパターンの距離を返す
    result    = 0
    distance  = 0
    pdistance = 0
    firsthit  = False

    for p in pattern:
        for r in record:
            if p == r:
                temp      = record.index(r) - pattern.index(p)
                distance  = temp - pdistance
                pdistance = temp
                if firsthit == False:
                    distance = 0
                    firsthit = True
                result += distance
    return result


if __name__ == '__main__':
	pattern = [       "Eat","Tea","Bar"]
	record  = ["Play","Eat","Tea","Bar"]

	print getDistance(pattern,record)