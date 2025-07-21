import requests

BASE_URL=' https://35404821272c.ngrok-free.app/api/v1/'
groups=BASE_URL+'groups'
sciences=BASE_URL+'sciences'
rooms=BASE_URL+'rooms'
teachers=BASE_URL+'teachers'
lesson=BASE_URL+'lesson'

def get_lesson_list_by_group(group_id):
    return BASE_URL+f'lesson-depth-one/{group_id}'
