import requests
import json
def json_out():
    #payload = {'user':fsayyed, 'password': secret}
    #payload = {'page': 2, 'count': 25}
    output = requests.get('https://jsonplaceholder.typicode.com/users')
    #output = requests.get('https://httpbin.org/get', params=payload)
    json_formatted = output.json()
    # with open('json.txt', 'w') as f:
    #     f.write(json_formatted)
    return (json_formatted)

def parse_results():
    json_output = json_out()

    final_result = []
    for data in json_output:
        # result = '{} - {} - {}'.format(data['name'],data['phone'],data['address']['street'])
        result = f"{data['name']} - {data['phone']} - {data['address']['street']}"
        #final_result.append(result)
    #return (final_result)
        geo_output = 'geo: {0}, {1}'.format(data['address']['geo']['lat'],data['address']['geo']['lng']) #+ '\n'#['geo']#['lat'] + ',' + data['geo']['lng']
        #data =
       # print('{0}\n{1}\n'.format(result,geo_output))


s = json_out()
# print(s)
# print(json.dumps(s, indent=2))
parse_results()
#print(sorted(s))
# for i in s:
#     print(i)