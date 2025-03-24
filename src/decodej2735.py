#!/usr/bin/python3
import J2735_201603_2023_06_22
import json
from binascii import unhexlify

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

def main():
    print('Press <Ctrl+C> to exit\n')
    while(1):
        payload = input('Enter your J2735 Payload:\n')
        decode = J2735_201603_2023_06_22.DSRC.MessageFrame
        decode.from_uper(unhexlify(payload))
        cleanObj = convertBytes(decode())
        jsonString = json.dumps(cleanObj, indent=2)
        print(jsonString)


if __name__=="__main__":
    main()
