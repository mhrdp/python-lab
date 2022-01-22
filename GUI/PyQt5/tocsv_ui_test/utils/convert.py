import os
import pandas as pd

class ExtractData:
    def __init__(self, file_in):
        self.file_in = file_in
        self.file_out = None
    
    def _get_sheetname(self, file_in):
        sheets = pd.ExcelFile(file_in)
        return sheets.sheet_names
    
    def _general_inf_sheet(self, file_in):
        sheet_name = self._get_sheetname(file_in)
        sheet = sheet_name[1]
        return sheet
    
    def _financial_pos_sheet(self, file_in):
        sheet_name = self._get_sheetname(file_in)
        sheet = sheet_name[2]
        return sheet
    
    def _profit_or_loss_sheet(self, file_in):
        sheet_name = self._get_sheetname(file_in)
        sheet = sheet_name[3]
        return sheet
    
    def _cashflow_sheet(self, file_in):
        sheet_name = self._get_sheetname(file_in)
        sheet = sheet_name[6]
        return sheet
    
    def _get_company_name(self, file_in):
        general_inf = self._general_inf_sheet(file_in)
        
        reader = pd.read_excel(file_in, sheet_name=general_inf)
        dict_temp = {}

        for i in range(len(reader)):
            key = reader['Unnamed: 2'][i]
            val = reader['Unnamed: 1'][i]
            dict_temp[key] = [val]
        
        df = pd.DataFrame(dict_temp)
        df = df.rename(
            columns = {
                'Entity code': 'entity_code',
                'Level of rounding used in financial statements': 'rounding_level',
                'Sector': 'sector',
                'Subsector': 'subsector',
            }
        )

        # Use __getitem__ method, aka. [[...]] to return type(DataFrame), instead of type(series)
        return df[['entity_code', 'rounding_level', 'sector', 'subsector']]
        
    def general_inf(self):
        self.file_out = './exports/company_general_information.csv'
        
        sheet = self._general_inf_sheet(self.file_in)
        
        # index_col=0 is to remove auto-generated index column
        gen_inf = pd.read_excel(self.file_in, sheet_name=sheet, index_col=0)
        gen_inf_dict = {}
        
        # Convert the initial dataframe into dictionary for cleaning
        for i in range(len(gen_inf)):
            key = gen_inf['Unnamed: 2'][i]
            val = gen_inf['Unnamed: 1'][i]
            gen_inf_dict[key] = [val]
        
        # Back to dataframe after cleaning
        df = pd.DataFrame(gen_inf_dict)

        # Rename the first dataframe header
        df.columns.values[0] = 'date_of_report'
        
        # Rename entire columns
        df = df.rename(columns={
            'Entity name': 'entity_name',
            'Entity code': 'entity_code',
            'Explanation of change in name from the end of the preceding reporting period': 'name_change_explanation',
            'Entity identification number': 'identification_number',
            'Entity main industry': 'main_industry',
            'Controlling shareholder information': 'information_control',
            'Type of entity': 'entity_type',
            'Type of listed securities': 'securities_type',
            'Type of board on which the entity is listed': 'type_of_board',
            'Whether the financial statements are of an individual entity or a group of entities': 'statements_from',
            'Period of financial statements submissions': 'period',
            'Current period start date': 'start_date',
            'Current period end date': 'end_date',
            'Prior period start date': 'prior_start_date',
            'Prior period end date': 'prior_end_date',
            'Description of presentation currency': 'currency',
            'Conversion rate at reporting date if presentation currency is other than rupiah': 'alternate_currency',
            'Level of rounding used in financial statements': 'rounding_level',
            'Type of report on financial statements': 'report_type',
            'Type of auditor\'s opinion': 'auditor_opinion_type',
            'Matters disclosed in emphasis-of-matter or other-matter paragraph, if any': 'emphasis_of_matter',
            'Result of review engagement': 'review_result',
            'Date of auditor\'s opinion or result of review report': 'date_of_review',
            'Name of current year audit signing partner': 'signing_partner_name',
            'Number of years served as audit signing partner': 'signing_partner_experience',
            'Name of prior year audit signing partner': 'prior_year_signing_partner',
            'Whether in compliance with BAPEPAM LK VIII G 11 rules concerning responsibilities of board of directors on financial statements': 'BAPEPAM_LK_VIII_G11',
            'Whether in compliance with BAPEPAM LK VIII A two rules concerning independence of accountant providing audit services in capital market': 'BAPEPAM_LK_VIII_A2',

            'Sector': 'sector',
            'Subsector': 'subsector',
            'Prior year end date': 'prior_year_end',
            'Current year auditor': 'current_year_auditor',
            'Prior year auditor': 'prior_year_auditor',
        })
        df = df.drop(columns=['General information'])

        # Check whether ./exports folder exists
        # os.getcwd() is to get current working directory
        current_dir = f'{os.getcwd()}/exports'
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
        
        # If output .csv exist
        if os.path.exists(self.file_out):
            read_file_out = pd.read_csv(self.file_out)
            
            # Delete a row if that row has entity_code column empty and save it again
            if True in list(read_file_out['entity_code'].isna()):
                read_file_out.dropna(subset=['entity_code'], inplace=True)
                read_file_out.reset_index(drop=True)
                read_file_out.to_csv('./exports/general_company_information.csv', index=False)
            
            # If emiten name not in the list
            if df['entity_code'][0] not in list(set(read_file_out['entity_code'])):
                # mode = 'a' is to append, default is 'w' to write
                df.to_csv('./exports/company_general_information.csv', mode='a', header=False, index=False)
            
            # If emiten name already inside the list
            if df['entity_code'][0] in list(set(read_file_out['entity_code'])):
                # Filter the dataframe based on entity_code
                filtered_df = read_file_out.loc[read_file_out['entity_code'] == df['entity_code'][0]]
                
                # Compare the date_of_report with filtered dataframe
                if df['date_of_report'][0] not in list(filtered_df['date_of_report']):
                    df.to_csv('./exports/company_general_information.csv', mode='a', header=False, index=False)
        else:
            # Create .csv if not exist
            df.to_csv('./exports/company_general_information.csv', index=False)
    
    def financial_pos(self):
        sheet = self._financial_pos_sheet(self.file_in)
        fin_pos = pd.read_excel(self.file_in, sheet_name=sheet, index_col=0)
        self.file_out = './exports/company_financial_position.csv'
        
        # Dataframe for basic company information
        df_get_name = self._get_company_name(self.file_in)

        fin_dict = {}
        
        # Convert the initial dataframe into dictionary for some cleaning
        for i in range(len(fin_pos)):
            key = fin_pos['Unnamed: 3'][i]
            val = fin_pos['Unnamed: 1'][i]
            # The val need to be encapsulated inside a list
            fin_dict[key] = [val]
        
        # Convert back into dataframe after cleaning
        df = pd.DataFrame(fin_dict)
        
        # Rename the first column
        df.columns.values[0] = 'date_of_report'

        # Slice the dataframe with __getitem__ method aka. [[...]]
        if df_get_name['subsector'][0] == '84. Insurance':
            df = df[[
                    'date_of_report', 'Cash and cash equivalents', 'Total assets', 
                    'Total liabilities', 'Total equity'
            ]]

            # Rename the entire columns
            df = df.rename(
                columns = {
                    'Cash and cash equivalents': 'cash_and_cash_equivalents',
                    'Total assets': 'total_assets',
                    'Total liabilities': 'total_liabilities',
                    'Total equity': 'total_equity',
                }
            )

            # Manually fill in the dataframe according to the columns expected for the output
            # you can fill the columns that are not exist for current dataframe with pd.NA
            # there's probably a better way to do this but...
            df['date_of_report'] = df['date_of_report']
            df['cash_and_cash_equivalents'] = df['cash_and_cash_equivalents']
            df['total_current_assets'] = pd.NA
            df['total_non_current_assets'] = pd.NA
            df['total_assets'] = df['total_assets']
            df['total_current_liabilities'] = pd.NA
            df['total_non_current_liabilities'] = pd.NA
            df['total_liabilities'] = df['total_liabilities']
            df['total_equity'] = df['total_equity']
            df['total_liabilities_and_equity'] = pd.NA
            df['total_temporary_syirkah_funds'] = pd.NA
            df['total_liabilities_syirkah_equity'] = pd.NA


        elif df_get_name['subsector'][0] == '81. Bank':
            df = df[[
                'date_of_report', 'Cash', 'Total assets', 'Total liabilities',
                'Total temporary syirkah funds', 'Total equity', 
                'Total liabilities, temporary syirkah funds and equity',
            ]]
            df = df.rename(
                columns = {
                    'Cash': 'cash_and_cash_equivalents',
                    'Total assets': 'total_assets',
                    'Total liabilities': 'total_liabilities',
                    'Total temporary syirkah funds': 'total_temporary_syirkah_funds',
                    'Total equity': 'total_equity',
                    'Total liabilities, temporary syirkah funds and equity': 'total_liabilities_syirkah_equity',
                }
            )

            # This specifically for a banking company to avoid pandas tokenization error
            # when you insert the data midway of the table
            if os.path.exists(self.file_out):
                reader = pd.read_csv(self.file_out)

                if (
                    'total_temporary_syirkah_funds' not in reader.columns or
                    'total_liabilities_syirkah_equity' not in reader.columns
                ):
                    reader['total_temporary_syirkah_funds'] = pd.NA * len(reader)
                    reader['total_liabilities_syirkah_equity'] = pd.NA * len(reader)

                    reader.to_csv('./exports/company_financial_position.csv', index=False)


            # Manually fill in the dataframe according to the columns expected for the output
            # you can fill the columns that are not exist for current dataframe with pd.NA
            # there's probably a better way to do this but...
            df['date_of_report'] = df['date_of_report']
            df['cash_and_cash_equivalents'] = df['cash_and_cash_equivalents']
            df['total_current_assets'] = pd.NA
            df['total_noncurrent_assets'] = pd.NA
            df['total_assets'] = df['total_assets']
            df['total_current_liabilities'] = pd.NA
            df['total_noncurrent_liabilities'] = pd.NA
            df['total_liabilities'] = df['total_liabilities']
            df['total_equity'] = df['total_equity']
            df['total_liabilities_and_equity'] = pd.NA
            df['total_temporary_syirkah_funds'] = df['total_temporary_syirkah_funds']
            df['total_liabilities_syirkah_equity'] = df['total_liabilities_syirkah_equity']

        else:
            df = df[[
                    'date_of_report', 'Cash and cash equivalents','Total current assets', 'Total non-current assets', 'Total assets',
                    'Total current liabilities', 'Total non-current liabilities', 'Total liabilities',
                    'Total equity', 'Total liabilities and equity',
            ]]
        
            # Rename the entire columns
            df = df.rename(
                columns = {
                    'Cash and cash equivalents': 'cash_and_cash_equivalents',
                    'Total current assets': 'total_current_assets',
                    'Total non-current assets': 'total_noncurrent_assets',
                    'Total assets': 'total_assets',
                    'Total current liabilities': 'total_current_liabilities',
                    'Total non-current liabilities': 'total_noncurrent_liabilities',
                    'Total liabilities': 'total_liabilities',
                    'Total equity': 'total_equity',
                    'Total liabilities and equity': 'total_liabilities_and_equity',
                }
            )

            # Manually fill in the dataframe according to the columns expected for the output
            # you can fill the columns that are not exist for current dataframe with pd.NA
            # there's probably a better way to do this but...
            df['date_of_report'] = df['date_of_report']
            df['cash_and_cash_equivalents'] = df['cash_and_cash_equivalents']
            df['total_current_assets'] = df['total_current_assets']
            df['total_noncurrent_assets'] = df['total_noncurrent_assets']
            df['total_assets'] = df['total_assets']
            df['total_current_liabilities'] = df['total_current_liabilities']
            df['total_noncurrent_liabilities'] = df['total_noncurrent_liabilities']
            df['total_liabilities'] = df['total_liabilities']
            df['total_equity'] = df['total_equity']
            df['total_liabilities_and_equity'] = df['total_liabilities_and_equity']
            df['total_temporary_syirkah_funds'] = pd.NA
            df['total_liabilities_syirkah_equity'] = pd.NA


        
        # Combine the two dataframe
        # axis=1 was to combine the DataFrames according to its index,
        # instead of making new row for each data inside the DataFrames like the default behaviour
        df = pd.concat([df_get_name, df], axis=1)

        # Check whether ./exports folder exists
        # os.getcwd() is to get current working directory
        current_dir = f'{os.getcwd()}/exports'
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
        
        # Define the header of the output csv file
        # this is useful to make it easier to append new header if we need it
        # combine this with a way to fill the dataframe manually like written above to ignore the empty columns for current dataframe
        head = [
            'entity_code', 'rounding_level', 'sector', 'subsector',
            'date_of_report', 'cash_and_cash_equivalents', 'total_current_assets', 'total_noncurrent_assets',
            'total_assets', 'total_current_liabilities', 'total_noncurrent_liabilities', 'total_liabilities',
            'total_equity', 'total_liabilities_and_equity', 'total_temporary_syirkah_funds', 'total_liabilities_syirkah_equity'
        ]

        # If corresponding .csv exist
        if os.path.exists(self.file_out):
            read_file_out = pd.read_csv(self.file_out)

            # Delete a row if that row has entity_code column empty and save it again
            if True in list(read_file_out['entity_code'].isna()):
                read_file_out.dropna(subset=['entity_code'], inplace=True)
                read_file_out.reset_index(drop=True)
                read_file_out.to_csv('./exports/company_financial_position.csv', index=False)

            # If entity_code in source dataframe not in corresponding .csv
            if df['entity_code'][0] not in list(set(read_file_out['entity_code'])):
                # mode = 'a' is to append, default is 'w' to write                
                df.to_csv('./exports/company_financial_position.csv', mode='a', header=False, index=False, columns=head)
            
            # If entity_code inside the corresponding .csv
            if df['entity_code'][0] in list(set(read_file_out['entity_code'])):
                # Filter the corresponding .csv based in entity_code in source dataframe
                filtered_df = read_file_out.loc[read_file_out['entity_code'] == df['entity_code'][0]]
                
                # Check whether the source dataframe's date_of_report already exist in output .csv
                if df['date_of_report'][0] not in list(filtered_df['date_of_report']):
                    df.to_csv('./exports/company_financial_position.csv', mode='a', header=False, index=False, columns=head)
        else:
            # If corresponding .csv not exist
            df.to_csv('./exports/company_financial_position.csv', index=False, columns=head)


    def profit_or_loss(self):
        sheet = self._profit_or_loss_sheet(self.file_in)
        df_get_name = self._get_company_name(self.file_in)
        profit_loss = pd.read_excel(self.file_in, sheet_name=sheet, index_col=0)

        self.file_out = './exports/profit_or_loss.csv'
        
        # Convert the dataframe into a dataframe convertable dictionary
        profit_loss_dict = {}
        for i in range(len(profit_loss)):
            key = profit_loss['Unnamed: 3'][i]
            val = profit_loss['Unnamed: 1'][i]
            profit_loss_dict[key] = [val]
            
        # Convert back to pandas Dataframe
        df = pd.DataFrame(profit_loss_dict)
        df.columns.values[0] = 'date_of_report'
        
        # Filter the irrelevant columns with .__getitem__ method aka. [[...]]
        if df_get_name['subsector'][0] == '84. Insurance' or df_get_name['subsector'][0] == '81. Bank':
            df = df[[
                'date_of_report', 'Total profit (loss)', 'Total comprehensive income'
            ]]

            df = df.rename(
                columns = {
                    'Total profit (loss)': 'total_profit',
                    'Total comprehensive income': 'total_comprehensive_income'
                }
            )

            # Manually fill in the dataframe according to the columns expected for the output
            # you can fill the columns that are not exist for current dataframe with pd.NA
            # there's probably a better way to do this but...
            df['date_of_report'] = df['date_of_report']
            df['sales_and_revenue'] = pd.NA
            df['cost'] = pd.NA
            df['gross_profit'] = pd.NA
            df['total_profit'] = df['total_profit']
            df['total_comprehensive_income'] = df['total_comprehensive_income']

        else:
            df = df[[
                'date_of_report', 'Sales and revenue', 'Cost of sales and revenue',
                'Total gross profit', 'Total profit (loss)', 'Total comprehensive income'
            ]]
        
            # Rename the columns
            df = df.rename(
                columns = {
                    'Sales and revenue': 'sales_and_revenue',
                    'Cost of sales and revenue': 'cost',
                    'Total gross profit': 'gross_profit',
                    'Total profit (loss)': 'total_profit',
                    'Total comprehensive income': 'total_comprehensive_income'
                }
            )

            # Manually fill in the dataframe according to the columns expected for the output
            # you can fill the columns that are not exist for current dataframe with pd.NA
            # there's probably a better way to do this but...
            df['date_of_report'] = df['date_of_report']
            df['sales_and_revenue'] = df['sales_and_revenue']
            df['cost'] = df['cost']
            df['gross_profit'] = df['gross_profit']
            df['total_profit'] = df['total_profit']
            df['total_comprehensive_income'] = df['total_comprehensive_income']
        
        # Combine two dataframe
        df = pd.concat([df_get_name, df], axis=1)

        # Check whether ./exports folder exists
        # os.getcwd() is to get current working directory
        current_dir = f'{os.getcwd()}/exports'
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)

        # Define the header of the output csv file
        # this is useful to make it easier to append new header if we need it
        # combine this with a way to fill the dataframe manually like written above to ignore the empty columns for current dataframe
        head = [
            'entity_code', 'rounding_level', 'sector', 'subsector',
            'date_of_report', 'sales_and_revenue', 'cost', 'gross_profit',
            'total_profit', 'total_comprehensive_income'
        ]

        # Check if the output file already exist
        if os.path.exists(self.file_out):
            read_file_out = pd.read_csv(self.file_out)
            
            # Check whether inside the output file we have a blank column based on entity_code column
            # and delete it
            if True in list(read_file_out['entity_code'].isna()):
                read_file_out.dropna(subset=['entity_code'], inplace=True)
                read_file_out.reset_index(drop=True)
                read_file_out.to_csv('./exports/profit_or_loss.csv', index=False)
            
            if df['entity_code'][0] not in list(set(read_file_out['entity_code'])):
                df.to_csv('./exports/profit_or_loss.csv', mode='a', header=False, index=False, columns=head)
            
            # Check whether entity_code from original dataframe has a duplicate in output file
            if df['entity_code'][0] in list(set(read_file_out['entity_code'])):
                
                # Filter the output file based on original file entity_code
                filtered_df = read_file_out.loc[read_file_out['entity_code'] == df['entity_code'][0]]

                # Check the duplicates data by date_of_report if there's a duplicate entity_code
                if df['date_of_report'][0] not in list(filtered_df['date_of_report']):
                    df.to_csv('./exports/profit_or_loss.csv', mode='a', header=False, index=False, columns=head)
        else:
            df.to_csv('./exports/profit_or_loss.csv', index=False, columns=head)
    
    def cashflow(self):
        sheet = self._cashflow_sheet(self.file_in)
        df_get_name = self._get_company_name(self.file_in)
        cashflow_sheet = pd.read_excel(self.file_in, sheet_name=sheet)
        
        self.file_out = './exports/cashflow.csv'
        
        # Convert original dafaframe into dataframe convertable dictionary
        cashflow_dict = {}
        for i in range(len(cashflow_sheet)):
            key = cashflow_sheet['Unnamed: 3'][i]
            value = cashflow_sheet['Unnamed: 1'][i]
            cashflow_dict[key] = [value]
        
        df = pd.DataFrame(cashflow_dict)
        
        # Rename the very first column
        df.columns.values[0] = 'date_of_report'
        
        # Filter the dataframe using .__getitem__ methods aka. [[...]]
        df = df[[
            'date_of_report', 'Total net cash flows received from (used in) operating activities',
            'Total net cash flows received from (used in) investing activities',
            'Total net cash flows received from (used in) financing activities',
            'Total net increase (decrease) in cash and cash equivalents',
            'Cash and cash equivalents cash flows, beginning of the period',
            'Effect of exchange rate changes on cash and cash equivalents',
            'Other increase (decrease) in cash and cash equivalents',
            'Cash and cash equivalents cash flows, end of the period',
        ]]
        
        # Rename the columns
        df = df.rename(
            columns = {
                'Total net cash flows received from (used in) operating activities': 'cashflow_from_operating',
                'Total net cash flows received from (used in) investing activities': 'cashflow_from_investing',
                'Total net cash flows received from (used in) financing activities': 'cashflow_from_financing',
                'Total net increase (decrease) in cash and cash equivalents': 'change_in_cash_and_equivalents',
                'Cash and cash equivalents cash flows, beginning of the period': 'cash_and_equivalents_start',
                'Effect of exchange rate changes on cash and cash equivalents': 'exchange_rate_effect',
                'Other increase (decrease) in cash and cash equivalents': 'other_change_in_cash_or_equivalents',
                'Cash and cash equivalents cash flows, end of the period': 'cash_or_equivalents_final',
            }
        )
        
        # Combine two dataframe
        df = pd.concat([df_get_name, df], axis=1)

        # Check whether ./exports folder exists
        # os.getcwd() is to get current working directory
        current_dir = f'{os.getcwd()}/exports'
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
        
        if os.path.exists(self.file_out):
            read_file_out = pd.read_csv(self.file_out)
            
            if True in list(read_file_out['entity_code'].isna()):
                read_file_out.dropna(subset=['entity_code'], inplace=True)
                read_file_out.reset_index(drop=True)
                read_file_out.to_csv('./exports/cashflow.csv', index=False)
            
            if df['entity_code'][0] not in list(set(read_file_out['entity_code'])):
                df.to_csv('./exports/cashflow.csv', mode='a', index=False, header=False)
            
            if df['entity_code'][0] in list(set(read_file_out['entity_code'])):
                filtered_df = read_file_out.loc[read_file_out['entity_code'] == df['entity_code'][0]]
                if df['date_of_report'][0] not in list(filtered_df['date_of_report']):
                    df.to_csv('./exports/cashflow.csv', mode='a', index=False, header=False)
        else:
            df.to_csv('./exports/cashflow.csv', index=False)

    def convert_all(self):
        self.general_inf()
        self.financial_pos()
        self.profit_or_loss()
        self.cashflow()

        return