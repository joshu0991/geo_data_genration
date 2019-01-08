import random

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sep = ', '

lower_lat = 25.5
upper_lat = 50
lower_long = -66.6
upper_long = -125.1
upper_alt = 7000
lower_alt = 0
upper_error = 45
lower_error = 5
lower_timestamp = 1545283639 # Dec 20 2018 5:27:19 GMT
upper_timestamp = 1546925239 # Jan 8 2019 5:27:19 GMT
lower_duration = 10
upper_duration = 100

long_lat_delta_lower = -0.000011
long_lat_delta_upper = 0.000011
ts_delta_lower = 0
ts_delta_upper = 1000
duration_delta_lower = 0
duration_delta_upper = 1000

def gen_similar(total, cluster_size):
    ret_list = []
    # implicit floor
    for _ in range(int(total/cluster_size)):
        # generate first record for our basis
        #Lat log gen
        r = random.randint(0, 25)
        l = labels[r]
        lat = round(random.uniform(lower_lat, upper_lat), 6)
        long = round(random.uniform(lower_long, upper_long), 6)
        alt = round(random.uniform(lower_alt, upper_alt), 3)
        err = round(random.uniform(lower_error, upper_error), 2)
        ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
        duration = round(random.uniform(lower_duration, upper_duration), 0)
        s = l + sep + str(lat) + sep + str(long) + sep + str(alt) + sep + str(err) + sep + str(ts) + sep + str(duration)
        ret_list.append(s)

        for _ in range(cluster_size):
            # slightly randomly permuate the data so it is similar
            r = random.randint(0, 25)
            l = labels[r]
            lat_p = round(random.uniform(lower_lat, upper_lat), 6) + round(random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6)
            long_p = round(random.uniform(lower_long, upper_long), 6) + round(random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6)
            alt_p = round(random.uniform(lower_alt, upper_alt), 3) + round(random.uniform(0, 1), 2)
            err_p = round(random.uniform(lower_error, upper_error), 2) + round(random.uniform(0, 1), 2)
            ts_p = round(random.uniform(lower_timestamp, upper_timestamp), 0) + round(random.uniform(0, 1), 0)
            duration_p = round(random.uniform(lower_duration, upper_duration), 0) + round(random.uniform(duration_delta_lower, duration_delta_upper), 0)
            s = l + sep + str(lat_p) + sep + str(long_p) + sep + str(alt_p) + sep + str(err_p) + sep + str(ts_p) + sep + str(duration_p)
            ret_list.append(s)

    return ret_list

def gen_non_similar(total):
    ret_list = []
    # implicit floor
    for _ in range(int(total)):
        # generate first record for our basis
        #Lat log gen
        r = random.randint(0, 25)
        l = labels[r]
        lat = round(random.uniform(lower_lat, upper_lat), 6)
        long = round(random.uniform(lower_long, upper_long), 6)
        alt = round(random.uniform(lower_alt, upper_alt), 3)
        err = round(random.uniform(lower_error, upper_error), 2)
        ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
        duration = round(random.uniform(lower_duration, upper_duration), 0)
        s = l + sep + str(lat) + sep + str(long) + sep + str(alt) + sep + str(err) + sep + str(ts) + sep + str(duration)
        ret_list.append(s)
    return ret_list

def gen_data(total_points, cluster_size):
    f = open('geo_location_dataset.dat', 'w+')

    # implicit floor for div by 2
    similar = gen_similar(total_points/2, cluster_size)
    non_similar = gen_non_similar(total_points/2)

    for rec in similar:
        print(rec + sep + 's')
        f.write("{0}{1}s\n".format(rec, sep))

    for rec in non_similar:
        print(rec + sep + 'n')
        f.write("{0}{1}n\n".format(rec, sep))

    f.close()

gen_data(1000, 5)
