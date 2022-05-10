/*
One item per line. Item format:

title:key:placeholder:group

- title is the displayed name of the entry in the UI
- key is the key name in the final dict
- placeholder is the value displayed in the placeholder
- group contains "?" if the item is optional
- group contains "#" if the item is a checkbox
- group is a group name if the group is optional

If placeholder is the word "true" for a checkbox, it's checked by default
Optional items are not listed if the value is empty.
Optional groups are not listed if no item in it has a value.

To make an item a popup menu (html SELECT) add an entry in select_fields below.
The entry is named field_ + the name of the field (as defined in the list above).
The value is a list of possible values for the field, starting with the empty string if the field is optional.
*/
var fields = `
WiFi SSID:ssid:home:
WiFi Password:password:password01:
Time Zone:timezone::?
Hide Drive:hide_drive::#?
Enable HID:enable_hid:True:#
Adafruit IO User:aio_username:Username:aio
Adafruit IO key:aio_key:bfa67934:aio
Open Weather Token:openweather_token:c1332f68:ow
Open Weather Location:openweather_location:Paris, FR:ow

`;
var select_fields = {
	field_timezone: ["Europe/Paris", "Europe/Berlin", "Canada/London"],
}
