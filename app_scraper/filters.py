class Filter(object):
    def __init__(self, rules=[]):
        self.filtered = {}
        self.rules = rules

    def by_dataset(self, data=[]):
        for item in data:
            for rule in self.rules:
                if rule.call(item):
                    self.filtered.setdefault(rule.type, []).append(item[rule.fetched_key])

        [self.filtered[rule.type].sort() for rule in self.rules]
        return self.filtered


class Rule(object):
    def __init__(self, type, fetched_key, with_rule=lambda item: True):
        self.with_rule = with_rule
        self.type = type
        self.fetched_key = fetched_key

    def call(self, data):
        return self.with_rule(data)
