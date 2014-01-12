from copy import deepcopy
SI=3
R=[' ',' ',' ',' ']
IC=0
IR=[' ',' ',' ',' ']
M=[]
M.append(deepcopy(R))
for a in range(0,100):
    M.append(deepcopy(R))
inputfile=open(r'E:\input.txt','r')
output=open(r'E:\output.txt','w')
C=False
def MOS():
    if(SI==1):
        READ()
    elif(SI==2):
        WRITE()
    elif(SI==3):
        TERMINATE()
def WRITE():
    global IR
    IR[3]='0'
    block=int(IR[2]+IR[3])
    for x in range(block,block+10):
        for y in range(0,4):
            print
            output.write(M[x][y])
    output.write('\n')
def TERMINATE():
    output.write('\n\n')
    LOAD()
def READ():
    global M
    global IR
    block=int(IR[2]+IR[3])
    IR[3]='0'
    datacard=inputfile.readline()
    if(datacard.endswith('\n')):
        datacard=datacard[0:len(datacard)-1]
    if(datacard=='$END'):
        TERMINATE()
    else:
        for count in range(len(datacard),40):
            datacard+=' '
        datacard=list(datacard)
        for count in range(0,10):
            M[block]=deepcopy(datacard[4*count:4*count+4])
            block+=1
def EXECUTEUSERPROGRAM():
    global IC
    global IR
    while(True):
        IR=deepcopy(M[IC])
        IC+=1
        if(IR[0]+IR[1]=='LR'):
            R=deepcopy(M[int(IR[2]+IR[3])])
        elif(IR[0]+IR[1]=='SR'):
            M[int(IR[2]+IR[3])]=deepcopy(R)
        elif(IR[0]+IR[1]=='CR'):
            if(R==M[int(IR[2]+IR[3])]):
                C=True
            else:
                C=False
        elif(IR[0]+IR[1]=='BT'):
            if(C):
                IC=int(IR[2]+IR[3])
        elif(IR[0]+IR[1]=='GD'):
            global SI
            SI=1
            MOS()
        elif(IR[0]+IR[1]=='PD'):
            SI=2
            MOS()
        elif(IR[0]=='H'):
            SI=3
            MOS()
def STARTEXECUTION():
    global IC
    IC=0
    EXECUTEUSERPROGRAM()
def LOAD():
    pointer=0
    inputfeed=inputfile.readline()
    while(inputfeed):
        if(inputfeed.endswith('\n')):
            inputfeed=inputfeed[0:len(inputfeed)-1]
        if(inputfeed.startswith("$AMJ") or inputfeed.startswith("$DTA") or inputfeed.startswith("$END")):
            '''if(inputfeed=='$AMJ'):
                break'''
            if(inputfeed=='$DTA'):
                STARTEXECUTION()
            elif(inputfeed=='$END'):
                output.close()
                exit(0)
        else:
            if(pointer==100):
                exit(0)
            else:
                for count in range(len(inputfeed),40):
                    inputfeed+=' '
                inputfeed=list(inputfeed)
                for count in range(0,10):
                    M[pointer]=deepcopy(inputfeed[4*count:4*count+4])
                    pointer+=1
        inputfeed=inputfile.readline()
LOAD()
inputfile.close()
