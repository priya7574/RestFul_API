import xlrd
wb = xlrd.open_workbook('test.xlsx')
sheet = wb.sheet_by_index(4)
sheet.cell_value(0, 0)
'id = db.Column(db.Integer, primary_key=True, autoincrement=True)'
for n, i in enumerate(range(1, sheet.nrows)):
    row = sheet.row_values(i)
    list = row[0], row[1]
    type=row[1]
    # email = db.Column(db.String(255), unique=True, nullable=False)
    # registered_on = db.Column(db.DateTime, nullable=False)
    if type == 'Boolean':
        d = '{0} = db.Column(db.Boolean, nullable=True, default=True)'.format(row[0], row[1])
    elif type == 'Number':
        d ='{0} = db.Column(db.Integer, nullable=True, default=True)'.format(row[0], row[1])
    elif type == '':
        continue
    elif type == 'String':
        d ='{0} = db.Column(db.String, nullable=True, default=True)'.format(row[0], row[1])
    elif type == 'Blob':
        d ='{0} = db.Column(db.Blob, nullable=True, default=True)'.format(row[0], row[1])
    elif type == 'Date':
        d ='{0} = db.Column(db.Date, nullable=True, default=True)'.format(row[0], row[1])
    elif type == 'Picklist':
        d ='{0} = db.Column(db.Picklist, nullable=True, default=True)'.format(row[0], row[1])

    print(d)


