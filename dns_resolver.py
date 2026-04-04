from smart_contract import contract

class DNSResolver:
    def __init__(self):
        # store resolved records (for /all endpoint)
        self.records = {}

    def resolve(self, domain, record_type='A'):
        """
        Resolve domain to IP
        """
        record = contract.get_record(domain)

        if record:
            # optional verification (safe check)
            if record.get('record_type') == record_type:
                if contract.verify_transaction(record):
                    value = record.get('value')

                    # store for viewing all records
                    self.records[domain] = value

                    return value

        return None

    def audit(self, domain):
        """
        Optional audit (safe fallback)
        """
        try:
            from blockchain import blockchain
            return blockchain.audit_trail(domain)
        except:
            return "Audit not available"


# Global instance
resolver = DNSResolver()