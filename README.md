# Currency Converter

**Note: This is a practice project** 
**⚠️You will need an api key from [ExchangeRate-API](https://exchangerate-api.com)⚠️**

**This program is unfinished, there may be bugs, here are features that are planned for this:**

- [x] Universal Conversion (USD, EUR, MXN, AUD)
- [ ] GUI Mode
- [ ] API Key Checker

**AFAIK**

## Usage

```bash
$ ./main.py --currency USD 1 --exchange MXN <- Mexican Peso
1 USD -> 20.40 MXN <- can change
```

```bash
$ ./main.py --currency EUR 5 --exchange USD <- United States Dollar
5 EUR -> 5.67 USD <- can change
```

`--currency` requires the currency (USD for now) and the amount  
`--exchange` currency to exchange to (MXN, EUR, AUD) (Peso, Euro, Australian Dollar) (for now)  
`--request` tests if the api works with the key  