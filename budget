
def expenseList():
    expL = []
    budgDict = {}
    total=0
    itemN = int(raw_input("How many expenses do you have? "))
    income = int(raw_input("How much do you make monthly? "))
    for n in range(itemN):
        expL.append(raw_input("What is expense? "))
        #print str(expL[n])
        budgDict[str(expL[n])] = int(raw_input("How much is your %s? " % (expL[n]) ))
    
    for key in budgDict:
        total+=budgDict[key]
    leftOver = income - total
    print
    print "----------"
    print
    print "Total Expenses: ", str(total)
    print
    print "Money left over: ", str(leftOver)
    print
    print "----------"
    
expenseList()
