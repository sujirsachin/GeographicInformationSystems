import arcpy

fc="major_roads"
out="C:\\Users\\sujir\\OneDrive\\Documents\\ArcGIS\\Projects\\lab06\\"
distance_list=["100 meters","200 meters","300 meters"]

for dist in distance_list:
    outname=out+fc+"_"+dist[0:3]
    print("Now Buffering: "+outname)
    arcpy.Buffer_analysis(fc,outname,dist,"","","ALL")
    
print ("Finished Buffering")