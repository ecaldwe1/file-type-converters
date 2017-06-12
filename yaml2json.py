#!/usr/bin/env python
#
# This file is a standalone package intended to be used on a variety of different projects.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# https://github.com/ecaldwe1/file-type-converters
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License (MPL), version 2.0.  If a copy of the MPL was not distributed
# with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import json
import sys
import yaml

# sys.stdout.write(json.dumps(yaml.load(sys.stdin), sort_keys=True, indent=2))

print("----------------------- BEGINNING YAML CONVERT TO JSON -----------------------")

input_yaml_file = sys.argv[1]

# with open(input_yaml_file) as yaml_data:
loaded_yaml = yaml.load(input_yaml_file)
    # if len(sys.argv) == 3:
    #     output_yaml_file = sys.argv[2]
    #     yaml_file = open(output_yaml_file, 'w+')
    # else:
    #     extension_index = input_json_file.find('.json')
    #     new_yaml_filename = input_json_file[:7] + '.yml'
    #     yaml_file = open(new_yaml_filename, 'w+')
    # ydump = yaml.safe_dump(loaded_json, yaml_file, allow_unicode=False,
    #                        default_flow_style=False, indent=2, canonical=True)
    # yaml_file.close()
    # json_data.close()
    #
    # print "Converted " + input_json_file + " to " + new_yaml_filename + "!"

print("----------------------- JSON DUMP COMPLETE -----------------------------------")

# python -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=4)' < helloworld.yml > helloworld.json