class TaxRatio:
    def __init__(self, lower_bound, upper_bound, ratio, coupon):
        self.min = lower_bound
        self.max = upper_bound
        self.ratio = ratio
        self.coupon = coupon
        
class FccKingTax:
    MAX_SALARY = 1000 * 1000 * 1000
    TAX_RATIO = [TaxRatio(0, 36000, 0.03, 0),
                 TaxRatio(36000 + 1, 144000, 0.1, 2520),
                 TaxRatio(144000 + 1, 300000, 0.2, 16920),
                 TaxRatio(300000 + 1, 420000, .25, 31920),
                 TaxRatio(420000 + 1, 660000, .3, 52920),
                 TaxRatio(660000 +1, 960000, .35, 85920),
                 TaxRatio(960000 +1, MAX_SALARY, .45, 181920)]
    TAX_THRESHOLD = 5000

    TAX_RATIO_BEFORE_2019 = [
        TaxRatio(0, 1500, 0.03, 0),
        TaxRatio(1500 + 1, 4500, .1, 105),
        TaxRatio(4500 + 1, 9000, .2, 555),
        TaxRatio(9000 + 1, 35000, .25, 1005),
        TaxRatio(35000 + 1, 55000, .3, 2755),
        TaxRatio(55000 + 1, 80000, .35, 5505), 
        TaxRatio(80000 + 1, MAX_SALARY, .45, 13505)
    ]
    
    def __init__(self, old_ratio=.08, medical_ratio=.02, 
                 unemployment_ratio=.005, 
                 house_funding_ratio=.07, 
                 insurance_upper_bound=31014,
                 house_found_upper_bound=31014):
        self.three_insurance_ratio = old_ratio + medical_ratio + unemployment_ratio
        self.house_funding_ratio = house_funding_ratio
        self.insurance_upper_bound = insurance_upper_bound
        self.house_found_upper_bound = house_found_upper_bound
        
    @classmethod
    def get_tax_ratio(cls, should_tax, new=True):
        ratios = cls.TAX_RATIO if new else cls.TAX_RATIO_BEFORE_2019
        for tax_ratio in ratios:
            if tax_ratio.min <= should_tax <= tax_ratio.max:
                return tax_ratio
        raise ValueError('Fail to find tax ratio for {}'.format(should_tax))

    def get_social_money(self, salary):
        insurance_base = self.insurance_upper_bound if salary > self.insurance_upper_bound else salary
        house_funding_base = self.house_found_upper_bound if salary > self.house_found_upper_bound else salary
        return insurance_base * self.three_insurance_ratio + house_funding_base * self.house_funding_ratio
        
    def get_new_tax(self, salary, taxfree):
        social_money = self.get_social_money(salary)
        total_tax_free = social_money + self.TAX_THRESHOLD + taxfree

        if salary <= total_tax_free:
            print('You Win!')
            return [0 for _ in range(12)]
        
        res = list()
        for i in range(1, 13):
            already_taxed = sum(res)
            should_tax = (salary - total_tax_free) * i
            tax_ratio = self.get_tax_ratio(should_tax)
            tax = should_tax * tax_ratio.ratio - already_taxed - tax_ratio.coupon
            tax = round(tax)
            res.append(tax)
        return res


if __name__ == '__main__':
    ft = FccKingTax()
    salary = 50000
    income = salary * 12
    tax_per_month = ft.get_new_tax(salary, 3000)
    total_tax = sum(tax_per_month)
    tax_ratio = total_tax/(salary * 12)
    tax_ratio = round(tax_ratio, 3)
    print(f"income: {income}")
    print(f"tax per month: {tax_per_month}")
    print(f"total tax of year: {total_tax}")
    print(f"total ratio: {tax_ratio}")
