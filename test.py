import datetime, time

#Run all the test cases, comment out test that is not run
RunGeneralCases = False
#RunGeneralCases = True


testList = []
passed = 0
failed = 0
'''
testList.append("./inventory/case1.py")
testList.append("./inventory/case2.py")
testList.append("./inventory/case3.py")
testList.append("./inventory/case4.py")
'''
testList.append("./catalog/case1.py")
'''
testList.append("./catalog/case2.py")

testList.append("./orders/case1.py")
testList.append("./orders/case2.py")
'''

#testList.append("./administration/case1.py")

def timestamp():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	return "[" + str(st) + "] "

#General test cases - Make sure all general test case pass
print "===================================================="
print "Start Automated Testing"
print "====================================================\n"

automationStart = datetime.datetime.now().replace(microsecond=0)
if(RunGeneralCases == True):
	print timestamp() + "Running general tests"
	caseStart = datetime.datetime.now().replace(microsecond=0)
	exec(open("./general/case1.py").read())
	exec(open("./general/case2.py").read())
	#exec(open("./general/test.py").read())
	caseEnd = datetime.datetime.now().replace(microsecond=0)
	print timestamp() + "Duration " + str(caseEnd - caseStart)
	print timestamp() + "General tests passed\n"
else:
	print timestamp() + "General tests skipped\n"


for case in testList:
	print timestamp() + "Running " + case.replace("./", "")
	caseStart = datetime.datetime.now().replace(microsecond=0)
	try:
		exec(open(case).read())
		caseEnd = datetime.datetime.now().replace(microsecond=0)
		print timestamp() + "Duration " + str(caseEnd - caseStart)
		print timestamp() + case.replace("./", "") + " passed\n"
		passed = passed + 1
	except Exception, err:
		print Exception, err
		caseEnd = datetime.datetime.now().replace(microsecond=0)
		print timestamp() + "Duration " + str(caseEnd - caseStart)
		print timestamp() + case.replace("./", "") + " failed\n"
		failed = failed + 1
		
automationEnd = datetime.datetime.now().replace(microsecond=0)
print "===================================================="
print str(passed) + "/" + str(len(testList)) + " cases passed"
print str(failed) + "/" + str(len(testList)) + " cases failed"
print "Total Duration " + str(automationEnd - automationStart)
print "====================================================\n"

