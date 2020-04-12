import gspread
from oauth2client.service_account import ServiceAccountCredentials


class SpreadSheet:
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
    ):
        self.sheet.update_cell(
            row=index + 2,
            col=2,
            value=lang,
        )

    def update_history(
        self,
        index: int,
        new_hist: str,
    ):
        self.sheet.update_cell(
            row=index + 2,
            col=3,
            value=new_hist,
        )