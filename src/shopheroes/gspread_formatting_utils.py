from gspread_formatting import CellFormat


def rightpad(row, max_len):
    pad_len = max_len - len(row)
    return row + ([None] * pad_len) if pad_len != 0 else row


def fill_gaps(L, rows=None, cols=None):

    max_cols = max(len(row) for row in L) if cols is None else cols
    max_rows = len(L) if rows is None else rows

    pad_rows = max_rows - len(L)

    if pad_rows:
        L = L + ([[]] * pad_rows)

    return [rightpad(row, max_cols) for row in L]


def get_effective_formats(worksheet):
    label = worksheet.title

    resp = worksheet.spreadsheet.fetch_sheet_metadata({
        'includeGridData': True,
        'ranges': [label],
        'fields': 'sheets.data.rowData.values.effectiveFormat'
    })
    result = []
    for row in resp['sheets'][0]['data'][0]['rowData']:
        result_row = []
        for cell in row['values']:
            print(cell)
            props = cell.get('effectiveFormat')
            result_row.append(CellFormat.from_props(props) if props else None)
        result.append(result_row)
    return fill_gaps(result)
