import json

def validate_credentials(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    # Perform validation logic here
    if username == 'admin' and password == 'password':
        response = {'valid': True}
    else:
        response = {'valid': False}

    return HttpResponse(json.dumps(response), content_type='application/json')
