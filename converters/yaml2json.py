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
import logging
import sys
import tempfile
import yaml

fd, temp_path = tempfile.mkstemp(prefix='yaml2json_log_', suffix='.log')

logging.basicConfig(filename=temp_path, filemode='w', level=logging.DEBUG)

logging.info("----------------------- BEGINNING YAML CONVERT TO JSON -----------------------")

input_yaml_file = sys.argv[1]

with open(input_yaml_file) as yaml_data:
    # Try to load the yaml from the input file. Fails if error in yaml file.
    try:
        loaded_yaml = yaml.load(yaml_data)
    except yaml.YAMLError, e:
        logging.debug("YAML Error in file: ", e)
        sys.exit(1)

    # If output file is not provided, use same name as input file
    new_json_filename = ""
    if len(sys.argv) == 3:
        output_json_file = sys.argv[2]
        new_json_filename = output_json_file

    else:
        extension_index = 0
        if input_yaml_file.find('.yaml') != -1:
            extension_index = input_yaml_file.find('.yaml')
        elif input_yaml_file.find('.yml') != -1:
            extension_index = input_yaml_file.find('.yml')
        new_json_filename = input_yaml_file[:extension_index] + '.json'

    logging.info("Creating new file " + new_json_filename)
    json_file = open(new_json_filename, 'w+')

    # Dump the yaml into a json file
    logging.info(loaded_yaml)
    jdump = json.dump(loaded_yaml, json_file, indent=2)

    # Close both the input and output files
    yaml_data.close()
    json_file.close()

    logging.info("Converted " + input_yaml_file + " to " + new_json_filename + "!")

logging.info("----------------------- JSON DUMP COMPLETE -----------------------------------")
