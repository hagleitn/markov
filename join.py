import sys
import datetime

with open(sys.argv[2], 'rU') as fs:
    lookup = {}
    for line in fs:
        fsd = line.split(',')
        if len(fsd) >= 2:
            resolved = datetime.datetime.strptime(fsd[1].strip(),"%m/%d/%y %H:%M")
            lookup[fsd[0].strip()] = resolved

    with open(sys.argv[1], 'rU') as ss:
        good = bad = worse = worst = 0
        for line in ss:
            ssd = line.split(',')
            bug = ssd[0]
            created = datetime.datetime.strptime(ssd[2], "%d/%b/%y %H:%M %p")
            resolved_dates = []
            for i in range(len(ssd)-3):
                key = ssd[i+3].strip()
                if key in lookup:
                    resolved_dates.append(lookup[key])

            if len(resolved_dates) >= 1:
                rd = resolved_dates[0]
                for d in resolved_dates:
                    if rd < d:
                        rd = d
                print "%s, %s" % (ssd[0], created - rd)
                if (created > rd):
                    bad += 1
                else:
                    good +=1

                if (created > rd + datetime.timedelta(days = 14)):
                    worse += 1
                if (created > rd + datetime.timedelta(days = 30)):
                    worst += 1


    print "Total: %i" % (good + bad)
    print "Number of known issues: %i" % bad
    print "Number of issues known for more than 2 weeks: %i" % worse
    print "Number of issues known for more than 4 weeks: %i" % worst
    print "Number of unknown issues: %i" % good
