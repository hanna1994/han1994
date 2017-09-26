import json

reg = open('streets.txt', 'r')
data = False;
count = 0;
map = []
coordinates3 = []
for line in reg:
    if data and count > 0:
        tmp = line.rstrip('\n').split("\t")
        co_data=[];
        co_data.append(tmp[0]);
        co_data.append(tmp[1]);
        coordinates3.append(co_data);
        count = count - 1;
        if count == 0:
            coordinates3 = []
            data = False
    else :
        tmp = line.rstrip('\n').split("\t")
        code = tmp[0];
        count = int(tmp[1]);
        coordinates3 = [];
        map.append(coordinates3)
        data = True



featurexx = []
id = 1
for i in map: 
    feature = {};
    feature['type'] = 'Feature'
    feature['id'] = str(id)
    feature['properties'] = {"name": str(id)}
    id = id + 1
    geometry = {}
    feature['geometry'] = geometry
    geometry['type'] = 'LineString'
    coordinates = i
    geometry['coordinates'] = coordinates
    featurexx.append(feature)

ouput = {}
ouput["type"] = "FeatureCollection"
ouput['features']=featurexx
f=open('ouput.txt','w') 
f.write(json.dumps(ouput))
