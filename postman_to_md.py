#!/usr/bin/env python3

import sys
import json

def gest_error(code):
    print("ERROR !", code, file=sys.stderr)
    print("USAGE : ./postman_to_md.py <path_to_file> <output_file>\n")
    print("\t- path_to_file ->\tpath to the postman json collection")
    print("\t- output_file ->\tpath to the output file")
    exit(84)
    return

def write_info(info):
    to_write = ""
    to_write += "# " + info["name"] + "\n"
    to_write += info["description"] + "\n"
    to_write += "___________________________________________________________________\n"
    to_write += "# Requests\n"
    return to_write

def write_items(items):
    to_write = ""
    for elem in items:
        to_write += "### [" + elem["request"]["method"] + "] " + elem["name"] + "\n"
        to_write += "`" + elem["request"]["url"] + "`\n"
        to_write += "#### Headers\n"
        to_write += "|key|value|\n"
        to_write += "|---|-----|\n"
        for header in elem["request"]["header"]:
            to_write += "|" + header["key"] + "|`" + header["value"] + "`|\n"
        if ("urlencoded" in elem["request"]["body"]):
            to_write += "#### Body\n"
            to_write += "|key|value|\n"
            to_write += "|---|-----|\n"
            for node in elem["request"]["body"]["urlencoded"]:
                to_write += "|" + node["key"] + "|`" + node["value"] + "`|\n"
        if elem["response"] != "{}" and len(elem["response"]) > 0:
            to_write += "#### Sample Response\n"
            for res in elem["response"]:
                to_write += res["name"] + "\n"
                to_write += "```json\n" + json.dumps(json.loads(res["body"]), indent=4) + "\n```\n"
    return to_write

if len(sys.argv) < 3:
    gest_error("two arguments are expected")

try:
    f = open(sys.argv[1], "r")
except:
    gest_error("file could not be read")

file = f.read()
f.close()

data = json.loads(file)

to_write = ""
to_write += write_info(data["info"])
to_write += write_items(data["item"])

try:
    f = open(sys.argv[2], "w")
    f.write(to_write)
    f.close()
except:
    gest_error("file could not be open/written") 
