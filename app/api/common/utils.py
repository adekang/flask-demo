def res(data=None, message='Ok', success=True, code=200):
    return {
        'success': success,
        'message': message,
        'data': data,
    }, code
