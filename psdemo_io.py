try:
    name = raw_input('enter the name : ')
    city = raw_input('enter the city : ')
    zip_code = int(raw_input('enter the postal zip : '))

    print 'name : ' , name
    print 'city : ' , city
    print 'zip_code :', zip_code

except ValueError as err:
    print err
