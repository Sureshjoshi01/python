# Exercise 8: Check whether following json is valid or invalid. If Invalid correct it
import json 

data = '''
{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}
'''

def json_validate(jsondata):
    try:
        json.loads(jsondata)
    except ValueError as err:
        return False
    return True

print("is data a valid json : ",json_validate(data))

