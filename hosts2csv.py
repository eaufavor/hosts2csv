import sys

domains = {}

for line in sys.stdin:
    line = line.rstrip()
    if not line or line.startswith("#"):
        continue
    line = line.split()
    if not line[1] or "." not in line[1]:
        continue
    domain = line[1]

    suffix = "." + domain
    dots = domain.split(".")
    root = dots[-2] + "." + dots[-1]

    subs = domains.get(root, {})
    skip = False
    for d, v in subs.items():
        if not v:
            continue
        if domain.endswith("." + d):
            # domain is subdomain of d
            skip = True
            break
        if d.endswith(suffix):
            # d is subdomain of domain
            subs[d] = False

    if not skip:
        subs[domain] = True
    domains[root] = subs

for _, subs in domains.items():
    for domain, v in subs.items():
        if v:
            print(f"{domain}")
