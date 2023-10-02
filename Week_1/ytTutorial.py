# Youtube Turorial
import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('10tGxWSu28sSfOFLmcZKB5siRmCfuEafqjabH_bDNl60')
worksheet = sh.sheet1

#will return information inside the sheet
#res = worksheet.get_all_records()
#res = worksheet.get_all_values()
res = worksheet.row_values(1)
#res = worksheet.get('A1:A2')
user = ["Susan", 25 ]
worksheet.insert_row(user,2)
worksheet.delete_rows(2)
print(res)