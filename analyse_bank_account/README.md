# Analyze Bank Account

The DKB (Deutsche Kreditbank AG) in Germany provides account statements in CSV format.

This is a script to show you where you spent your most money.


The 4th row has the following headers:
```CSV
Buchungsdatum,Wertstellung,Betrag (€),Status,Zahlungspflichtige*r,Zahlungsempfänger*in,Verwendungszweck,Umsatztyp,IBAN,,Gläubiger-ID,Mandatsreferenz,Kundenreferenz
```

## Usage
1. Clone repo
2. Install requirements:
```SHELL
pip install -r requirements.txt
```
3. Run script:
```SHELL
python3 spending_report.py <PATH-TO-SPENDING-REPORT-CSV>
```
4. Find a `spending_report.csv` in your directory
