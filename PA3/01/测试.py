import requests
import re
import json
from requests import get
from time import time, sleep
from urllib.parse import parse_qs, urlparse
from urllib.parse import urlencode


def get_fans_list(ad='人民日报', url='https://www.douyin.com/user/MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4'):
    cookie = 'douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; __ac_referer=https://www.douyin.com/user/MS4wLjABAAAA3y0gs9xhygmvZhVEHWt5Y4aLHi9KooKSNxVQ2pslu10; ttwid=1%7CYxJoy5cC4_51ZOuZK2n7pPjnv91Gavk0R0jOy9_JWIE%7C1703119835%7C8b2603dd3d6b7302c9607ca4dc7e57237637e940d26ec7b2b19942bd8069c08f; dy_swidth=1440; dy_sheight=960; s_v_web_id=verify_lqehktvc_OILF8jxv_lOko_4fzw_Bj6i_tOc8XqtvtaFu; passport_csrf_token=e8f57958402c9f254c102828fe1e2efb; passport_csrf_token_default=e8f57958402c9f254c102828fe1e2efb; bd_ticket_guard_client_web_domain=2; csrf_session_id=ec122a85079095da2fc1cfcc483f1037; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20231221%2F1%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=Ld_2sVp0ll_u6mp6b_LurZQyiDFye8Ekksyi0O0RcOo; passport_auth_status=9de3935ced0b493f12bbd223522a5d61%2C; passport_auth_status_ss=9de3935ced0b493f12bbd223522a5d61%2C; publish_badge_show_info=%220%2C0%2C0%2C1703831076774%22; strategyABtestKey=%221703831078.104%22; _bd_ticket_crypt_doamin=2; store-region=cn-bj; store-region-src=uid; __security_server_data_status=1; passport_assist_user=CjwPz7rPkyDLe-vL7ERFGU-0sQDYCF9_rFKpVpQf0q33WT4O5WIrMFHDYe9c3FQq14xeTSXv4jAlqA9_C-waSgo86_VTn-yXs1VOWGM_-B0s_N7-CzNgYBuVT8bmvS2GAp74-iMWFjf99wixo_EXXZ6k-JZfBR5Adm4SgDtiELObxQ0Yia_WVCABIgEDE4Hv3w%3D%3D; sso_uid_tt=6165c5a4b5393ec547012f7c19828c71; sso_uid_tt_ss=6165c5a4b5393ec547012f7c19828c71; toutiao_sso_user=3e0d874dd585c91429edcd6e376f19ce; toutiao_sso_user_ss=3e0d874dd585c91429edcd6e376f19ce; sid_ucp_sso_v1=1.0.0-KGJmOGQzY2RkNjljM2Q0MmFiMjliMDFmMThmMjg2ZjNjZDRiZWFjYTIKHwj74b6ujAIQw-u5rAYY7zEgDDC27__OBTgFQPsHSAMaAmxxIiAzZTBkODc0ZGQ1ODVjOTE0MjllZGNkNmUzNzZmMTljZQ; ssid_ucp_sso_v1=1.0.0-KGJmOGQzY2RkNjljM2Q0MmFiMjliMDFmMThmMjg2ZjNjZDRiZWFjYTIKHwj74b6ujAIQw-u5rAYY7zEgDDC27__OBTgFQPsHSAMaAmxxIiAzZTBkODc0ZGQ1ODVjOTE0MjllZGNkNmUzNzZmMTljZQ; uid_tt=e16bc823cecd572bc58c362027664947; uid_tt_ss=e16bc823cecd572bc58c362027664947; sid_tt=25f728ccada64c912281607a3ac576d7; sessionid=25f728ccada64c912281607a3ac576d7; sessionid_ss=25f728ccada64c912281607a3ac576d7; _bd_ticket_crypt_cookie=76c90f9795b51364094d6383440024a6; LOGIN_STATUS=1; sid_guard=25f728ccada64c912281607a3ac576d7%7C1703835081%7C5183997%7CTue%2C+27-Feb-2024+07%3A31%3A18+GMT; sid_ucp_v1=1.0.0-KDZlODdlNWMwNjA0ZDljNTM0YzgwNzg2MWUxZmRhNjgwMGY2MTUwOTgKGQj74b6ujAIQyeu5rAYY7zEgDDgFQPsHSAQaAmhsIiAyNWY3MjhjY2FkYTY0YzkxMjI4MTYwN2EzYWM1NzZkNw; ssid_ucp_v1=1.0.0-KDZlODdlNWMwNjA0ZDljNTM0YzgwNzg2MWUxZmRhNjgwMGY2MTUwOTgKGQj74b6ujAIQyeu5rAYY7zEgDDgFQPsHSAQaAmhsIiAyNWY3MjhjY2FkYTY0YzkxMjI4MTYwN2EzYWM1NzZkNw; passport_fe_beating_status=true; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.6%7D; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; pwa2=%220%7C0%7C3%7C1%22; __ac_nonce=0658ea20f00c3680c4da7; __ac_signature=_02B4Z6wo00f016aNqxgAAIDAmySxhBzyq3Omra-AAIw267MPKwL6drWjctCruPxZf8Lrze.3ucapFYdXDsVtfqF9DRjosTotVO6UD3DMtPTRpssHIaqFlIpCRVEdRaSMOok5Ufi2aKIf2mcUa4; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSTUrV3gwajZGZFJyNFAzR245ZUNYSVhYS1NRWUtIaHc5UzdJQmVuUDZCTXFDR3RaSTJ5RG1nMzVqbHFTakJvTjlQOFRYTW9EU0NyQTRUL3dHak9Fcm89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=jfIphBIlIDK6SC9Wvw6B18guSHjMGs-No_kIt2Z-s3IVrXadMhU8NcAag3iEkVNYos11lJNarnj7eOdp1F47jfRfXdoQW89hoQHERQpNH8yHJvASh7gzlw==; tt_scid=Dus9zT.0zXxeyuzx17dwhOhVc900MJ9HhjZcE3ZmItKQfb3j3el.yaRJrCcsGOQx93d9; home_can_add_dy_2_desktop=%221%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAnOVhWteHlcX1uMzCR3Q1JMzgMINKPzSEmdOiJJ6zDCM%2F1703865600000%2F0%2F0%2F1703847041787%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAnOVhWteHlcX1uMzCR3Q1JMzgMINKPzSEmdOiJJ6zDCM%2F1703865600000%2F0%2F1703846441795%2F0%22; msToken=olHB7060R6mN_wDkmQPLN9ZsXB4l8bxLuyLkzDFdEhW8j5y4ibjAth0DDRz5dHudWYtsr6xk3SO1Q3Nmxh9pRHmRIMaHxEsTgjwnqHhvc1XFvNkLpDrosQ==; odin_tt=e5792702617539a31b13e6a8a20336b25898180ad3ae146e318b8a63f98c7c6b8429e1596ad7e70a4505076610d754c2d683a439629e72db820560a711428287; IsDouyinActive=false'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ad_html = f'../{ad}/源/粉丝列表源码.html'
    ad_json = f'../{ad}/源/粉丝列表源码.json'
    ad_csv = f'../{ad}/粉丝列表.csv'
    headers = {
        'cookie': cookie,
        'User-Agent': ua
    }

    sec_user_id = 'MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4'
    url_api = 'https://www.douyin.com/aweme/v1/web/user/follower/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&user_id=104255897823&sec_user_id=MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4&offset=0&min_time=0&max_time=0&count=20&source_type=3&gps_access=0&address_book_access=0&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1440&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=120.0.0.0&browser_online=true&engine_name=Blink&engine_version=120.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7319862193234265639&msToken=tzPZChc6Ohd3UFyaiVQZ7z7-0Ptubyk3UXvFdkeFPeWfFxa2qNctwcpcHTLGZlWQjLJEkQT7gfp5pk3rpcxR_vsKbycIuUYLIDdx64sa34BglS-NPvkOvQRplkRn&X-Bogus=DFSzswVufJhAN9oEt7LeOvB9PimK'
    params = parse_qs(urlparse(url_api).query)
    print('\n'.join(f'{key}: {value[0]}' for key, value in params.items()))
    params_ = {
        'aid': '6383',
        'count': 20,
        'sec_user_id': sec_user_id,
        'user_id': '104255897823',
        'webid': '7319862193234265639',
        'cookie_enabled': 'true',
        'offset': 0,
        'browser_online': 'true',
        'msToken': 'tzPZChc6Ohd3UFyaiVQZ7z7-0Ptubyk3UXvFdkeFPeWfFxa2qNctwcpcHTLGZlWQjLJEkQT7gfp5pk3rpcxR_vsKbycIuUYLIDdx64sa34BglS-NPvkOvQRplkRn'
    }
    params1 = params_.copy()
    XB = get('http://xb.tom14.top/?', params={'form': urlencode(params1)}).json()
    xb = XB['data']["X_Bogus"]
    params1['X-Bogus'] = xb
    url = 'https://www.douyin.com/aweme/v1/web/user/follower/list/?'
    data_user = requests.get(url=url, params=params1, headers=headers).json()
    with open(ad_json, 'w', encoding='utf-8') as f:
        f.write(str(data_user))


get_fans_list()