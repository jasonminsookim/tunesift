import datetime

def convert_to_date(pf_date):
    # pf_date are all in GMT
    date_time_ls = []
    date_and_time = pf_date.split('T')
    date_time_ls.append(date_and_time[0].split('-'))
    date_time_ls.append(date_and_time[1].split(':'))

    date_time_ls = sum(date_time_ls, [])
    date_time_ls = [int(num) for num in date_time_ls]

    date_time_fixed = datetime.datetime(date_time_ls[0], date_time_ls[1], date_time_ls[2], date_time_ls[3],
                                        date_time_ls[4], date_time_ls[5])

    return (date_time_fixed)