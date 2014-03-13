
def user(request):
    user = request.user
    return {'user':user}