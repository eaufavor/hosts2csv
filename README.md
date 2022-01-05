# Convert hosts files to CSV format
Convert hosts files to CSV format in order to upload as Cloudflare for Teams host lists.
It drops subdomains if their parent domain exists in the hosts file already.

Example:
```
curl https://someonewhocares.org/hosts/zero/hosts  |  python3 hosts2csv.py  > hosts.csv
```
To split the file in to smaller files:
```
split hosts.csv -l 1000 --additional-suffix=.csv -d
```