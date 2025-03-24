#!/usr/bin/python3
import J2735_201603_2023_06_22
import ast
import subprocess
import signal, sys
from binascii import hexlify

def signal_handler(sig, frame):
    print('\nExiting')
    sys.exit(0)

def bsmFix(updatedMsg):
    idPos = updatedMsg.find("\"id\":") + 6
    idEnd = updatedMsg.find(", ", idPos+1)
    toFix = updatedMsg[idPos:idEnd]
    byte = str(bytes.fromhex(toFix))
    msgFix = updatedMsg[:idPos] + byte + updatedMsg[idEnd:]
    return msgFix

def timFix(updatedMsg):
    idPos = updatedMsg.find("\"packetID\":") + 12
    idEnd = updatedMsg.find(", ", idPos+1)
    toFix = updatedMsg[idPos:idEnd]
    byte = str(bytes.fromhex(toFix))
    msgFix = updatedMsg[:idPos] + byte + updatedMsg[idEnd:]
    return msgFix

def main():
    print('\nPress <Ctrl+C> to exit\n\n')

    while(1):
        subprocess.check_call(["stty","-icanon"])
        msgIn = input('Enter your JSON J2735 message:\n')
        updatedMsg = msgIn.replace("\'", "\"")
        updatedMsg = updatedMsg.strip("\n")
        if (updatedMsg[14:16] == "20"):
            updatedMsg = bsmFix(updatedMsg)
        elif (updatedMsg[14:16] == "31"):
            updatedMsg = timFix(updatedMsg)

        print("\n", len(updatedMsg), ": ", updatedMsg, "\n")
        msg = ast.literal_eval(updatedMsg)
        msgFrame = J2735_201603_2023_06_22.DSRC.MessageFrame
        msgFrame.set_val(msg)
        print(msgFrame)
        msgFrameUper = msgFrame.to_uper()
        print(msgFrameUper)
        encodedMsg = hexlify(msgFrameUper)
        print("\nEncoded Hex:\n", encodedMsg, "\n")
        subprocess.check_call(["stty","icanon"])

if __name__=="__main__":
    main()

signal.signal(signal.SIGINT, signal_handler)
print('\n<Ctrl+C> to exit')
signal.pause()
