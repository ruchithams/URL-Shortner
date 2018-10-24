# URL_Shortner

Assuming that we are generating short-URLs for a URL with the same domain name.

step 1: To execute the program from terminal run following commands:

        python URLShortner.py

Step 2: Enter URL to generate short-URL

Step 3: Enter short-URL generated to get back original URL

Logic:

The code generates a unique-id for the given URL and this is converted to a base 64 number, using which a string is generated. I'm appending this string to the end of the domain part of the URL to get a shortened URL string.

A map is used to maintain the mapping between unique-id and original-URL

To get back the original-URL for the given short URL, code extracts the short-string that was appended to the URL and decodes it to get the ID. This ID is used to retrieve the original-URL from the map. 






