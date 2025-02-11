import pandas as pd
import sys

def import_bank_csv(file_path):
    df = pd.read_csv(file_path, encoding='utf-8', delimiter=',', header=4)
    return df


def export_spending_report(spending_report, output_path):
    spending_report.to_csv(output_path, index=False, sep=';', encoding='utf-8')
    print(f"Processed data saved to {output_path}")

def find_column_in_columns(df, search_term):
    column_name = ""
    for index, col in enumerate(df.columns):
        if search_term in col:
            column_name = col

    return column_name


def create_spending_report(bank_df):
    bank_df["Buchungsdatum"] = pd.to_datetime(bank_df["Buchungsdatum"], format='%d.%m.%y', errors='coerce')

    betrag_col_identifier = find_column_in_columns(bank_df, "Betrag") 

    bank_df[betrag_col_identifier] = (
        bank_df[betrag_col_identifier]
        .str.split().str[0]
        .str.replace('.', '')
        .str.replace(',', '.')
        .str.strip()
    )

    bank_df[betrag_col_identifier] = pd.to_numeric(bank_df[betrag_col_identifier], errors='coerce')

    bank_df["Jahr"] = bank_df["Buchungsdatum"].dt.year

    df_expenses = bank_df[bank_df[betrag_col_identifier] < 0]
    print(df_expenses)
    df_summary = df_expenses.groupby(["Jahr", "Zahlungsempfänger*in"])[betrag_col_identifier].sum().reset_index()

    spending_report = df_summary.sort_values(by=["Jahr", "Zahlungsempfänger*in"])

    return spending_report


def main():
    if len(sys.argv) != 2:
        print("usage: python3 spending_report.py <PATH-TO-CSV>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_path = "spending_report.csv"
    bank_df = import_bank_csv(file_path)
    spending_report = create_spending_report(bank_df)
    export_spending_report(spending_report, output_path)

if __name__ == '__main__':
    main()
