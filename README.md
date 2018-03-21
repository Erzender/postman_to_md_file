# postman_to_md_file
I wasn't able to find a working script to build a markdown file out of a Postman collection to document over my API, so I made my own using the power of ugly code that works.

At least it works with v2 collections, and urlencoded body in requests. I don't know when it fails yet, feel free to leave me some feedback if you'd like me to provide a better version, ha.
## Run
`./postman_to_md.py <path_to_postman_collection> <output_file> `
