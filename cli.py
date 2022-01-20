# Currency Converter CLI
#!/usr/bin/python3

import requests
import json
import argparse, sys

def usage():
    print(
        f'Usage: {sys.argv[0]} -c, --currency [CURRENCY][AMOUNT] -e, --exchange [EXCHANGE] -r\n'
        '    -h, --help                            display this usage page\n'
        '    -c, --currency [CURRENCY][AMOUNT]     set currency to exchange from\n'
        '    -e, --exchange [EXCHANGE]             set currency to exchange to\n'
        '    -r, --request                         request test\n'
    )

def fetch_chart(url):
    response = requests.get(url)
    data = response.json()

    # data_json = json.dumps(data, indent=4)

    return data

def convert(currency: list, exchange: str):    
    if currency[0] == "USD":
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
            raise Exception('misspelling error')

    elif currency[0] == "MXN":
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
    else:
        raise Exception('unknown currency')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Currency converter CLI', add_help=False)

    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-c', '--currency', nargs=2)
    parser.add_argument('-e', '--exchange', type=str)
    parser.add_argument('-r', '--request', action='store_true')

    args = parser.parse_args()

    url = 'https://v6.exchangerate-api.com/v6/ef977f211c62be97aeff5d2a/latest/USD'

    if args.help is True:
        usage()
        
    elif args.request:
        try:
            data = fetch_chart(url)
            data = json.dumps(data, indent=4)
            print(data)

        except Exception as err:
            print(err)
    
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
    
    elif args.currency and args.exchange:
        pass

    elif args.currency and not args.exchange:
        pass

    elif not args.currency and args.exchange:
        pass

    else:
        usage()
