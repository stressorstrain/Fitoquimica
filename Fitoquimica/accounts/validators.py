
def validation(mime, tipo):
    doc=[
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        'application/msword',
        'vnd.oasis.opendocument.text',
        'application/rtf',
        'text/plain'
    ]

    pdf = ['application/pdf']

    tables = [
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-works'
        'application/vnd.ms-excel',
        'officedocument.spreadsheetml.sheet',
        'application/vnd.oasis.opendocument.spreadsheet',
        'text/csv',

    ]
    outros = [
        'application/vnd.ms-powerpoint',
        'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'application/vnd.oasis.opendocument.presentation',
        'image/jpeg',
        'image/gif',
        'image/png',
        'application/x-rar-compressed',
        'image/svg+xml',
        'application/zip',
    ]
    if tipo == 1  and mime in doc:
        return True
    elif tipo==2 and mime in tables:
        return True
    elif tipo == 3 and mime in pdf:
        return True
    elif tipo == 4 and mime in outros:
        return True
    else:
        return False