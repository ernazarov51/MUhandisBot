import requests

BASE_URL='https://muhandisschedular-2.onrender.com/api/v1/'
groups=BASE_URL+'groups/<admin_id>'
sciences=BASE_URL+'sciences/<admin_id>'
rooms=BASE_URL+'rooms/<admin_id>'
teachers=BASE_URL+'teachers/<admin_id>'
lesson=BASE_URL+'lesson<admin_id>'
frontend_url='https://preview-okmk-admin-panel-kzmqem5t7ktoyv5npl6h.vusercontent.net'

def get_lesson_list_by_group(group_id):
    return BASE_URL+f'lesson-depth-one/{group_id}'
