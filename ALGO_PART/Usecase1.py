from tkinter import *
import pickle
inr = False
lean = []
no_datas = 2016
period_length = 1
API = {}
predefined=[]
lean_periods = []
switchList = ['S1', 'S2', 'S3', 'S4', 'S5']

def day(x):
       
        y = x/288
        if y < 1:
            z = x*5/60
            z1 = x*5 % 60
            day = " 13/2/23 at "+str(int(z))+":"+str(int(z1))
            print(day)
          
            API[switch] = day

        elif y >= 1 and y < 2:
            x = x-288
            z = x*5/60
            z1 = x*5 % 60
            day = " 14/2/23 at "+str(int(z))+":"+str(int(z1))
            print(day)
          
            API[switch] = day
        elif y >= 2 and y < 3:
            x = x-288*2
            z = x*5/60
            z1 = x*5 % 60
            day = " 15/2/23 at "+str(int(z))+":"+str(int(z1))
            print(day)
           
            API[switch] = day
        elif y >= 3 and y < 4:
            x = x-288*3
            z = x*5/60
            z1 = x*5 % 60
            day = " 16/2/23 at "+str(int(z))+":"+str(int(z1))
            print(day)
            
            API[switch] = day
        elif y >= 4 and y < 5:
            x = x-288*4
            z = x*5/60
            z1 = x*5 % 60
            day = " 17/2/23 at "+str(int(z))+":"+str(int(z1))
            print(day)
          
            API[switch] = day
        elif y >= 5 and y < 6:
            x = x-288*5
            z = x*5/60
            z1 = x*5 % 60
            day = " 18/2/23 at "+str(int(z))+":"+str(int(z1))
            print(day)
           
            API[switch] = day
        elif y >= 6 and y < 7:
            x = x-288*6
            z = x*5/60
            z1 = x*5 % 60
            day = " 19/2/23 at "+str(int(z))+":"+str(int(z1))
            print(day)
           
            API[switch] = day
        print()
       
        
        

for i in switchList:
    lean_periods = []
    lean=[]
    print(i)
    print()

    switch = i
    threshold = float(input('Threshold'))

   

    with open("../PRED_"+switch+"/"+switch, "rb") as fp:   # Unpickling
        jsk = pickle.load(fp)
        

    try:

        for i in range(0, no_datas):
            if (len(lean) == period_length):
                lean_periods.append([i-6, lean])
                lean = []
                inr = False

            if (jsk[i] > threshold):
                inr = False
                lean = []
            elif (jsk[i] <= threshold):
                if (inr):
                    lean.append(jsk[i])

                else:
                    lean = []
                    inr = True
                    lean.append(jsk[i])

        sumx = []
        jst = []
        for i in lean_periods:
            sumx.append([i[0], sum(i[1])])
            jst.append(sum(i[1]))

    # print(sumx)
        out=False
        jst.sort() 
        for p in range(len(jst)):
           if out is True:
             break
           minx = jst[p]
           lean_start = 0
           for i in sumx:
              if i[1] == minx:
                lean_start = i[0]
                if lean_start in predefined:
                  print('Conflicting with 5 mins nos upgrade of another swtich ')
                  continue
                
                else:
                   for i in range(1): 
                    predefined.append(lean_start+i)
                   out=True
                   break

        if out==False:
             raise Exception("asdf")        
        day(lean_start)



    except:
        print('Use Case2 -> Diverting traffic to the supporting switch')
        import pickle
        capacity = 10

        def nolag():

            print('NO LAG SUPPORTED -> SKIPPING TO USECASE 4')
            print('use case 4')
            threshold = float(input('Threshold'))
            atl = float(input("ATL"))
            ##########################################
            import pickle
            inr = False
            lean = []
            
            threshold = threshold+atl
            no_datas = 2016
            period_length = 6
            lean_periods = []
            PT = int(input('ENTER Priority Threshold'))
            threshold = threshold+atl
            with open("../PRED_"+switch+"/"+switch, "rb") as fp:   # Unpickling
                jsk = pickle.load(fp)

            with open("../Priority/P", "rb") as fp:   # Unpickling
                P = pickle.load(fp)

            try:

                for i in range(0, no_datas):
                    if (len(lean) == period_length):
                        lean_periods.append([i-6, lean])
                        lean = []
                        inr = False

                    if (jsk[i] > threshold or P[i] >= PT):
                        inr = False
                        lean = []
                    elif (jsk[i] <= threshold and P[i] <= PT):
                        if (inr):
                            lean.append(jsk[i])

                        else:
                            lean = []
                            inr = True
                            lean.append(jsk[i])

                sumx = []
                jst = []
                for i in lean_periods:
                    sumx.append([i[0], sum(i[1])])
                    jst.append(sum(i[1]))

    # print(sumx)
                out=False
                jst.sort() 
                for p in range(len(jst)):
                 if out is True:
                   break
                 minx = jst[p]
                 lean_start = 0
                 for i in sumx:
                  if i[1] == minx:
                   lean_start = i[0]
                   if lean_start in predefined:
                    print('Conflicting with 5 mins nos upgrade of another swtich ')
                   
                    continue
                   else:
                    for i in range(1): 
                     predefined.append(lean_start+i)
                    out=True
                    break
               
                if out==False:
                    raise Exception()   
                day(lean_start)

                

            except Exception as e:
                print(e)
                print('NO LEAN PERIOD FOUND !!!, RAISE THE THRESHOLD')

        lag = False
        if switch == 'S2':
            lag = 'S3'
        elif switch == 'S3':
            lag = 'S2'
        elif switch == 'S4':
            lag = 'S5'
        elif switch == 'S5':
            lag = 'S4'
        else:
            lag = False

        if lag == False:
            nolag()
            continue
            

        with open("../PRED_"+switch+"/"+switch, "rb") as fp:   # Unpickling
            sw = pickle.load(fp)

        with open("../PRED_"+lag+"/"+lag, "rb") as fp:   # Unpickling
            lg = pickle.load(fp)

        inr = False
        lean = []
        no_datas = 2016
        period_length = 6
        lean_periods = []
        try:

            for i in range(30, 2016):

                if (len(lean) == period_length):
                    lean_periods.append([i-6, lean])
                    lean = []
                    inr = False

                if (sw[i]+lg[i] > capacity):
                    inr = False
                    lean = []
                elif (sw[i]+lg[i] <= capacity):
                    if (inr):
                        lean.append(sw[i]+lg[i])

                    else:
                        lean = []
                        inr = True
                        lean.append(sw[i]+lg[i])

    # print(lean_periods)

            sumx = []
            jst = []
            for i in lean_periods:
                sumx.append([i[0], sum(i[1])])
                jst.append(sum(i[1]))

    # print(sumx)
            out=False
            jst.sort() 
            for p in range(len(jst)):
             if out is True:
               break
             minx = jst[p]
             lean_start = 0
             for i in sumx:
              if i[1] == minx:
                lean_start = i[0]
                if lean_start in predefined:
                  print('Conflicting with 5 mins nos upgrade of another swtich ')
                
                  continue
                else:
                   for i in range(1): 
                    predefined.append(lean_start+i)
                   out=True
                   break
            if out==False:
             raise Exception()       
            day(lean_start)
    

        except:
            print('No lean period found in usecase 2 -> Diverting Traffic with Acceptable Traffic Loss')
            import pickle
            ATL = float(input('ENTER ATL'))
            PT = int(input('ENTER Priority Threshold'))
            capacity = capacity+ATL

            with open("../PRED_"+switch+"/"+switch, "rb") as fp:   # Unpickling
                S2 = pickle.load(fp)

            with open("../PRED_"+lag+"/"+lag, "rb") as fp:   # Unpickling
                S3 = pickle.load(fp)

            with open("../Priority/P", "rb") as fp:   # Unpickling
                P = pickle.load(fp)

            inr = False
            lean = []
            no_datas = 2016
            period_length = 6
            lean_periods = []

            try:
                for i in range(30, 2016):

                    if (len(lean) == period_length):
                        lean_periods.append([i-6, lean])
                        lean = []
                        inr = False

                    if (S2[i]+S3[i] > capacity or P[i] >= PT):
                        inr = False
                        lean = []
                    elif (S2[i]+S3[i] <= capacity and P[i] <= PT):
                        if (inr):
                            lean.append(S2[i]+S3[i])

                        else:
                            lean = []
                            inr = True
                            lean.append(S2[i]+S3[i])
              

                sumx = []
                jst = []
                for i in lean_periods:
                    sumx.append([i[0], sum(i[1])])
                    jst.append(sum(i[1]))

    # print(sumx)
                out=False
                jst.sort() 
                for p in range(len(jst)):
                  if out is True:
                    break
                  minx = jst[p]
                  lean_start = 0
                  for i in sumx:
                    if i[1] == minx:
                     lean_start = i[0]
                     if lean_start in predefined:
                       print('Conflicting with 5 mins nos upgrade of another swtich ')
                
                       continue
                     else:
                         for i in range(1): 
                           predefined.append(lean_start+i)
                         out=True
                         break
                if out==False:
                  raise Exception()           
                day(lean_start)


            except:
                print('No time has been found for the upcoming week (13/2/23 to 19/2/23)')

print('Response To the SDN Controller')
print(API)
# root = Tk()
# text = Text(root)
# for i, j in API.items():
#     l = i+""+j
#     text.insert(INSERT, l + '\n')
# text.pack()
# root.mainloop()
