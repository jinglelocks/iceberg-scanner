def iceberg_scan(radar_file, lidar_file):
    start = time.time()
    raw_data = open(radar_file, 'r')
    data_array = numpy.loadtxt(raw_data, delimiter = ",")
    raw_data.close
    data_array = data_array.astype('int32')
    #print(data_array)
    #print(type(data_array))
    print("start of array check")
    print("dimensions of data array:",data_array.ndim)
    print("shape of data array:",data_array.shape) # make a check to see if they are the same shape
    #rows, columns = data_array.shape
    #print("# of rows:",rows)
    #print("# of columns:",columns)
    #print(data_array[data_array >= 100])
    result = numpy.where(data_array >= 100)
    #print(result)
    #result = numpy.where(data_array >= 0)
    #print("x values:",result[0])
    #print("y values:",result[1])
    #list_of_coords = list(zip(result[0], result[1]))
    #print(list_of_coords)
    #return list_of_coords
    volume = 0
    for i in range(len(result[0])):
        x = result[0][i]
        y = result[1][i]
        with open(lidar_file, 'r'):
            lidar_array = numpy.loadtxt(lidar_file, delimiter = ",")
            lidar_array = lidar_array.astype('int32')  
        height = lidar_array[x][y]
        #print(height_metres)
        volume = volume + height*1*1
    mass_above_water = volume*90 # Mass = volume*density/10
    mass_total = 10*mass_above_water
    print(mass_above_water,mass_total)
    total_volume = volume*10
    end = time.time()
    print(end-start) # This version: 70.96026253700256

        