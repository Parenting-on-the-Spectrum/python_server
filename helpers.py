# Format the leaders data to match the existing front end
def leader_format(input_data):
    result = []
    for entry in input_data:
        for e in entry:
          _id = str(entry[0])
          name = entry[1]
          postnomials = entry[2]
          picture = entry[3]
          priority = entry[4]
          bio = entry[5]

        formatted_entry = {
            "_id": _id,
            "name": name,
            "postnomials": postnomials,
            "picture": picture,
            "priority": priority,
            "bio": bio
        }

        result.append(formatted_entry)

    return result

def tip_format(input_data):
    transformed_data = []

    for item in input_data:
        transformed_item = {
            "_id": str(item[0]),
            "title": item[1],
            "info": item[2]
        }
        transformed_data.append(transformed_item)

    return transformed_data

def resource_format(input_data):
   return None