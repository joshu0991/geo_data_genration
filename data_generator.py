import random

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sep = ','

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

long_lat_delta_lower = 0
long_lat_delta_upper = 0.000011
ts_delta_lower = 0
ts_delta_upper = 1000
duration_delta_lower = 0
duration_delta_upper = 1000

def gen_similar(total, cluster_size):
    ret_list = []
    # implicit floor
    counter = 0
    for _ in range(int(total/cluster_size)):
        # generate first record for our basis
        #Lat log gen
        r = random.randint(0, 25)
        lab = labels[r]
        lat = round(random.uniform(lower_lat, upper_lat), 6)
        long = round(random.uniform(lower_long, upper_long), 6)
        alt = round(random.uniform(lower_alt, upper_alt), 3)
        err = round(random.uniform(lower_error, upper_error), 2)
        ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
        duration = round(random.uniform(lower_duration, upper_duration), 0)
        s = lab + sep + str(lat) + sep + str(long) + sep + str(alt) + sep + str(err) + sep + str(ts) + sep + str(duration) + sep + 's' + str(counter)
        ret_list.append(s)

        for _ in range(cluster_size):
            # slightly randomly permuate the data so it is similar
            r = random.randint(0, 25)
            lab = labels[r]
            lat_p = round(lat + round(random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
            long_p = round(long + round(random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
            alt_p = round(alt + round(random.uniform(0, 1), 2), 2)
            err_p = round(err + round(random.uniform(0, 1), 2), 2)
            ts_p = int(ts + round(random.uniform(0, 1), 0))
            duration_p = int(duration + round(random.uniform(duration_delta_lower, duration_delta_upper), 0))
            s = lab + sep + str(lat_p) + sep + str(long_p) + sep + str(alt_p) + sep + str(err_p) + sep + str(ts_p) + sep + str(duration_p) + sep + 's' + str(counter)
            ret_list.append(s)
        counter = counter + 1
    return ret_list

def gen_non_similar(total):
    ret_list = []
    # implicit floor
    for _ in range(int(total)):
        # generate first record for our basis
        #Lat log gen
        r = random.randint(0, 25)
        lab = labels[r]
        lat = round(random.uniform(lower_lat, upper_lat), 6)
        long = round(random.uniform(lower_long, upper_long), 6)
        alt = round(random.uniform(lower_alt, upper_alt), 3)
        err = round(random.uniform(lower_error, upper_error), 2)
        ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
        duration = round(random.uniform(lower_duration, upper_duration), 0)
        s = lab + sep + str(lat) + sep + str(long) + sep + str(alt) + sep + str(err) + sep + str(ts) + sep + str(duration) + sep + 'n'
        ret_list.append(s)
    return ret_list

def gen_longterm_data(total_points, cluster_size):
    f = open('longterm_geo_location_dataset.dat', 'w+')

    # implicit floor for div by 2
    similar = gen_similar(total_points/2, cluster_size)
    non_similar = gen_non_similar(total_points/2)

    for rec in similar:
        print(rec)
        f.write("{0}\n".format(rec))

    for rec in non_similar:
        print(rec)
        f.write("{0}\n".format(rec))

    f.close()

def gen_person(label, points_per_person, long, lat, counter):
    ret_list = []
    for _ in range(points_per_person):
        lat_p = round(lat + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        long_p = round(long + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        alt_p = round(round(random.uniform(lower_alt, upper_alt), 3) + round(random.uniform(0, 1), 2), 2)
        err_p = round(round(random.uniform(lower_error, upper_error), 2) + round(random.uniform(0, 1), 2), 2)
        ts_p = int(round(random.uniform(lower_timestamp, upper_timestamp), 0) + round(random.uniform(0, 1), 0))
        duration_p = int(round(random.uniform(lower_duration, upper_duration), 0) + round(
            random.uniform(duration_delta_lower, duration_delta_upper), 0))
        s = label + sep + str(lat_p) + sep + str(long_p) + sep + str(alt_p) + sep + str(err_p) + sep + str(
            ts_p) + sep + str(duration_p) + sep + 's' + str(counter)
        ret_list.append(s)
    return ret_list

def gen_recent_data(total_points, cluster_size, points_per_person):
    f = open('recent_geo_location_dataset_small.dat', 'w+')

    for _ in range(int(total_points / cluster_size)):
        lat = round(random.uniform(lower_lat, upper_lat), 6)
        long = round(random.uniform(lower_long, upper_long), 6)
        for counter in range(cluster_size):
            r = random.randint(0, 25)
            l = labels[r]
            person_list = gen_person(l, points_per_person, long, lat, counter)
            for person in person_list:
                print(person)
                f.write("{0}\n".format(person))

    f.close()

def gen_routine_and_anamoly(long, lat, total, l):
    # Typical routine for person l
    ret_list = []
    lat_1 = round(lat + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
    long_1 = round(long + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
    lat_2 = round(lat + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
    long_2 = round(long + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
    lat_3 = round(lat + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
    long_3 = round(long + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
    lat_4 = round(lat + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
    long_4 = round(long + round(
        random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)

    ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)

    for i in range(total):
        lat_1 = round(lat + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        long_1 = round(long + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        lat_2 = round(lat + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        long_2 = round(long + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        lat_3 = round(lat + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        long_3 = round(long + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        lat_4 = round(lat + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)
        long_4 = round(long + round(
            random.uniform(long_lat_delta_lower, long_lat_delta_upper), 6), 6)

        # We go to each of the 4 every day four hours apart
        s1 = l + sep + str(lat_1) + sep + str(long_1) + sep + str(ts)
        ts = ts + 14400
        ret_list.append(s1)
        s2 = l + sep + str(lat_2) + sep + str(long_2) + sep + str(ts)
        ts = ts + 14400
        ret_list.append(s2)
        s3 = l + sep + str(lat_3) + sep + str(long_3) + sep + str(ts)
        ts = ts + 28800
        ret_list.append(s3)
        s4 = l + sep + str(lat_4) + sep + str(long_4) + sep + str(ts)
        ts = ts + 14400
        ret_list.append(s4)

    # make a few anamolies
    lat_a = round(random.uniform(lower_lat, upper_lat), 6)
    long_a = round(random.uniform(lower_long, upper_long), 6)
    ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
    s5 = l + sep + str(lat_a) + sep + str(long_a) + sep + str(ts)
    ret_list.append(s5)
    lat_a = round(random.uniform(lower_lat, upper_lat), 6)
    long_a = round(random.uniform(lower_long, upper_long), 6)
    ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
    s5 = l + sep + str(lat_a) + sep + str(long_a) + sep + str(ts)
    ret_list.append(s5)
    lat_a = round(random.uniform(lower_lat, upper_lat), 6)
    long_a = round(random.uniform(lower_long, upper_long), 6)
    ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
    s5 = l + sep + str(lat_a) + sep + str(long_a) + sep + str(ts)
    ret_list.append(s5)
    lat_a = round(random.uniform(lower_lat, upper_lat), 6)
    long_a = round(random.uniform(lower_long, upper_long), 6)
    ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
    s5 = l + sep + str(lat_a) + sep + str(long_a) + sep + str(ts)
    ret_list.append(s5)

    lat_a = round(lat + round(
        random.uniform(long_lat_delta_lower+2, long_lat_delta_upper+2), 6), 6)
    long_a = round(long + round(
        random.uniform(long_lat_delta_lower+2, long_lat_delta_upper+2), 6), 6)
    ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
    s5 = l + sep + str(lat_a) + sep + str(long_a) + sep + str(ts)
    ret_list.append(s5)

    lat_a = round(lat + round(
        random.uniform(long_lat_delta_lower+1, long_lat_delta_upper+1), 6), 6)
    long_a = round(long + round(
        random.uniform(long_lat_delta_lower+1, long_lat_delta_upper+1), 6), 6)
    ts = round(random.uniform(lower_timestamp, upper_timestamp), 0)
    s5 = l + sep + str(lat_a) + sep + str(long_a) + sep + str(ts)
    ret_list.append(s5)
    return ret_list

def gen_single_person(total_points):
    f = open('pol_recent_geo_location_dataset_small.dat', 'w+')
    r = random.randint(0, 25)
    l = labels[r]
    lat = round(random.uniform(lower_lat, upper_lat), 6)
    long = round(random.uniform(lower_long, upper_long), 6)
    points = gen_routine_and_anamoly(long, lat, total_points, l)

    for point in points:
        print(point)
        f.write("{0}\n".format(point))


    f.close()
gen_single_person(20)

#gen_recent_data(25, 3, 2)

#gen_longterm_data(1000, 5)
