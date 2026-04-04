class Contract:
    def __init__(self):
        self.domains = {}

    def register_domain(self, domain, record_type, value, owner):
        self.domains[domain] = {
            "value": value,
            "owner": owner
        }
        return True

    def update_domain(self, domain, new_value, owner):
        if domain in self.domains and self.domains[domain]['owner'] == owner:
            self.domains[domain]['value'] = new_value
            return True
        return False

    def transfer_ownership(self, domain, new_owner, current_owner):
        if domain in self.domains and self.domains[domain]['owner'] == current_owner:
            self.domains[domain]['owner'] = new_owner
            return True
        return False

contract = Contract()