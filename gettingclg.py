a = [['RVSR Pg for Gents', 'Old Mahabalipuram Road, Kelambakkam, Kelambakkam', 1264, 'yes', 'no', 1], ['GTR Luxury Gents Pg', 'Rajiv Gandhi Salai, Padur, Thiruporur 603103', 1793, 'no', 'no', 1], ['Prof Dhanapalan College Of Hostel', 'Fourrts Avenue, Kelambakkam, Thiruporur 603103', 3359, 'yes', 'yes', 1], ['Jothi Gents Hostel', 'Rajiv Gandhi Salai, Padur, Thiruporur 603103', 3551, 'yes', 'yes', 1], ['K Abhiram Gents Hostel', 'Rajiv Gandhi Salai, Padur, Thiruporur 603103', 2939, 'yes', 'yes', 3]]
b = ['Name','Address','Price','Wifi','Parking','Rating']
for i in range(len(a)):
    for j in range(len(b)):
        print(a[i][j])