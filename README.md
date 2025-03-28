These scripts encode and decode SAE J2735 messages in JSON to/from UPER-encoded Hex.
The encoder accepts either single or double-quotes, seen below with examples.
Developed using linux. Can also be used in Windows.

## Prerequisites:
Run the install_dependencies.sh script to install all dependencies. 
```
cd install
sudo ./install_dependencies.sh
```

## Encoder Usage:
1. `./encodeJ2735.py`
2. Paste the sequence in the terminal when prompted
3. Hex string will be printed

## Decoder Usage:
1. `./decodeJ2735.py`
2. Paste the Hex string in the terminal when prompted
3. Decoded message will be printed

## Realtime Decoder Usage:
1. `./realtimeDecode.py -h`
2. Enter the IP Address and Port for where to receive messages.
3. The contents of the file will be decoded and printed as messages are received.


## Examples:
Example SPAT message:
```
{"messageId": 19, "value": ("SPAT", {"intersections": [{"id": {"id": 5813}, "revision": 1, "status": (0, 16), "moy": 137825, "states": [{"signalGroup": 7, "state-time-speed": [{"eventState": "permissive-clearance", "timing": {"startTime": 0, "minEndTime": 40, "maxEndTime": 40, "likelyTime": 40, "confidence": 15, "nextTime": 0}}]}]}]})}
```

Example BSM message:
```
{'messageId': 20, 'value': ('BasicSafetyMessage', {'coreData': {'msgCnt': 1, 'id': f03ad610, 'secMark': 38283, 'lat': 389549439, 'long': -771489145, 'elev': 72, 'accuracy': {'semiMajor': 200, 'semiMinor': 200, 'orientation': 100}, 'transmission': 'park', 'speed': 0, 'heading': 22454, 'angle': 10, 'accelSet': {'long': 0, 'lat': 0, 'vert': -127, 'yaw': 0}, 'brakes': {'wheelBrakes': (16, 5), 'traction': 'off', 'abs': 'off', 'scs': 'off', 'brakeBoost': 'off', 'auxBrakes': 'off'}, 'size': {'width': 300, 'length': 500}}})}
```

Example TIM message:
```
{'messageId': 31, 'value': ('TravelerInformation', {'msgCnt': 1, 'packetID': 122345567827b582a6, 'dataFrames': [{'sspTimRights': 0, 'frameType': 'advisory', 'msgId': ('roadSignID', {'position': {'lat': 389549832, 'long': -771491828, 'elevation': 390}, 'viewAngle': (65535, 16), 'mutcdCode': 'warning'}), 'startYear': 2023, 'startTime': 339600, 'duratonTime': 1, 'priority': 5, 'sspLocationRights': 0, 'regions': [{'anchor': {'lat': 389549832, 'long': -771491828, 'elevation': 390}, 'laneWidth': 366, 'directionality': 'both', 'closedPath': False, 'direction': (65535, 16), 'description': ('path', {'offset': ('xy', ('nodes', [{'delta': ('node-LatLon', {'lon': -771491667, 'lat': 389549796})}, {'delta': ('node-LatLon', {'lon': -771488227, 'lat': 389549384}), 'attributes': {'dElevation': 10}}]))})}], 'sspMsgRights1': 0, 'sspMsgRights2': 0, 'content': ('advisory', [{'item': ('itis', 7186)}])}]})}
```

Example MAP message:
```
{'messageId': 18, 'value': ('MapData', {'msgIssueRevision': 3, 'layerType': 'intersectionData', 'layerID': 1, 'intersections': [{'id': {'id': 9709}, 'revision': 3, 'refPoint': {'lat': 389549844, 'long': -771493239, 'elevation': 390}, 'laneWidth': 274, 'laneSet': [{'laneID': 1, 'ingressApproach': 1, 'laneAttributes': {'directionalUse': (2, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': -523, 'y': -1294}), 'attributes': {'dElevation': 10}}, {'delta': ('node-XY2', {'x': -360, 'y': -724})}, {'delta': ('node-XY3', {'x': -622, 'y': -1111})}, {'delta': ('node-XY2', {'x': -209, 'y': -654})}, {'delta': ('node-XY2', {'x': 76, 'y': -579})}, {'delta': ('node-XY1', {'x': 366, 'y': -509})}]), 'connectsTo': [{'connectingLane': {'lane': 6}, 'signalGroup': 2}, {'connectingLane': {'lane': 7}, 'signalGroup': 2}, {'connectingLane': {'lane': 8}, 'signalGroup': 2}]}, {'laneID': 5, 'egressApproach': 5, 'laneAttributes': {'directionalUse': (1, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': -965, 'y': -1056}), 'attributes': {'dElevation': 10}}, {'delta': ('node-XY2', {'x': -250, 'y': -527})}, {'delta': ('node-XY2', {'x': -378, 'y': -781})}, {'delta': ('node-XY2', {'x': -244, 'y': -619})}, {'delta': ('node-XY1', {'x': -174, 'y': -428})}, {'delta': ('node-XY2', {'x': 29, 'y': -729})}])}, {'laneID': 6, 'egressApproach': 6, 'laneAttributes': {'directionalUse': (1, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': 1523, 'y': -518})}, {'delta': ('node-XY2', {'x': 581, 'y': -133})}, {'delta': ('node-XY3', {'x': 1035, 'y': -162}), 'attributes': {'dElevation': 10}}, {'delta': ('node-XY2', {'x': 953, 'y': -122})}, {'delta': ('node-XY2', {'x': 709, 'y': -41})}, {'delta': ('node-XY3', {'x': 1360, 'y': -98}), 'attributes': {'dElevation': 10}}])}, {'laneID': 2, 'ingressApproach': 2, 'laneAttributes': {'directionalUse': (2, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': 1604, 'y': -182})}, {'delta': ('node-XY2', {'x': 593, 'y': -139})}, {'delta': ('node-XY2', {'x': 924, 'y': -139})}, {'delta': ('node-XY2', {'x': 837, 'y': -110}), 'attributes': {'dElevation': 10}}, {'delta': ('node-XY2', {'x': 872, 'y': -93})}, {'delta': ('node-XY3', {'x': 1348, 'y': -64}), 'attributes': {'dElevation': 10}}]), 'connectsTo': [{'connectingLane': {'lane': 5}, 'signalGroup': 4}, {'connectingLane': {'lane': 7}, 'signalGroup': 4}, {'connectingLane': {'lane': 8}, 'signalGroup': 4}]}, {'laneID': 7, 'egressApproach': 7, 'laneAttributes': {'directionalUse': (1, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': 872, 'y': 1363})}, {'delta': ('node-XY1', {'x': 232, 'y': 498})}, {'delta': ('node-XY2', {'x': 308, 'y': 805}), 'attributes': {'dElevation': -10}}, {'delta': ('node-XY2', {'x': 331, 'y': 741})}, {'delta': ('node-XY2', {'x': 250, 'y': 712})}])}, {'laneID': 3, 'ingressApproach': 3, 'laneAttributes': {'directionalUse': (2, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': 506, 'y': 1467})}, {'delta': ('node-XY2', {'x': 349, 'y': 735})}, {'delta': ('node-XY2', {'x': 372, 'y': 897}), 'attributes': {'dElevation': -10}}, {'delta': ('node-XY2', {'x': 285, 'y': 683})}, {'delta': ('node-XY1', {'x': 215, 'y': 480})}]), 'connectsTo': [{'connectingLane': {'lane': 5}, 'signalGroup': 2}, {'connectingLane': {'lane': 6}, 'signalGroup': 2}, {'connectingLane': {'lane': 8}, 'signalGroup': 2}]}, {'laneID': 8, 'egressApproach': 8, 'laneAttributes': {'directionalUse': (1, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': -1540, 'y': 703})}, {'delta': ('node-XY2', {'x': -715, 'y': 214})}, {'delta': ('node-XY2', {'x': -808, 'y': 359})}, {'delta': ('node-XY2', {'x': -587, 'y': 272})}, {'delta': ('node-XY1', {'x': -511, 'y': 255})}])}, {'laneID': 4, 'ingressApproach': 4, 'laneAttributes': {'directionalUse': (2, 2), 'sharedWith': (0, 10), 'laneType': ('vehicle', (0, 0))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': -1651, 'y': 368})}, {'delta': ('node-XY1', {'x': -465, 'y': 139})}, {'delta': ('node-XY2', {'x': -651, 'y': 208})}, {'delta': ('node-XY2', {'x': -639, 'y': 232})}, {'delta': ('node-XY2', {'x': -750, 'y': 313})}, {'delta': ('node-XY2', {'x': -761, 'y': 492})}]), 'connectsTo': [{'connectingLane': {'lane': 5}, 'signalGroup': 4}, {'connectingLane': {'lane': 6}, 'signalGroup': 4}, {'connectingLane': {'lane': 7}, 'signalGroup': 4}]}, {'laneID': 9, 'laneAttributes': {'directionalUse': (0, 2), 'sharedWith': (0, 10), 'laneType': ('crosswalk', (0, 16))}, 'nodeList': ('nodes', [{'delta': ('node-XY2', {'x': -1023, 'y': -634}), 'attributes': {'dElevation': 10}}, {'delta': ('node-XY2', {'x': 808, 'y': -365})}])}, {'laneID': 10, 'laneAttributes': {'directionalUse': (0, 2), 'sharedWith': (0, 10), 'laneType': ('crosswalk', (0, 16))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': 1343, 'y': 43})}, {'delta': ('node-XY2', {'x': -134, 'y': -550})}])}, {'laneID': 11, 'laneAttributes': {'directionalUse': (0, 2), 'sharedWith': (0, 10), 'laneType': ('crosswalk', (0, 16))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': 238, 'y': 1213})}, {'delta': ('node-XY2', {'x': 593, 'y': -203})}])}, {'laneID': 12, 'laneAttributes': {'directionalUse': (0, 2), 'sharedWith': (0, 10), 'laneType': ('crosswalk', (0, 16))}, 'nodeList': ('nodes', [{'delta': ('node-XY3', {'x': -1174, 'y': 738})}, {'delta': ('node-XY2', {'x': -157, 'y': -515})}])}]}]})}
```
