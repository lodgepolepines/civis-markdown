import civis
import json
import os


def main():
    number = '40000K'

    json_value_dict = {
        'number': number
    }
    post_json_run_output(json_value_dict)


def post_json_run_output(json_value_dict):
    client = civis.APIClient()
    json_value_object = client.json_values.post(
        json.dumps(json_value_dict),
        name='email_outputs')
    client.scripts.post_python3_runs_outputs(
        os.environ['CIVIS_JOB_ID'],
        os.environ['CIVIS_RUN_ID'],
        'JSONValue',
        json_value_object.id)


if __name__ == '__main__':
    main()