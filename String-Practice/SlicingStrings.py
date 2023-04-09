# Author: Norm McCord
# Taken from slides at KSU

# Take a slice of a string (a span of characters from the sentence) and print Known as a substring format: string[
# start : end] Will return a string containing a copy of the characters from INCLUDING the starting index,
# and up to BUT NOT INCLUDING the ending point.  If start is not specified, the 0 index will be assumed.  If end is
# not specified, len(string) will be assumed as the end.

#-------------------------------------

# Write a program to verify a URL
# URL must:
# - start with a protocol (http or https or ftp)
# - contain '://' after the protocol
# - MAY contain 'www.' before the domain
# - contain a domain
# - end with any of the following TLDs:
#     .com, .org, .edu, .de, .net, .cn, .uk, .info, .nl, .eu, .ru

dom_ex = ["com", "org", "edu", "de", "net", "cn", "uk", "info", "nl", "eu", "ru", "ca"]
url = "https://www.google.com/search?q=python+find%28%29+nth+occurance&rlz=1C1CHBD_enUS1030US1030&ei=9qwtZPzXB92uqtsP2oSuiAw&ved=0ahUKEwj8qrqjn5P-AhVdl2oFHVqCC8EQ4dUDCA8&uact=5&oq=python+find%28%29+nth+occurance&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQHhANMgYIABAeEA0yBggAEB4QDTIICAAQigUQhgMyCAgAEIoFEIYDOgQIABBHSgQIQRgAUI0dWM8eYKAjaABwAngAgAFtiAHBAZIBAzEuMZgBAKABAcgBCMABAQ&sclient=gws-wiz-serp"
start_index = 0
print(url)
if url.startswith("http://"):
    start_index = 7
    print("URL has a valid protocol")
elif url.startswith("https://"):
    start_index = 8
    print("URL has a valid protocol")
elif url.startswith("ftp://"):
    start_index = 6
    print("URL has a valid protocol")
else:
    print("URL doesn't contain a valid protocol")

# check for extension
slash = url.find("/", start_index) # find the first occurrence of the slash
if slash != -1: # if we find it
    url = url[0:slash] # grab only the part of the string we care about
p = url.split(".")
has_ext = False
for e in dom_ex:          # For each extension in the array...
    if p[len(p)-1].startswith(e):
        has_ext = True

if has_ext:
    print("URL has a valid extension")
else:
    print("URL doesn't have a valid extension")

# check for a domain
p = url.split(".")
print(f"Domain is: ", p[len(p)-2])

# check for 'www'
if "://www" in url:
    print("URL contains 'www'")
else:
    print("URL doesn't contain 'www'")