#!/usr/local/bin/python3

import sys,os
sys.path.append(os.path.dirname(__file__) + 'cove/lib/')

import json, io
import glob
from cove.lib import common as c
import cove.lib.ocds as ocds

def validate():
    schema_url = 'http://ocds.open-contracting.org/standard/r/1__0__RC/release-package-schema.json'
    report = io.open('validations.json', 'w', encoding='utf-8')

    for filename in glob.glob('data/*.json'):
        with open(filename) as fp:
            error_list = c.get_schema_validation_errors(json.load(fp), schema_url, 'cove-ocds')
            error_list['name'] = filename
            report.write(json.dumps(error_list, ensure_ascii=False))

if __name__ == "__main__":
    validate()
