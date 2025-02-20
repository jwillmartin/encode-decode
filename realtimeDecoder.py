#!/usr/bin/python3
import J2735_201603_2023_06_22
import socket
import argparse
import asyncio
from binascii import unhexlify


def checkMessage(line):
    print("Line: ", line)
    tempFrame = line[6:]
    print("Bytes Size: ", len(tempFrame))
    if (len(tempFrame) > 510):
        frameSize = 8
        encodedSize = int(line[5:8], 16) * 2
    else:
        frameSize = 6
        encodedSize = int(line[4:6], 16) * 2

    print("Size encoded in message: ", encodedSize)
    print("Checking against frame size starting at index: ", frameSize)
    newFrame = line[frameSize:]
    print("Frame under test: ", newFrame)
    print("Frame size: ", len(newFrame))
    if (encodedSize == len(newFrame)):
        print("Valid message, continuing.")
        return True
    else:
        print("Not a valid message, skipping.")
        return False
    
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
    payload = str(hexPayload).strip('b\'')

    if (payload[:4] == "0014"):
        fixedBSM = fixBSMID(seq, strId)

        return fixedBSM

    elif (payload[:4] == "001f"):
        fixedTIM = fixTIMID(seq, strId)

        return fixedTIM

    elif (payload[:4] == "00f4"):
        reqid = seq()['value'][1]['body'][1]['reqid']
        newReqId = str(convID(reqid, 8))

        begID = strId.find("b'") + 2
        endID = strId.find("'", begID)
        newString = strId[:begID-2] + newReqId + strId[endID+1:]

        return newString

    elif (payload[:4] == "00f5"):
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

def parse(data, seq):
    msgIds=['0014'] # this can be updated to include other J2735 PSIDs
    for id in msgIds:
        idx = data.find(id)
        if (idx != -1):
            data = data[idx:].strip('\n')
            print("Found: ", data)
            validity = checkMessage(data)
        
            if (validity == True):
                try:
                    seq.from_uper(unhexlify(data))
                except: continue
                decodedStr = str(seq())

                # If no issues with decoding, print
                if "b'" not in decodedStr: 
                    print(decodedStr, '\n')

                # Decoding issues found, fix and update message
                else: 
                    print('\n', fix(data, seq, decodedStr), '\n')
            else: continue

async def main():
    parser = argparse.ArgumentParser(description='Script to decode J2735 V2X Messages as they are received over UDP')
    parser.add_argument('--ip', help='IP address to receive data.', type=str, default="127.0.0.1") 
    parser.add_argument('--port', help='Port to receive data.', type=int, default=5398)
    args = parser.parse_args()

    sk_listen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk_listen.bind((args.ip, args.port))

    seq = J2735_201603_2023_06_22.DSRC.MessageFrame
    print('Press <Ctrl+C> to exit\n')
    while(1):
        parse(str(sk_listen.recvfrom(10000)[0].hex()), seq)

if __name__=="__main__":
    asyncio.run(main())
