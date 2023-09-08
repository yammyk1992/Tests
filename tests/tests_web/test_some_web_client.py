from some_web_client_live import SomeWebClient
import responses


@responses.activate
def test_some_web_client():
    valid_json_answer = {'id': 3671980, 'name': 'some-name', 'status': 1,
                         'avatar': {'small': 'https://content.onliner.by/user/avatar/100x100/3671980',
                                    'large': 'https://content.onliner.by/user/avatar/300x300/3671980'}, 'cover': None,
                         'registration_date': '2023-05-14T17:09:02+03:00', 'email': None,
                         'fields': {'signature': 'TalerBY'},
                         'online_status': None,
                         'permissions': {'delete': False, 'update': False, 'change_name': False,
                                         'delete_devices': False,
                                         'delete_baraholka_adverts': False, 'delete_old_comments': False,
                                         'delete_forum_posts': False,
                                         'manage_account': False, 'manage_bans': False, 'manage_comment_bans': False,
                                         'manage_sms_validation': False, 'manage_notes': False, 'manage_roles': False,
                                         'view_accounting_acts': False, 'view_subscriptions': False,
                                         'view_transactions': False,
                                         'view_devices': False, 'restore': False}}

    responses.add(method=responses.GET, url='https://profile.onliner.by/sdapi/user.api/users/3671980?v=0.5016547602272422',
                  json=valid_json_answer, status=200)
    some_resource_client = SomeWebClient('https://profile.onliner.by')
    res = some_resource_client.get_user_registration_date(3671980)
    c = 1
