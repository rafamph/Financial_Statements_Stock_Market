from yahoo_finance import Share
import inspect
import quandl
import math
import pandas

while True:

    print ('STOCK TICKER?')

    z= input()

    yahoo = Share(z)

    quandl.ApiConfig.api_key = ''

    # print(yahoo.get_ebitda())


    # print(inspect.getsourcelines(yahoo.get_price_book))

    mydata = (quandl.get_table('ZACKS/FR', ticker=z))
    # mydata = mydata.as_matrix()


    roa1 = float(mydata[(len(mydata) - 2):(len(mydata) - 1)]['ret_asset'])
    roa2 = float(mydata[-1:]['ret_asset'])
    roe1 = float(mydata[(len(mydata) - 2):(len(mydata) - 1)]['ret_equity'])
    roe2 = float(mydata[-1:]['ret_equity'])
    profitmargin1 = float(mydata[(len(mydata) - 2):(len(mydata) - 1)]['profit_margin'])
    profitmargin2 = float(mydata[-1:]['profit_margin'])
    assetturn1 = float(mydata[(len(mydata) - 2):(len(mydata) - 1)]['asset_turn'])
    assetturn2 = float(mydata[-1:]['asset_turn'])
    inventturn1 = float(mydata[(len(mydata) - 2):(len(mydata) - 1)]['invty_turn'])
    inventturn2 = float(mydata[-1:]['invty_turn'])
    currentratio1 = float(mydata[(len(mydata) - 2):(len(mydata) - 1)]['curr_ratio'])
    currentratio2 = float(mydata[-1:]['curr_ratio'])
    debtequity1 = float(mydata[(len(mydata) - 2):(len(mydata) - 1)]['tot_debt_tot_equity'])
    debtequity2 = float(mydata[-1:]['tot_debt_tot_equity'])
    booktomark2 = (float((mydata[(len(mydata) - 2):(len(mydata) - 1)]['book_val_per_share']))) / (float(yahoo.get_price()))
    pe2 = float(yahoo.get_price_earnings_ratio())

    try:

        if roa2 > roa1 and roa2 > 0:
            print("ROA = %s CHANGE = %s%% Interpretation: Assets are being used effectively" % (
            round(roa2, 2), round(((roa2 - roa1) / abs(roa1)) * 100)))
        elif roa2 > roa1 and roa2 < 0:
            print("ROA = %s CHANGE = %s%% Interpretation: Assets are being used OK" % (
            round(roa2, 2), round(((roa2 - roa1) / abs(roa1)) * 100)))
        elif roa2 < roa1 and roa2 > 0:
            print("ROA = %s CHANGE = %s%% Interpretation: Assets are being used OK" % (
            round(roa2, 2), round(((roa2 - roa1) / abs(roa1)) * 100)))
        else:
            print("ROA = %s CHANGE = %s%% Interpretation: Assets are not being well used" % (
            round(roa2, 2), round(((roa2 - roa1) / abs(roa1)) * 100)))

        if roe2 > roe1 and roe2 > 0:
            print("ROE = %s CHANGE = %s%% Interpretation: Capital is being invested effectively" % (
            round(roe2, 2), round(((roe2 - roe1) / abs(roe1)) * 100)))
        elif roe2 > roe1 and roe2 < 0:
            print("ROE = %s CHANGE = %s%% Interpretation: Capital usage is OK" % (
            round(roe2, 2), round(((roe2 - roe1) / abs(roe1)) * 100)))
        elif roe2 < roa1 and roe2 > 0:
            print("ROE = %s CHANGE = %s%% Interpretation: Capital usage is ok" % (
            round(roe2, 2), round(((roe2 - roe1) / abs(roe1)) * 100)))
        else:
            print("ROE = %s CHANGE = %s%% Interpretation: Capital is not being well used" % (
            round(roe2, 2), round(((roe2 - roe1) / abs(roe1)) * 100)))

        if profitmargin2 > profitmargin1 and profitmargin2 > 0:
            print("PROFIT MARGIN = %s CHANGE = %s%% Interpretation: Company is doing well overall" % (
            round(profitmargin2, 2), round(((profitmargin2 - profitmargin1) / abs(profitmargin1)) * 100)))
        elif profitmargin2 > profitmargin1 and profitmargin2 < 0:
            print("PROFIT MARGIN = %s CHANGE = %s%% Interpretation: Company is doing ok" % (
            round(profitmargin2, 2), round(((profitmargin2 - profitmargin1) / abs(profitmargin1)) * 100)))
        elif profitmargin2 < profitmargin1 and profitmargin2 > 0:
            print("PROFIT MARGIN = %s CHANGE = %s%% Interpretation: Company is doing ok" % (
            round(profitmargin2, 2), round(((profitmargin2 - profitmargin1) / abs(profitmargin1)) * 100)))
        else:
            print("PROFIT MARGIN = %s CHANGE = %s%% Interpretation: Company is not doing ok" % (
            round(profitmargin2, 2), round(((profitmargin2 - profitmargin1) / abs(profitmargin1)) * 100)))

        if assetturn2 > assetturn1 and assetturn2 > 2:
            print("ASSET TURNOVER = %s CHANGE = %s%% Interpretation: Assets are producing great sales" % (
            round(assetturn2, 2), round(((assetturn2 - assetturn1) / abs(assetturn1)) * 100)))
        elif assetturn2 > assetturn1 and assetturn2 < 2:
            print("ASSET TURNOVER = %s CHANGE = %s%% Interpretation: Assets are producing ok sales" % (
            round(assetturn2, 2), round(((assetturn2 - assetturn1) / abs(assetturn1)) * 100)))
        elif assetturn2 < assetturn1 and assetturn2 > 2:
            print("ASSET TURNOVER = %s CHANGE = %s%% Interpretation: Assets are producing ok sales" % (
            round(assetturn2, 2), round(((assetturn2 - assetturn1) / abs(assetturn1)) * 100)))
        else:
            print("ASSET TURNOVER = %s CHANGE = %s%% Interpretation: Assets are not producing great sales" % (
            round(assetturn2, 2), round(((assetturn2 - assetturn1) / abs(assetturn1)) * 100)))

        if inventturn2 > inventturn1 and inventturn2 > 4:
            print("INVENTORY TURNOVER = %s CHANGE = %s%% Interpretation: Company is selling fast" % (
            round(inventturn2, 2), round(((inventturn2 - inventturn1) / abs(inventturn1)) * 100)))
        elif inventturn2 > inventturn1 and inventturn2 < 4:
            print("INVENTORY TURNOVER = %s CHANGE = %s%% Interpretation: Company is selling at ok speed" % (
            round(inventturn2, 2), round(((inventturn2 - inventturn1) / abs(inventturn1)) * 100)))
        elif inventturn2 < inventturn1 and inventturn2 > 4:
            print("INVENTORY TURNOVER = %s CHANGE = %s%% Interpretation: Company is selling at ok speed" % (
            round(inventturn2, 2), round(((inventturn2 - inventturn1) / abs(inventturn1)) * 100)))
        else:
            print("INVENTORY TURNOVER = %s CHANGE = %s%% Interpretation: Company is selling slow" % (
            round(inventturn2, 2), round(((inventturn2 - inventturn1) / abs(inventturn1)) * 100)))

        if currentratio2 > currentratio1 and currentratio2 > 1:
            print("CURRENT RATIO = %s CHANGE = %s%% Interpretation: Company has enough assets for its debt" % (
            round(currentratio2, 2), round(((currentratio2 - currentratio1) / abs(currentratio1)) * 100)))
        elif currentratio2 > currentratio1 and currentratio2 < 1:
            print("CURRENT RATIO = %s CHANGE = %s%% Interpretation: Company may have problems with debt" % (
            round(currentratio2, 2), round(((currentratio2 - currentratio1) / abs(currentratio1)) * 100)))
        elif currentratio2 < currentratio1 and currentratio2 > 1:
            print("CURRENT RATIO = %s CHANGE = %s%% Interpretation: Company may have problems with debt" % (
            round(currentratio2, 2), round(((currentratio2 - currentratio1) / abs(currentratio1)) * 100)))
        else:
            print("CURRENT RATIO = %s CHANGE = %s%% Interpretation: Company does not have enough assets for its debt" % (
            round(currentratio2, 2), round(((currentratio2 - currentratio1) / abs(currentratio1)) * 100)))

        if debtequity1 > debtequity2 and currentratio2 < 1:
            print("DEBT EQUITY RATIO = %s CHANGE = %s%% Interpretation: Company has safer capital structure" % (
            round(debtequity2, 2), round(((debtequity2 - debtequity1) / abs(debtequity1)) * 100)))
        elif debtequity1 > debtequity2 and currentratio2 > 1:
            print("DEBT EQUITY RATIO = %s CHANGE = %s%% Interpretation: Company has balanced capital structure" % (
            round(debtequity2, 2), round(((debtequity2 - debtequity1) / abs(debtequity1)) * 100)))
        elif debtequity1 < debtequity2 and currentratio2 < 1:
            print("DEBT EQUITY RATIO = %s CHANGE = %s%% Interpretation: Company has balanced capital structure" % (
            round(debtequity2, 2), round(((debtequity2 - debtequity1) / abs(debtequity1)) * 100)))
        else:
            print("DEBT EQUITY RATIO = %s CHANGE = %s%% Interpretation: Company has riskier capital structure" % (
            round(debtequity2, 2), round(((debtequity2 - debtequity1) / abs(debtequity1)) * 100)))

        if booktomark2 > 1:
            print("BOOK TO MARKET = %s Stock may be undervalued" % (round(booktomark2*100)))
        elif booktomark2 < 1:
            print("BOOK TO MARKET = %s Stock may be overvalued" % (round(booktomark2*100)))
        else:
            print("BOOK TO MARKET = %s Stock price may be fait" % (round(booktomark2*100)))

        if pe2 > 20:
            print("PRICE EARNINGS = %s Investors may anticipate higher growth\n" % (pe2))
        else:
            print("PRICE EARNINGS = %s Investors may not anticipate higher growth\n" % (pe2))

    except ValueError:
        print('Stock currently not available\n')
