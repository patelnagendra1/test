import datetime
def getDay(dt):
    day, month, year = (int(x) for x in dt.split('/'))    
    ans = datetime.date(year, month, day)
    return (ans.strftime("%A"))



def func(d):


    d1 = {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
    for i in d:
        year = i[0:4]
        month = i[5:7]
        day = i[8:10]
       # print(year,month,day)
        date = day+"/"+month+"/"+year
        #print(date)
        day = getDay(date)
        
        d1[day] = d1[day] + d[i]
    # print(d1)
    d2 = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0}
    x = "0"
    for i in d1:
        d2[x] = d1[i]
        x = str((int(x))+1)
    #print(d2)
    i = 0
    while(i<len(d2)):
        if (d2[str(i)]) == 0:
            start = i
            end = i
            for j in range(start,len(d2)):
                if d2[str(j)] == 0:
                    i += 1
                    continue
                else:
                    end = j
                    i += j
                    break
          #  print(start,end)
            d = (d2[str(end)]-d2[str(start-1)])//(end-start+1)
           # print(d)
            a = d2[str(start-1)]+d
            for i in range(start,end):
                d2[str(i)] = a
                a += d
        else:
            i += 1
    #print(d2)
    c = 0
    for i in d1:
        d1[i] = d2[str(c)]
        c += 1
    print(d1)


################### Input for First test case ##########################

d = {"2020-01-01":4,"2020-01-02":4,"2020-01-03":6,"2020-01-04":8,"2020-01-05":2,"2020-01-06":-6,"2020-01-07":2,"2020-01-08":-2}
func(d)

################### Input for First test case ##########################    
d = {"2020-01-01":6,"2020-01-04":12,"2020-01-05":14,"2020-01-06":2,"2020-01-07":4}
func(d)