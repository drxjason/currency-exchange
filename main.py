# Currency Converter CLI
#!/usr/bin/python3

import requests
import json
import argparse, sys

from tkinter import *
from tkinter import ttk
import tkinter as tk

def usage():
    print(
        f'Usage: {sys.argv[0]} -c, --currency [CURRENCY][AMOUNT] -e, --exchange [EXCHANGE] -r, --request [CURRENCY] -g, --gui\n\n'
        'Currency Converter/Exchanger\n\n'
        '    -h, --help                            display this usage page\n'
        '    -c, --currency [CURRENCY][AMOUNT]     set currency to exchange from\n'
        '    -e, --exchange [EXCHANGE]             set currency to exchange to\n'
        '    -r, --request  [CURRENCY]             request test\n'
        '    -g, --gui                             program in a graphical user interface'
    )

def fetch_chart(curr: str):
    curr = curr.upper()

    if curr == 'MXN':
        url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/MXN'

        response = requests.get(url)
        data = response.json()

        return data

    elif curr == 'USD':
        url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/USD'

        response = requests.get(url)
        data = response.json()

        return data

    elif curr == 'EUR':
        url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/EUR'

        response = requests.get(url)
        data = response.json()

        return data

    elif curr == 'AUD':
        url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/AUD'

        response = requests.get(url)
        data = response.json()

        return data

    else:
        raise Exception("unknown currency")


def convert(currency: list, exchange: str):
    # Currency detects for currency and amount, ex. currency = ['EUR', 15] (15 EUR)
    # Converts to currency to exchange to, ex. exchange_total_usd = 17.01 USD

    if currency[0] == "USD":
        if "USD" in exchange:
            raise NameError(f"cannot convert currency into itself")

        else:
            url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/USD'

            response = requests.get(url)
            data = response.json()

            usd = data['conversion_rates']['USD']
            mxn = data['conversion_rates']['MXN']
            eur = data['conversion_rates']['EUR']
            aud = data['conversion_rates']['AUD']

            if "MXN" in exchange:
                exchange_total_mxn = mxn * float(currency[1])

                return exchange_total_mxn

            elif "EUR" in exchange:
                exchange_total_eur = eur * float(currency[1])

                return exchange_total_eur

            elif "AUD" in exchange:
                exchange_total_aud = aud * float(currency[1])

                return exchange_total_aud
            
            else:
                raise NameError('cannot convert into itself')

    elif currency[0] == "MXN":
        if "MXN" in exchange:
            raise NameError("cannot convert curency into itself")

        else:   
            url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/MXN'

            response = requests.get(url)
            data = response.json()

            mxn = data['conversion_rates']['MXN']
            usd = data['conversion_rates']['USD']
            eur = data['conversion_rates']['EUR']
            aud = data['conversion_rates']['EUR']

            if "USD" in exchange:
                exchange_total_usd = usd * float(currency[1])

                return exchange_total_usd

            elif "EUR" in exchange:
                exchange_total_eur = eur * float(currency[1])

                return exchange_total_eur
            
            elif "AUD" in exchange:
                exhange_total_aud = aud * float(currency[1])

                return exchange_total_aud

            else:
                raise Exception('unknown exchange')

    elif currency[0] == "EUR":
        if "EUR" in exchange:
            raise NameError("cannot convert currency into itself")

        else:  
            url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/EUR'

            response = requests.get(url)
            data = response.json()

            eur = data['conversion_rates']['EUR']
            mxn = data['conversion_rates']['MXN']
            usd = data['conversion_rates']['USD']
            aud = data['conversion_rates']['AUD']

            if "AUD" in exchange:
                exchange_total_aud = aud * float(currency[1])

                return exchange_total_aud

            elif "MXN" in exchange:
                exchange_total_mxn = mxn * float(currency[1])

                return exchange_total_mxn

            elif "USD" in exchange:
                exchange_total_usd = usd * float(currency[1])

                return exchange_total_usd

            else:
                raise Exception('unknown exchange')

    elif currency[0] == 'AUD':
        if "AUD" in exchange:
            raise NameError("cannot convert currency into itself")

        else:
            url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/EUR'

            reponse = requests.get(url)
            data = response.json()

            aud = data['conversion_rates']['AUD']
            usd = data['conversion_rates']['USD']
            mxn = data['conversion_rates']['MXN']
            eur = data['conversion_rates']['MXN']

            if "EUR" in exchange:
                exchange_total_eur = eur * float(currency[1])

                return exchange_total_eur

            elif "USD" in exchange:
                exchange_total_usd = usd * float(currency[1])

                return exchange_total_usd

            elif "MXN" in exchange:
                exchange_total_mxn = mxn * float(currency[1])

                return exchange_total_mxn

            else:
                raise Exception('unknown exchange')

    else:
        if exchange == currency[0]:
            raise NameError("what.. read the usage page")
        raise Exception('unknown currency')

def check_api(api):
    pass

class CurrencyConv:
    def __init__(self):
        self.root = Tk()
        self.root.title('drxjason \u2014 currency-exchange')

    def widgets(self):
        self.root.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Currency converter CLI', add_help=False)

    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-c', '--currency', nargs=2)
    parser.add_argument('-e', '--exchange', type=str)
    parser.add_argument('-r', '--request', type=str)
    parser.add_argument('-g', '--gui', action='store_true')

    args = parser.parse_args()

    if args.help is True:
        usage()
        
    elif args.request:
        try:
            data = fetch_chart(args.request)
            data = json.dumps(data, indent=4)
            print(data)

        except Exception as err:
            print(err)

    elif args.gui:
        gui_cc = CurrencyConv()
        gui_cc.widgets()
    
    elif args.currency and args.exchange:
        if len(args.currency) > 1:
            if "USD" or "usd" in args.currency[0]:
                # If the user types in lowercase
                args.exchange = args.exchange.upper()
                args.currency[0] = args.currency[0].upper()

                _exchange = convert(args.currency, args.exchange)
                print(f'{args.currency[1]} {args.currency[0]} \u2015> {round(_exchange, 2)} {args.exchange}')

            elif "MXN" or "mxn" in args.currency[0]:
                args.exchange = args.exchange.upper()
                args.currency[0] = args.currency[0].upper()


                _exchange = convert(args.currency, args.exchange)
                print(f'{args.currency[1]} {args.currency[0]} \u2015> {round(_exchange, 2)} {args.exchange}')
            
            elif "EUR" or "eur" in args.currency[0]:
                args.exchange = args.exchange.upper()
                args.currency[0] = args.currency[0].upper()

                _exchange = convert(args.currency, args.exchange)
                print(f'{args.currency[1]} {args.currency[0]} \u2015> {round(_exchange, 2)} {args.exchange}')
            
            elif "AUD" or "aud" in args.currency[0]:
                args.exchange = args.exchange.upper()
                args.currency[0] = args.currency[0].upper()

                _exchange = convert(args.currency, args.exchange)
                print(f'{args.currency[1]} {args.currency[0]} \u2015> {round(_exchange, 2)} {args.exchange}')
        
            else:
                raise Exception('unknown currency')

    elif args.currency and not args.exchange:
        raise ValueError("Missing required argument: -e, --exchange")

    elif not args.currency and args.exchange:
        raise ValueError("Missing required argument: -c, --currency")

    else:
        usage()
