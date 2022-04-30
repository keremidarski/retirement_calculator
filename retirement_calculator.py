class RetirementCalculator:
    def __init__(
        self,
        current_age,
        yearly_contribution,
        current_savings,
        retirement_age,
        annual_return,
    ):
        self.current_age = current_age
        self.yearly_contribution = yearly_contribution
        self.current_savings = current_savings
        self.retirement_age = retirement_age
        self.annual_return = annual_return
        self.years_until_retirement = self.retirement_years()
        self.total_savings = self.savings()
        self.calculate()

    def calculate(self):
        while self.years_until_retirement > 0:
            self.years_until_retirement -= 1
            self.total_savings += self.earnings()

    def annual_percentage(self):
        return (self.annual_return / 100) + 1

    def retirement_years(self):
        return self.retirement_age - self.current_age

    def savings(self):
        return self.current_savings * (
            self.annual_percentage() ** self.retirement_years()
        )

    def earnings(self):
        return self.yearly_contribution * (
            self.annual_percentage() ** self.years_until_retirement
        )

    def __str__(self):
        return f"{self.total_savings:.2f}"
