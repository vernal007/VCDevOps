import json

jsonstr = """{"People":
    [
        {
            "Id": "1",
            "Firstname": "Vernal",
            "Lastname": "Cooper",
            "Email": "vcooper@apdport.com",
            "Active": true
        },
        {
            "Id": "2",
            "Firstname": "John",
            "Lastname": "Doe",
            "Active": false
        },
        {
            "Id": "3",
            "Firstname": "John1",
            "Lastname": "Doe1",
            "Email": "jdoe1@apdport.com",
            "Active": true
        },
        {
            "Id": "4",
            "Firstname": "Giovanni",
            "Lastname": "Moncur",
            "Email": "gmoncur@apdport.com",
            "Active": true
        }

    ]
 }"""

jsonobj = json.loads(jsonstr)

print(jsonobj['People'])

jsonobj = json.load(open('test.json'))

print(jsonobj['People'])

