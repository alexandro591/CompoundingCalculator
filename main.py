import calculator

def main():
  c = calculator.CompoundingCalculator(
    savings=120000,
    monthly_savings=10000,
    anual_percentage_yield=0.09,
    monthly_percentage_yield=0.04/12,
    export_to_excel=True
  )
  c.calculate_for_n_years(6)

if __name__ == "__main__":
  main()