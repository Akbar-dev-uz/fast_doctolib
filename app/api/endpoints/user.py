from fastapi import APIRouter

user_router = APIRouter()


@user_router.get('/')
async def get_user():
    return {'message': 'Hello World'}
