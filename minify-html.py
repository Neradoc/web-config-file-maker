#!/bin/env python3

import minify_html
import re
import sys

if len(sys.argv) != 2:
	print("What file ?")
	sys.exit(1)

config_include = '<script src="js-file-maker.js"></script>'
config_file = "js-file-maker.js"

input_file = sys.argv[1]
with open(input_file, "r") as fp:
	data = fp.read()

	html_ids = re.findall(r'id="([a-z_]+)"', data)
	html_ids = list(reversed(sorted(html_ids)))

	html_ids += ["make_form_auto", "submit_data", "colors_list"]
	print(html_ids)

	for index, id in enumerate(html_ids):
		repl = chr(65 + index)
		# repl = f"i{index}"
		data = re.sub(f'([^a-z_]){id}([^a-z_])', f'\\1{repl}\\2', data)
		# data = data.replace(f'id="{id}"', f'id="{repl}"')
		# data = data.replace(f'$("{id}")', f'$("{repl}")')
		# data = data.replace(f'#{id}', f'#{repl}')

	data = data.replace('"input_group"', '"gg"')
	data = data.replace('"input_modes"', '"mm"')
	data = data.replace('"target_input"', '"tt"')

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

print(f"Lengths: Mini = {len(output)} Full = {len(full_output)}")

output_file = input_file[:-5] + ".mini.html"
with open(output_file, "w") as fp:
	fp.write(output)

full_file = input_file[:-5] + ".setup.html"
with open(full_file, "w") as fp:
	fp.write(full_output)
