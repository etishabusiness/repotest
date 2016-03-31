from nsepy.archives import get_price_history


dates = [('01-01-2015', '31-01-2015'), ('01-04-2015', '31-07-2015'),
         ('01-07-2015', '30-10-2015'), ('01-10-2015', '31-12-2015')]

for date in dates:
    df = get_price_history(stock = 'DABUR', start = date[0], end = date[1])
    print df  ['Close'] 