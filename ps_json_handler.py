from json import dump, load
from pprint import pprint as pp


def serialize_json():

    data = {
        '/etc/' : {
            'passwd': [1234, '13 Jan 2016'],
            'passwd1' : [1234, '13 Jan 2016'],
            'passwd2' : [1234, '13 Jan 2016']
        }
    }


    dump(data, open('temp.json', 'w'), indent=4)


#serialize_json()   # serialize json


# unserialize Json

pp(load(open('temp.json')))
print load(open('temp.json'))['/etc/']['passwd'][-1]