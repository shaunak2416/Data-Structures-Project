import gmplot



with open("Hospitalnames.txt","r") as hospfile:
    hosplist = hospfile.read().splitlines()

    

for j in range (len(hosplist)):
    with open("OutputFile "+hosplist[j]+".txt","r") as fd:
        lines = fd.read().splitlines()
    lat_list = []
    lon_list = []
    for i in range(len(lines)):
        if(i==0):
            user_lat = float((lines[i].split(" "))[0])
            user_lon = float((lines[i].split(" "))[1])
            continue
        elif(i==len(lines)-1):
            hlat = float((lines[i].split(" "))[0])
            hlon = float((lines[i].split(" "))[1])
            continue
        else:
            lat_list.append(float((lines[i].split(" "))[0]))
            lon_list.append(float((lines[i].split(" "))[1]))

        gmap = gmplot.GoogleMapPlotter(18.5308,73.8475,13)
        gmap.scatter(lat_list,lon_list,"#FF0000", size=5, marker=False)
        gmap.plot(lat_list,lon_list,'cornflowerblue', edge_width = 2.5)

        gmap.draw("output "+hosplist[j]+".html")

