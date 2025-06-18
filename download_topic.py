import requests
import os

# Make sure this directory exists
os.makedirs("downloaded_threads", exist_ok=True)

# Your two cookies
cookies = {
    "_forum_session": "3OQBrswtML7kZEfFyik3ZZXKX7DY00TvPVcVqmBTcyERsfeW8NesObDZoCw7Kcayye9lR2PFtuAPMHjTON4fwNG1xyo0IjvGka9kSdk%2FrkHmQ7KO7fVIV6ia5eowUwCu4GMlm2a3clkaT9icbB2KS21MawaNunVwUb6hnISIDGbH2iFotOrCpHmdp3Ruk7LhNW1dv%2BRr4KvTsWXM7zLk%2FpA9l2c6RBo7URvJ8W7okut4wYpyWjqeDm7IuSWEJ7JZ0NxEyZAfdERfTrqnmkLg0gT4HaF0Ag%3D%3D--XdxG1a4N122NKuV9--iRukpNfLAa8gTP79B%2F9laA%3D%3D",
    "_t":         "JdDFmAZQzskmDsNdEi%2BLG%2FxZWA3JI7n3re7utpQjs63oblX0ODgoeZS4wVBoSKn5BJCvBBg2sNSDotp1PsevVD9NSSb9V94HpXTUG7JIwJLIlWjO92KMkJQKFc915NzbOy7smstbTTu96EAwKujhsJyb%2FSVi2gbQ6dmt%2FItqTM%2BeLBJL2etB2igqNMhJLvI%2FOCLoRTJrfvkHV0VqN%2BSyNebQDSsN5ok%2FkVGigNkh%2FUw%2F20X4T9Orw8HcKkNz1djgYU42%2FiAF09mh6fecip0LnVDRDEEKsz0r6g1mU2De49bnfg%2BZnJYchtz6XFJnwkbw--uxzOUY0xwcE9ZXWH--vXaVU9y0OVX1ifDmHLs5jw%3D%3D"
}

url = "https://discourse.onlinedegree.iitm.ac.in/t/155939.json"
r = requests.get(url, cookies=cookies, timeout=15)
r.raise_for_status()
with open("downloaded_threads/topic_155939.json", "wb") as f:
    f.write(r.content)
print("Saved topic_155939.json")
