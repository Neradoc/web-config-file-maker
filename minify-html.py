#!/bin/env python3

import minify_html
import re
import sys


input_file = "js-file-maker.html"
config_file = "js-file-maker.js"

if len(sys.argv) == 2:
	input_file = sys.argv[1]
	config_file = re.sub("html?$","js",input_file)

config_include = f'<script src="{config_file}"></script>'

with open(input_file, "r") as fp:
	data = fp.read()

	html_ids = re.findall(r'id="([a-z_]+)"', data)
	html_ids = list(reversed(sorted(html_ids)))

	html_ids += [
		"make_form_auto",
		"submit_data",
		"colors_list",
		"_get_attr_",
		"_set_attr_",
	]
	print(html_ids)

	substitutes = []

	for index, id in enumerate(html_ids):
		repl = chr(65 + index)
		# repl = f"i{index}"
		data = re.sub(f'([^a-z_]){id}([^a-z_])', f'\\1{repl}\\2', data)
		# data = data.replace(f'id="{id}"', f'id="{repl}"')
		# data = data.replace(f'$("{id}")', f'$("{repl}")')
		# data = data.replace(f'#{id}', f'#{repl}')
		substitutes.append((repl, id))

	data = data.replace('"input_group"', '"G"')
	data = data.replace('"input_modes"', '"M"')
	data = data.replace('"target_input"', '"T"')

	with open(config_file, "r") as fp:
		config_data = "<script>" + fp.read() + "</script>"
		full_data = data.replace(config_include, config_data)

	output = minify_html.minify(
		data,
		minify_js=True,
		minify_css=True,
		remove_processing_instructions=True,
	)

	full_output = minify_html.minify(
		full_data,
		minify_js=True,
		minify_css=True,
		remove_processing_instructions=True,
	)

output = re.sub("> +<", "><", output)
output = re.sub("\t", "", output)
output = re.sub("let ", "", output)
output = re.sub("var ", "", output)

print(dict(substitutes))
print(f"Lengths: Mini = {len(output)} Full = {len(full_output)}")

output_file = input_file[:-5] + ".mini.html"
with open(output_file, "w") as fp:
	fp.write(output)

full_file = input_file[:-5] + ".setup.html"
with open(full_file, "w") as fp:
	fp.write(full_output)
