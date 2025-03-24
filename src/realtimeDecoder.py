#!/usr/bin/python3
import J2735_201603_2023_06_22
import socket
import argparse
import asyncio
import json
from binascii import unhexlify

counter = 0

def checkMessage(line):
    tempFrame = line[6:]
    if (len(tempFrame) > 510):
        frameSize = 8
        encodedSize = int(line[5:8], 16) * 2
    else:
        frameSize = 6
        encodedSize = int(line[4:6], 16) * 2

    newFrame = line[frameSize:]
    if (encodedSize == len(newFrame)):
        print("Valid message.")
        return True
    else:
        print("Not a valid message, continuing.")
        return False

def convertBytes(obj):
    if isinstance(obj, dict):
        return {k: convertBytes(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convertBytes(item) for item in obj]
    elif isinstance(obj, tuple):
        return [convertBytes(item) for item in obj]
    elif isinstance(obj, bytes):
        return obj.hex()
    else:
        return obj

def parse(data, seq):
    global counter
    msgIds=['0012','0013','0014'] # this can be updated to include other J2735 PSIDs
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
                cleanObj = convertBytes(seq())
                jsonString = json.dumps(cleanObj, indent=2)
                counter += 1
                print("Message ", counter)
                print(jsonString)

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
        data = str(sk_listen.recvfrom(10000)[0].hex())
        parse(data, seq)

if __name__=="__main__":
    asyncio.run(main())
