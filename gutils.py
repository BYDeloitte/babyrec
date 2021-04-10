from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

class GoogleConnector():
    def __init__(self,scope=None,cred_json=None,spreadsheet_id=None):
        scope=['https://www.googleapis.com/auth/drive.readonly','https://www.googleapis.com/auth/spreadsheets'] if scope is None else scope
        cred_json='BabyRec-0083cc5b51cb.json' if cred_json is None else cred_json
        creds=Credentials.from_service_account_file(cred_json,scopes=scope)
        self.gsheet=build('sheets','v4',credentials=creds).spreadsheets()
        self.spreadsheet_id='1dX7OtIp7wDVDQXBidfD_Tx1E8h0cuEAxW05suWKTQCk' if spreadsheet_id is None else spreadsheet_id
        self.sheets={'milk':0}
    
    def add_data(self,sheet,data,range='milk!A1'):
        # insert empty row at top of table
        ins_range={'sheetId':self.sheets[sheet],'dimension':'ROWS','startIndex':1,'endIndex':2}
        ins_dim={'range':ins_range,'inheritFromBefore':'false'}
        req_body={'requests':[{'insertDimension':ins_dim}]}
        self.gsheet.batchUpdate(spreadsheetId=self.spreadsheet_id,body=req_body).execute()

        # populate with values
        self.gsheet.values().append(spreadsheetId=self.spreadsheet_id,range=range,valueInputOption='USER_ENTERED',insertDataOption='OVERWRITE',body=data).execute()