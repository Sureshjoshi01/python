# Write a code to generate random secure token of 64 bytes and random URL

import secrets 

print(secrets.token_hex(64))

passwordresetlink = "demo.com/customer/eric/reset="
passwordresetlink += secrets.token_urlsafe(64)
print(passwordresetlink)