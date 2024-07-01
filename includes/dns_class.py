from nslookup import Nslookup

class dns_lookup:
    def __init__(self, domain, dns_server_list=[]):
        self.domain = domain
        with open("includes/dns_list.txt") as file:
            self.dns_list_default = [line.rstrip() for line in file]
        self.full_dns_list = dns_server_list + self.dns_list_default

    def check_dns(self):
        final_dict = {}
        counter = 1
        
        for dns in self.full_dns_list:
            print(f"Check DNS: {dns} -> ({counter} - {len(self.full_dns_list)})")
            dns_query = Nslookup(dns_servers=[dns], verbose=True, tcp=False)
            ip_record = dns_query.dns_lookup(self.domain)
            final_dict[dns] = ip_record.answer[:2]
            counter += 1

        return final_dict

