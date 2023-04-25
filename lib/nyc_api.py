import requests
import json

class GetPrograms:

  def get_programs():
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    return response.content
  
  def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list


# programs = GetPrograms.get_programs()
# print(programs)
programs = GetPrograms()
programs_schools = GetPrograms.program_school(GetPrograms)

for school in set(programs_schools):
    print(school)