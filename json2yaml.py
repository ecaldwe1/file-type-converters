#!/usr/bin/env python
#
# This file is a standalone package intended to be used on a variety of different projects.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# https://github.com/ecaldwe1/file-type-converters

import json
import sys
import yaml

print("----------------------- BEGINNING JSON CONVERT TO YAML -----------------------")

input_json_file = sys.argv[1]

with open(input_json_file) as json_data:
    loaded_json = json.load(json_data)
    if len(sys.argv) == 3:
        output_yaml_file = sys.argv[2]
        yaml_file = open(output_yaml_file, 'w+')
    else:
        extension_index = input_json_file.find('.json')
        new_yaml_filename = input_json_file[:7] + '.yml'
        yaml_file = open(new_yaml_filename, 'w+')
    ydump = yaml.safe_dump(loaded_json, yaml_file, allow_unicode=False,
                           default_flow_style=False, indent=2, canonical=True)
    yaml_file.close()
    json_data.close()

    print "Converted " + input_json_file + " to " + new_yaml_filename + "!"

print("----------------------- YAML DUMP COMPLETE -----------------------------------")
