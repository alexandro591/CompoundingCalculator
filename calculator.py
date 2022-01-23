class CompoundingCalculator:
  """
  inits the compounding calculator based which can calculate and predict your total savings
  in n number of years based on smart decistions made monthly and yearly
  """
  def __init__(
    self,
    savings,
    monthly_savings,
    anual_percentage_yield,
    monthly_percentage_yield,
    export_to_excel=True
  ):
    self.savings = savings
    self.monthly_savings = monthly_savings
    self.anual_percentage_yield = anual_percentage_yield
    self.monthly_percentage_yield = monthly_percentage_yield
    self.export_to_excel = export_to_excel
  
  def calculate_apy_interest_in_one_year(self):
    return self.anual_percentage_yield*self.savings
  
  def calculate_mpy_interest_in_one_year(self):
    result = 0
    for year in range(0, 12):
      result += (result + year*self.monthly_savings + self.calculate_apy_interest_in_one_year()/12)*self.monthly_percentage_yield
    return result

  def calculate_total_savings_historic_in_n_years(self, years):
    historic = {
      "years": [],
      "monthly_average_interest": [],
      "yearly_interest_plus_savings": [],
      "total_savings": []
    }
    for year in range(1, years + 1):
      yearly_savings = self.monthly_savings*12
      yearly_interest = self.calculate_mpy_interest_in_one_year() + self.calculate_apy_interest_in_one_year()
      yearly_savings_plus_interest = yearly_savings + yearly_interest
      self.savings += yearly_savings_plus_interest

      historic["years"].append(year)
      historic["monthly_average_interest"].append(yearly_interest/12)
      historic["yearly_interest_plus_savings"].append(yearly_savings_plus_interest)
      historic["total_savings"].append(self.savings)

    return historic

  @staticmethod
  def calculator_historic_logger(historic):
    for index, year in enumerate(historic["years"]):
      print(
        "year:",
        year,
        ",  monthly_average_interest:",
        "%.2f" % historic["monthly_average_interest"][index],
        ",  yearly_interest_plus_savings:",
        "%.2f" % historic["yearly_interest_plus_savings"][index],
        ",  total_savings:",
        "%.2f" % historic["total_savings"][index]
      )

  def calculate_for_n_years(self, years):
    historic = self.calculate_total_savings_historic_in_n_years(years)
    CompoundingCalculator.calculator_historic_logger(historic)
    if self.export_to_excel:
      import pandas as pd
      df = pd.DataFrame(historic)
      df.to_excel("output.xlsx", index=False)
