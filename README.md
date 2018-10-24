# URL_Shortner

Assuming that we are generating short-url's for a url with same domain name.  

step 1: To execute program from terminal run following commands:

        python URLShortner.py

Step 2: Enter URL to generate short-url

Step 3: Enter short-url genearted to get back original url

Logic:

Code generates a unique-id for the given url and this is converted to a base 64 number, using which a string is genarted. I'm appending this string to the end of the domain part of the url to get a shortned url string. 

A map is used to maintain the mapping between unique-id and originl-url

To get back the original-url for the given short url, code extract the short-string that was appended to the url and decodes it to get the ID. This ID is used to retrieve the original-url from the map. 






