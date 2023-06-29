import dns.resolver


def return_records(target: str, record_type: str):

    try:
        records = dns.resolver.resolve(target, record_type)

    except dns.resolver.NoAnswer as e:
        print(" - ", record_type, "records were not found for", target)
        return

    except dns.resolver.NXDOMAIN as n:
        print("The provided domain (" + target + ") was not found.")
        return

    for record in records:
        print(" - ", record)
