class CH_Shipping:

    def __int__(self, **kwargs):
        self.country = kwargs['country']
        self.channel = kwargs['channel']
        self.weight = kwargs['weight']
        self.shipping_cost = kwargs['shipping_cost']
        self.extra_charge = kwargs['extra_charge']

    def calculate_shipping(self, weight):
        return weight * self.shipping_cost + self.extra_charge

    def validation(self, calculate_data):
        if not self.weight[0] < calculate_data.weight < self.weight[1]:
            return False
        elif not self.channel == calculate_data.channel:
            return False
        elif not self.country == calculate_data.country:
            return False
        else:
            return True
