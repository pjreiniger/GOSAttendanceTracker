import gspread


##def lookupID(fname, lname):
##    pass
##

def lookupName(idNumber):
    for i in range(len(lastNames)):
        if (ids[i] == idNumber):
            return(firstNames[i] + " " + lastNames[i])

    return None


def updateIDData(SK):
    sh = gc.open_by_key(SK)

    wl = sh.worksheets()

    ds = wl[1]
    ln = ds.col_values(1)[1:]
    fn = ds.col_values(2)[1:]
    newIDs = ds.col_values(3)[1:]

    return ln, fn, newIDs


def login(SK, name, ID):
    sh = gc.open_by_key(SK)
    wl = sh.worksheets()

    ds = wl[1]
    ds.append_row([date, ID, name, "General Meeting"])

    



SPREADSHEET_KEY = "163-AIfY7czQUz-1WUggts3lUEXNV6TebKseutOeIeDI"


gc = gspread.service_account(filename='credentials.json')

sh = gc.open_by_key(SPREADSHEET_KEY)

worksheet_list = sh.worksheets()

databaseSheet = worksheet_list[1]
lastNames = databaseSheet.col_values(1)[1:]
firstNames = databaseSheet.col_values(2)[1:]
ids = databaseSheet.col_values(3)[1:]

for i in range(len(ids)):
    ids[i] = int(ids[i])
    

print(lookupName(3504000028))

attendanceSheet = worksheet_list[0]


#print(sh.sheet1.get('A1'))






