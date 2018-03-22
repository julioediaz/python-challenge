import csv

# Python script for analyzing the financial records of company.
# Datasets are in csv format composed of two columns: Date and Revenue
#
# !!! To analyze data correctly a dataset must contains at least two months and months are ordered
#
# Script analyzes the records to calculate each of the following:
# 1) The total number of months included in the dataset
# 2) The total amount of revenue gained over the entire period: this is sum of revenue column
# 3) The average change in revenue between months over the entire period:
#                   sum all revenue changes and divide on (months count - 1).
#                   revenue change is calculated as difference between current revenue and revenue for previous month
#                   That is mean revenue changes count is equal (months count - 1)
# 4) The greatest increase in revenue (date and amount) over the entire period
#   it is possible situation that there are few equal Greatest Increase in Revenue. In this case
#   the application print first one.
# 5) The greatest decrease in revenue (date and amount) over the entire period
#   it is possible situation that there are few equal Greatest Decrease in Revenue. In this case
#   the application print first one.
#
# for output comma is used as thousand separator


def analyze_data(input_file_name, output_file_name):
    total_revenue = 0
    total_months = 0
    total_revenue_change = 0
    max_increase = None
    month_of_max_increase = None
    max_decrease = None
    month_of_max_decrease = None

    with open(input_file_name, newline='') as f:
        csv_sheet = csv.reader(f)
        csv_iterator = iter(csv_sheet)

        header = csv_iterator.__next__()  # skip header
        first_row = csv_iterator.__next__()
        total_months += 1
        total_revenue += int(first_row[1])
        # info for application debuging
        # print('{}. {}, total revenue: {}, revenue: {}'
        #       .format(total_months, first_row[0], total_revenue, first_row[1]))
        prev_revenue = int(first_row[1])  # used for revenue changes calculating

        for row in csv_iterator:
            if len(row[0]) == 0:
                break
            cur_revenue = int(row[1])
            revenue_change = cur_revenue - prev_revenue  # current month revenue - previous month revenue
            total_revenue_change += revenue_change
            total_revenue += int(row[1])
            total_months += 1
            if revenue_change >= 0:  # revenue increases
                if max_increase is None:  # first increase
                    max_increase = revenue_change
                    month_of_max_increase = row[0]
                elif max_increase < revenue_change:
                    max_increase = revenue_change
                    month_of_max_increase = row[0]

            if revenue_change <= 0:  # revenue decreases
                if max_decrease is None:  # first decrease
                    max_decrease = revenue_change
                    month_of_max_decrease = row[0]
                elif max_decrease > revenue_change:
                    max_decrease = revenue_change
                    month_of_max_decrease = row[0]

            # info for application debuging
            # print('{}. {}, total revenue: {}, revenue: {}, revenue change: {}, total revenue change: {}'
            #       .format(total_months, row[0], total_revenue,  row[1], revenue_change, total_revenue_change))

            prev_revenue = cur_revenue

    with open(output_file_name, mode='w') as out:
        out.write('Financial Analysis\n')
        out.write('Total Months: {}\n'.format(total_months))
        out.write('Total Revenue: $({:,})\n'.format(total_revenue))  # comma is used as thousand separator
        average_revenue_change = float(total_revenue_change) / (total_months - 1)
        out.write('Average Revenue Change: $({:,.2f})\n'.format(average_revenue_change))  # comma is used as thousand separator
            # .2 means output 2 digits after dot
        if max_increase is not None:  # and max_increase != 0:
            out.write('Greatest Increase in Revenue: {} $({:,})\n'.format(month_of_max_increase, max_increase))  # comma is used as thousand separator
        else:
            out.write('There is no increase')

        if max_decrease is not None:  # and max_decrease != 0:
            out.write('Greatest Decrease in Revenue: {} $({:,})\n'.format(month_of_max_decrease, max_decrease))  # comma is used as thousand separator
        else:
            out.write('There is no decrease')

        print('The result was written in file {}'.format(output_file_name))


if __name__ == '__main__':
    # analyze_data('budget_data_1.csv', result_1.txt)
    analyze_data('budget_data_2.csv', 'result_2.txt')
