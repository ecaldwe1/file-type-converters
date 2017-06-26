#!/usr/bin/env python
#
# This file is a standalone package intended to be used to convert between file types.
# Written @ University of Notre Dame, June 2017
#
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

tempdir = tempfile.mkdtemp()
fd, temp_path = tempfile.mkstemp(prefix='json2yaml_log_', dir=tempdir)

logging.basicConfig(filename=temp_path, filemode='w', level=logging.DEBUG)

logging.info("----------------------- BEGINNING JSON CONVERT TO YAML -----------------------")

input_json_file = sys.argv[1]

with open(input_json_file) as json_data:
    # Try to load the json from the input file. Fails if input file is not a valid json.
    try:
        loaded_json = json.load(json_data)
    except ValueError:
        logging.debug("ERROR:  Input file is not valid JSON! Please try again with a valid JSON file.")
        sys.exit(1)

    # If output file is not provided, use same name as input file
    new_yaml_filename = ""
    if len(sys.argv) == 3:
        output_yaml_file = sys.argv[2]
        new_yaml_filename = output_yaml_file

    else:
        extension_index = input_json_file.find('.json')
        new_yaml_filename = input_json_file[:extension_index] + '.yml'

    logging.info("Creating new file " + new_yaml_filename)
    yaml_file = open(new_yaml_filename, 'w+')

    # Dump the json into a yaml file
    ydump = yaml.safe_dump(loaded_json, yaml_file, allow_unicode=False,
                           default_flow_style=False, indent=2, canonical=True)

    # Close both the input and output files
    yaml_file.close()
    json_data.close()

    logging.info("Converted " + input_json_file + " to " + new_yaml_filename + "!")

logging.info("----------------------- YAML DUMP COMPLETE -----------------------------------")
