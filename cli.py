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

def convert(currency, exchange):
    url = 'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD'

    response = requests.get(url)
    data = response.json()

    usd = data['conversion_rates']['USD']
    mxn = data['conversion_rates']['MXN']
    eur = data['conversion_rates']['EUR']
    aud = data['conversion_rates']['AUD']

    if "MXN" in exchange:
        exchange_total_mxn = mxn * currency
    
        return exchange_total_mxn

    elif "EUR" in exchange:
        exchange_total_eur = eur * currency

        return exchange_total_eur

    elif "AUD" in exchange:
        exchange_total_aud = aud * currency

        return exchange_total_aud

    else:
        raise Exception('Unknown exchange')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Currency converter CLI', add_help=False)

    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-c', '--currency', nargs="+")
    parser.add_argument('-e', '--exchange', type=str)
    parser.add_argument('-r', '--request', action='store_true')

    args = parser.parse_args()

    url = 'https://v6.exchangerate-api.com/v6/4ddce1eec5ce1cc3e518a495/latest/USD'

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
                currency = float(args.currency[1])

                # If the user types in lowercase
                args.exchange = args.exchange.upper()

                _exchange = convert(currency, args.exchange)
                print(f'{round(_exchange, 2)} {args.exchange}')
        
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
