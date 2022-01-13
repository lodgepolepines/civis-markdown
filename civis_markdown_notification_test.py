import civis
import json
import os

number = '40000K'

json_value_dict = {
    'number': number
}

client = civis.APIClient()
json_value_object = client.json_values.post(
    json.dumps(json_value_dict),
    name='email_outputs')
client.scripts.post_containers_runs_outputs(
    os.environ['CIVIS_JOB_ID'],
    os.environ['CIVIS_RUN_ID'],
    'JSONValue',
    json_value_object.id)

print(os.environ['CIVIS_JOB_ID'])
print(os.environ['CIVIS_RUN_ID'])
print(json_value_object.id)