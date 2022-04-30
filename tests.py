from retirement_calculator import Retirement_Calculator


def main():
    test1 = Retirement_Calculator(25, 2000, 5700, 65, 5)
    assert f"{test1.total_savings:.2f}" == "281727.48"
    assert test1.annual_percentage() == 1.05
    assert test1.retirement_years() == 40
    assert test1.savings() == 40127.93565911055
    assert test1.__str__() == "You will have 281727.48 money when you retire at age 65."


if __name__ == "__main__":
    main()
