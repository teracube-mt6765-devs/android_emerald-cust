#!/usr/bin/env python3
"""
Copyright (C) 2022 Gagan Malvi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Program-intention: Clone device trees according to elements in trees.json
"""

import json
import os

root_dir = "../../"
tree_json = "trees.json"


def return_json_object(json_file):
    try:
        return json.load(open(json_file))
    except:
        print("Error: Unable to open json file")
        exit(1)


def clone_trees(tree_object):
    for (node, value) in tree_object.items():
        git_cmd = "git clone "
        git_cmd += value["url"] + " "
        git_cmd += root_dir + value["path"] + " "
        if "branch" in value:
            git_cmd += "--branch " + value["branch"] + " "
        if "depth" in value:
            git_cmd += "--depth=" + str(value["depth"])
        print("Cloning " + node + " tree...")
        os.system(git_cmd)


# Get JSON object
tree = return_json_object(tree_json)

# Set a few variables
branch = tree["branch"]
fallback_branch = tree["fallback_branch"]
organization = tree["organization"]
gh_org = tree["github_organization"]
codename = tree["codename"]
platform = tree["platform"]

trees_data = {
    "device": {
        "url": "https://github.com/"
        + gh_org
        + "/"
        + "android_device_"
        + organization
        + "_"
        + codename,
        "path": "device/" + organization + "/" + codename,
    }
}

if tree["is_vendorless"] == False:
    name = "android_vendor_" + organization + "_" + codename
    trees_data.update(
        {
            "vendor": {
                "url": "https://github.com/" + gh_org + "/" + name,
                "path": "vendor/" + organization + "/" + codename,
            }
        }
    )

if tree["uses_prebuilt_kernel"] == True:
    name = "android_device_" + organization + "_" + codename + "-kernel"
    trees_data.update(
        {
            "kernel": {
                "url": "https://github.com/" + gh_org + "/" + name,
                "path": "device/" + organization + "/" + codename + "-kernel",
            }
        }
    )
elif tree["custom_kernel"] == True:
    print(
        "Target has specified custom kernel usage. Checking additional repos for a kernel repository..."
    )
    if "kernel" in tree["additional_trees"]:
        print("Kernel repo found, appending as is...")
        trees_data.update({"kernel": tree["additional_trees"]["kernel"]})
else:
    print("Kernel source assumed kernel/vendor/device, appending")
    name = "android_kernel_" + organization + "_" + codename
    trees_data.update(
        {"kernel": {"url": name, "path": "kernel/" + organization + "/" + codename}}
    )

if tree["clone_sepolicy"] == True:
    if "sepolicy" in tree["additional_trees"]:
        print("Sepolicy mentioned in additional_trees, appending")
        trees_data.update({"sepolicy": tree["additional_trees"]["sepolicy"]})
    else:
        print("Assuming device/platform/sepolicy, appending")
        name = "android_device_" + platform + "_" + "sepolicy"
        trees_data.update(
            {
                "sepolicy": {
                    "url": "https://github.com/" + gh_org + "/" + name,
                    "path": "device/" + platform + "/sepolicy",
                }
            }
        )

if "gms" in tree["additional_trees"]:
    print("Target has GMS specified. Using as is.")
    trees_data.update({"gms": tree["additional_trees"]["gms"]})


# Work
clone_trees(trees_data)
