"""Google Sheets API utilities"""

from typing import *

import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheet:
    """A Google SpreadSheet object that is initialized based
    on a `credentials.json` file in your Python Path.

    TODO: Explain what the structure of the credential JSON file
    looks like.
    """

    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'credentials.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open('worldometers').sheet1

    def append_row(
        self,
        data_dict: Dict[str, Any],
    ):
        """Appends a row to the spreadsheet. This function uses the 
        following values:
        
        values: [
            'country',
            'active_cases',
            'cases_per_million',
            'critical',
            'new_cases',
            'new_deaths',
            'total_cases',
            'total_deaths',
            'total_recoveries',
        ]
        """

        values = [
            data_dict['country'],
            data_dict['active_cases'],
            data_dict['cases_per_million'],
            data_dict['critical'],
            data_dict['new_cases'],
            data_dict['new_deaths'],
            data_dict['total_cases'],
            data_dict['total_deaths'],
            data_dict['total_recoveries'],
        ]

        self.sheet.append_row(
            values=values,
        )

    def update_lang(
        self,
        index: int,
        lang: str,
    ) -> None:
        "TODO: Mind explaining @vipermu ?"
        self.sheet.update_cell(
            row=index + 2,
            col=2,
            value=lang,
        )

    def update_history(
        self,
        index: int,
        new_hist: str,
    ) -> None:
        "TODO: Mind explaining @vipermu ?"
        self.sheet.update_cell(
            row=index + 2,
            col=3,
            value=new_hist,
        )