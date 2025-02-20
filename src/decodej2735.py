#!/usr/bin/python3

## Classic J2735 Payload Decoder - Single Message
import J2735_201603_2023_06_22
import signal, sys
from binascii import unhexlify

def signal_handler(sig, frame):
    print('\nExiting')
    sys.exit(0)
    
def fixBSMID(seq, bsm):
    bsmId = seq()['value'][1]['coreData']['id']
    bsmId = bsmId.hex()

    begID = bsm.find("b'") + 2
    endID = bsm.find("'", begID)
    newString = bsm[:begID-2] + str(bsmId) + bsm[endID+1:]

    return newString

def fixTIMID(seq, tim):
    timId = seq()['value'][1]['packetID']
    timId = timId.hex()

    if "b\'" in tim:
        begID = tim.find('b\'') + 2
        endID = tim.find('\'', begID)
    else:
        begID = tim.find('b\"') + 2
        endID = tim.find('\"', begID)

    newString = tim[:begID-2] + str(timId) + tim[endID+1:]

    return newString
    
def convID(id, length):
    id = id.hex()
    i = 0
    if (length == 8):
        while(i<21):
            id = id[:i+2] + " " + id[i+2:]
            i += 3
    else:
        while(i<45):
            id = id[:i+2] + " " + id[i+2:]
            i += 3

    id = list(id.split(" "))

    for x in range(len(id)):
        inted = int(id[x], 16)
        id[x] = inted

    return id

def fix(hexPayload, seq, strId):
    if (hexPayload[:4] == "0014"):
        fixedBSM = fixBSMID(seq, strId)

        return fixedBSM

    elif (hexPayload[:4] == "001f"):
        fixedTIM = fixTIMID(seq, strId)

        return fixedTIM

    elif (hexPayload[:4] == "00f4"):
        reqid = seq()['value'][1]['body'][1]['reqid']
        newReqId = str(convID(reqid, 8))

        begID = strId.find("b'") + 2
        endID = strId.find("'", begID)
        newString = strId[:begID-2] + newReqId + strId[endID+1:]

        return newString

    elif (hexPayload[:4] == "00f5"):
        reqid = seq()['value'][1]['body'][1]['reqid']
        tcmId = seq()['value'][1]['body'][1]['id']
        tcId = seq()['value'][1]['body'][1]['package']['tcids'][0]
        newReqId = str(convID(reqid, 8))
        newTcmId = str(convID(tcmId, 16))
        newtcId = str(convID(tcId, 16))
        newIds = [newReqId, newTcmId, newtcId]

        for b in range(len(newIds)):
            begID = strId.find("b'") + 2
            endID = strId.find("'", begID)
            strId = strId[:begID-2] + newIds[b] + strId[endID+1:]

        return strId
    
    else:
        print("ID fix not included in filters yet. Unfixed message:\n")
        print(strId, "\n")


def main():

    print('Press <Ctrl+C> to exit\n\n')

    while(1):
        payload = input('Enter your J2735 Payload:\n')
        decode = J2735_201603_2023_06_22.DSRC.MessageFrame
        decode.from_uper(unhexlify(payload))
        decodedStr = str(decode())
        print("\n", decodedStr, '\n')

        # if no issues with decoding, print
        if 'b\'' not in decodedStr:
            if 'b\'' not in decodedStr:
                print("\n", decodedStr, '\n')

        # decoding issues found, fix and update message
        else:
            msgFix = fix(payload, decode, decodedStr)
            print("\n", msgFix, "\n")

if __name__=="__main__":
    main()
       
signal.signal(signal.SIGINT, signal_handler)
print('Press <Ctrl+C> to exit\n\n')
signal.pause()
