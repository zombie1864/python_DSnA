""" This class provides an API that allows one to calculate the number of months that are needed to 
save up for a downpayment on a house based on the user's salary, total cost of the house, 
annual return, and the percentage of the total cost needed for a downpayment.

It also takes into account that your salary will be adjusted every 6 months by some percentage. 

The main algorithm should be implemented in the `months` method which takes the percentage that you wish 
to save and returns the number of months that is required given the configuration.


1. The total cost is the cost of the house.
2. The percent_down_payment is the portion of the cost needed for a down payment. 
3. The algo should start with a current savings value of zero and the current_annual_salary set to the annual_salary. 
These values should be adjusted during the calculation.
4. At the end of each month you receive an addtional current_savings * percent_annual_return / 12 that you would add 
to your current savings.
5. Assume you are going to dedicate a certain amount of your salary each month to saving for 
the down payment. This is the percent_to_save value passed to `months` as a decimal value. It is defaulted to 0.25 
6. At the end of each month, your savings will be increased by the return on your investment,
plus a percentage of your monthly salary (annual_salary / 12).
7. The semi_annual_raise value is used to increase your salary by that percentage. This calculation occurs every 
6 months.

"""


class SavingsCalculator(object): 


    def __init__(self, 
        annual_salary: float, 
        total_cost: float=1000000, 
        semi_annual_raise: float=0.07, 
        percent_down_payment: float=0.25, 
        percent_annual_return: float=0.04): 
        """ A class that calculates how many months it will take for you to make a down payment 
        on a house based on a number of factors.

        Args:
            annual_salary (float): Your starting annual salary.
            total_cost (float, optional): The total cost of the house you wish to buy. Defaults to 1000000.
            semi_annual_raise (float, optional): The percentage that your salary increases every 6 months. Defaults to 0.07.
            percent_down_payment (float, optional): The percentage of the total_cost needed for a downpayment. Defaults to 0.25.
            percent_annual_return (float, optional): The percentage of  . Defaults to 0.04.

        """

        self._annual_salary = annual_salary 
        self._total_cost = total_cost 
        self._semi_annual_raise = semi_annual_raise 
        self._percent_down_payment = percent_down_payment
        self._percent_annual_return = percent_annual_return 


    def _monthly_salary(self, current_annual_salary: float) -> float: 
        """A monthly salary calculated based on the current_annual_salary in the 
        calculation.

        Args:
            current_annual_salary (float): The current annual salary during the calculation

        Returns:
            float: The monthly salary
        """
        current_annual_salary = self._annual_salary
        return current_annual_salary / 12  


    def _annual_return(self, current_savings: float) -> float: 
        """The annual return calculated as current_savings * percent_annual_return per month 
        during the calculation.

        Args:
            current_savings (float): The current_savings at this point in the calc.

        Returns:
            float: The annual return
        """
        return current_savings * (self._percent_annual_return / 12)


    def months(self, percent_to_save: float=0.1) -> int:
        """Given the percent of money you wish to save each month return the number of months 
        that it will take to put a down payment on a house.

        Args:
            percent_to_save (float, optional): The percentage of money that will be saved each month. Defaults to 0.1.

        Returns:
            int: the number of months it will take to save for a downpayment given the variables.
        """

        # ** before you code it... write out the steps here...
        '''
            1. while curr_savings < portion_down_payment
            2. amt_towards_savings are set aside 
            3. every 6 months inc annual_salary and amt_towards_savings 
            4. else inc curr_savings by amt_towards_savings 
            5. months += 1 
        '''

        # ** giving you a head start here based on what is in the module description
        current_savings = 0.0 
        portion_down_payment = self._percent_down_payment * self._total_cost 
        current_annual_salary = self._annual_salary
        #⚠️ the above are given
        months = 0 
        while current_savings < portion_down_payment:
            inc_by_amt = self._monthly_salary(current_annual_salary) * percent_to_save + self._annual_return(current_savings)
            if months % 6 != 0 or months == 0:
                current_savings += inc_by_amt
            else: 
                self._annual_salary += self._annual_salary * self._semi_annual_raise
                current_savings += inc_by_amt 
            months += 1  
        return months

