"""Classes for melon orders."""
class AbstractMelonOrder():
    """ An abstract melon class"""
    def __init__(self, species, qty, tax, order_type):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax
        self.order_type = order_type

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == 'Christmas melons':
            base_price = 1.5 * base_price
        
        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == 'international' and self.qty < 10:
            total += 3
        
        return round(total,2)

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    def __init__(self, species, qty):
        super().__init__(species, qty, 0.08, 'domestic')
        """Initialize melon order attributes."""
 
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, 0.17, 'international')
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""
        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government oder, no tax"""
    def __init__(self, species, qty, country_code = "USA"):
        self.country_code = country_code
        self.passed_inspection = False
        if country_code == 'USA':
            order_type = 'domestic'
        else: 
            order_type = 'international'
        super().__init__(species, qty, 0, order_type)

    def mark_inspection(self,passed):
         self.passed_inspection = passed


       

        
    
    