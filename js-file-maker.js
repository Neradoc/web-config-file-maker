/*
One field per line. Field format:

title:key:placeholder:group

- title is the displayed name of the entry in the UI
- key is the key name in the final dict
- placeholder is the value displayed in the placeholder
- a group name with letters makes the fields appear grouped with colors
- group contains "?" if the field is optional
- group contains "#" if the field is a checkbox
- group contains "$" if the field is a number
- group contains "+" if the field is required

If placeholder is the word "true" for a checkbox, it's checked by default.
Non-optional fields are filled with their default value if empty.
Optional fields are not listed if the value is empty.
Required fields show an error message if they are empty.
All fields in a group are listed if any field is listed.

NOTE: a field can be optional and required, but it makes no sense, so don't do that.

To make an item a popup menu (html SELECT) add an entry in select_fields below.
The entry is named field_ + the name of the field (as defined in the list above).
The value is a list of possible values for the field, starting with the empty string if the field is optional.
*/
var file_name = "secrets.py"
var file_prefix = "secrets = {\n"
var file_suffix = "}\n"
var line_format = '  "${name}": ${value},\n'
var value_true = "True"
var value_false = "False"

/*
var file_name = "config.txt"
var file_prefix = ""
var file_suffix = ""
var line_format = '${name} = ${value}\n'
*/

var fields = `
WiFi SSID:ssid:home:wifi+
WiFi Password:password:password01:wifi
Time Zone:timezone::
Hide Drive:hide_drive::#?
Enable HID:enable_hid:True:#
Adafruit IO User:aio_username:Username:aio?
Adafruit IO key:aio_key:bfa67934:aio?
Open Weather Token:openweather_token:c1332f68:ow
Open Weather Location:openweather_location:Paris, FR:ow

`;
var select_fields = {
	field_timezone: ["Europe/Paris", "Europe/Berlin", "Canada/London"],
}
