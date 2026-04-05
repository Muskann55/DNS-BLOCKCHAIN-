class Contract:
    def __init__(self):
        # store domain records
        self.records = {}

    def register_domain(self, domain, record_type, value, owner):
        self.records[domain] = {
            "record_type": record_type,
            "value": value,
            "owner": owner
        }

    def get_record(self, domain):
        # 🔥 THIS WAS MISSING
        return self.records.get(domain)

    def verify_transaction(self, record):
        # simple validation
        return True


# global instance
contract = Contract()