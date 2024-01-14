import requests
import re
import json
from requests import get
from time import time, sleep
from urllib.parse import urlencode
from datetime import datetime
from datetime import timedelta

def get_post(params, url, headers):
    try:
        response = requests.get(url=url, params=params, headers=headers)
        return response
    except:
        sleep(5)
        return get_post(params, url, headers)
def get_situation(ad='钉钉', url='https://www.douyin.com/user/MS4wLjABAAAAdnwM98hf2G2ivOlk9sc0VIAywdu2hLry1LCwGrm9X-w'):
    cookie = 'douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; __ac_referer=https://www.douyin.com/user/MS4wLjABAAAA3y0gs9xhygmvZhVEHWt5Y4aLHi9KooKSNxVQ2pslu10; ttwid=1%7CYxJoy5cC4_51ZOuZK2n7pPjnv91Gavk0R0jOy9_JWIE%7C1703119835%7C8b2603dd3d6b7302c9607ca4dc7e57237637e940d26ec7b2b19942bd8069c08f; dy_swidth=1440; dy_sheight=960; s_v_web_id=verify_lqehktvc_OILF8jxv_lOko_4fzw_Bj6i_tOc8XqtvtaFu; passport_csrf_token=e8f57958402c9f254c102828fe1e2efb; passport_csrf_token_default=e8f57958402c9f254c102828fe1e2efb; bd_ticket_guard_client_web_domain=2; csrf_session_id=ec122a85079095da2fc1cfcc483f1037; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20231221%2F1%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=Ld_2sVp0ll_u6mp6b_LurZQyiDFye8Ekksyi0O0RcOo; passport_auth_status=9de3935ced0b493f12bbd223522a5d61%2C; passport_auth_status_ss=9de3935ced0b493f12bbd223522a5d61%2C; publish_badge_show_info=%220%2C0%2C0%2C1703831076774%22; strategyABtestKey=%221703831078.104%22; _bd_ticket_crypt_doamin=2; store-region=cn-bj; store-region-src=uid; __security_server_data_status=1; passport_assist_user=CjwPz7rPkyDLe-vL7ERFGU-0sQDYCF9_rFKpVpQf0q33WT4O5WIrMFHDYe9c3FQq14xeTSXv4jAlqA9_C-waSgo86_VTn-yXs1VOWGM_-B0s_N7-CzNgYBuVT8bmvS2GAp74-iMWFjf99wixo_EXXZ6k-JZfBR5Adm4SgDtiELObxQ0Yia_WVCABIgEDE4Hv3w%3D%3D; sso_uid_tt=6165c5a4b5393ec547012f7c19828c71; sso_uid_tt_ss=6165c5a4b5393ec547012f7c19828c71; toutiao_sso_user=3e0d874dd585c91429edcd6e376f19ce; toutiao_sso_user_ss=3e0d874dd585c91429edcd6e376f19ce; sid_ucp_sso_v1=1.0.0-KGJmOGQzY2RkNjljM2Q0MmFiMjliMDFmMThmMjg2ZjNjZDRiZWFjYTIKHwj74b6ujAIQw-u5rAYY7zEgDDC27__OBTgFQPsHSAMaAmxxIiAzZTBkODc0ZGQ1ODVjOTE0MjllZGNkNmUzNzZmMTljZQ; ssid_ucp_sso_v1=1.0.0-KGJmOGQzY2RkNjljM2Q0MmFiMjliMDFmMThmMjg2ZjNjZDRiZWFjYTIKHwj74b6ujAIQw-u5rAYY7zEgDDC27__OBTgFQPsHSAMaAmxxIiAzZTBkODc0ZGQ1ODVjOTE0MjllZGNkNmUzNzZmMTljZQ; uid_tt=e16bc823cecd572bc58c362027664947; uid_tt_ss=e16bc823cecd572bc58c362027664947; sid_tt=25f728ccada64c912281607a3ac576d7; sessionid=25f728ccada64c912281607a3ac576d7; sessionid_ss=25f728ccada64c912281607a3ac576d7; _bd_ticket_crypt_cookie=76c90f9795b51364094d6383440024a6; LOGIN_STATUS=1; sid_guard=25f728ccada64c912281607a3ac576d7%7C1703835081%7C5183997%7CTue%2C+27-Feb-2024+07%3A31%3A18+GMT; sid_ucp_v1=1.0.0-KDZlODdlNWMwNjA0ZDljNTM0YzgwNzg2MWUxZmRhNjgwMGY2MTUwOTgKGQj74b6ujAIQyeu5rAYY7zEgDDgFQPsHSAQaAmhsIiAyNWY3MjhjY2FkYTY0YzkxMjI4MTYwN2EzYWM1NzZkNw; ssid_ucp_v1=1.0.0-KDZlODdlNWMwNjA0ZDljNTM0YzgwNzg2MWUxZmRhNjgwMGY2MTUwOTgKGQj74b6ujAIQyeu5rAYY7zEgDDgFQPsHSAQaAmhsIiAyNWY3MjhjY2FkYTY0YzkxMjI4MTYwN2EzYWM1NzZkNw; passport_fe_beating_status=true; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.6%7D; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22; pwa2=%220%7C0%7C3%7C1%22; __ac_nonce=0658ea20f00c3680c4da7; __ac_signature=_02B4Z6wo00f016aNqxgAAIDAmySxhBzyq3Omra-AAIw267MPKwL6drWjctCruPxZf8Lrze.3ucapFYdXDsVtfqF9DRjosTotVO6UD3DMtPTRpssHIaqFlIpCRVEdRaSMOok5Ufi2aKIf2mcUa4; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSTUrV3gwajZGZFJyNFAzR245ZUNYSVhYS1NRWUtIaHc5UzdJQmVuUDZCTXFDR3RaSTJ5RG1nMzVqbHFTakJvTjlQOFRYTW9EU0NyQTRUL3dHak9Fcm89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=jfIphBIlIDK6SC9Wvw6B18guSHjMGs-No_kIt2Z-s3IVrXadMhU8NcAag3iEkVNYos11lJNarnj7eOdp1F47jfRfXdoQW89hoQHERQpNH8yHJvASh7gzlw==; tt_scid=Dus9zT.0zXxeyuzx17dwhOhVc900MJ9HhjZcE3ZmItKQfb3j3el.yaRJrCcsGOQx93d9; home_can_add_dy_2_desktop=%221%22; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAnOVhWteHlcX1uMzCR3Q1JMzgMINKPzSEmdOiJJ6zDCM%2F1703865600000%2F0%2F0%2F1703847041787%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAnOVhWteHlcX1uMzCR3Q1JMzgMINKPzSEmdOiJJ6zDCM%2F1703865600000%2F0%2F1703846441795%2F0%22; msToken=olHB7060R6mN_wDkmQPLN9ZsXB4l8bxLuyLkzDFdEhW8j5y4ibjAth0DDRz5dHudWYtsr6xk3SO1Q3Nmxh9pRHmRIMaHxEsTgjwnqHhvc1XFvNkLpDrosQ==; odin_tt=e5792702617539a31b13e6a8a20336b25898180ad3ae146e318b8a63f98c7c6b8429e1596ad7e70a4505076610d754c2d683a439629e72db820560a711428287; IsDouyinActive=false'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    ad_html = f'../{ad}/源/源码.html'
    ad_json = f'../{ad}/源/源码.json'
    ad_csv = f'../{ad}/账户信息.csv'
    headers = {
        'cookie': cookie,  # change with your cookie
        'User-Agent': ua
    }

    res = requests.get(url=url, headers=headers)
    with open(ad_html, 'w', encoding='utf-8') as f:
        f.write(res.text)

    data = re.search(r'\{(.*)\}', re.findall(r'self.__pace_f.push\((.*?)\)', res.text)[-1]).group(0).replace('\\', '')

    with open(ad_json, 'w', encoding='utf-8') as f:
        f.write(data)
    data_json = json.loads(data)
    basic_situation = {
        '账户名称': 'realName',
        '抖音号': 'uniqueId',
        '用户简介': 'desc',
        '粉丝数': 'followerCount',
        '总获赞数': 'totalFavorited',
        '视频数': 'awemeCount'
    }
    situation_total = {}
    for i in basic_situation.items():
        with open(ad_csv, 'a+', encoding='utf-8') as f:
            f.write(f"{i[0]},{data_json['user']['user'][i[1]]}\n")
        situation_total[i[0]] = data_json['user']['user'][i[1]]
    situation_total['ip'] = f"{data_json['user']['user']['ipLocation']}"  if data_json['user']['user']['ipLocation'] else f"{data_json['user']['user']['country']}{data_json['user']['user']['province']}{data_json['user']['user']['city']}{data_json['user']['user']['district']}{data_json['user']['user']['school']}"
    with open(ad_csv, 'a+', encoding='utf-8') as f:
        f.write(f"ip地址,{situation_total['ip']}")
    print(situation_total)
    return situation_total


def get_video(ad='钉钉', sec_user_id='MS4wLjABAAAAdnwM98hf2G2ivOlk9sc0VIAywdu2hLry1LCwGrm9X-w'):
    cookie = 'douyin.com; ttwid=1%7CYxJoy5cC4_51ZOuZK2n7pPjnv91Gavk0R0jOy9_JWIE%7C1703119835%7C8b2603dd3d6b7302c9607ca4dc7e57237637e940d26ec7b2b19942bd8069c08f; dy_swidth=1440; dy_sheight=960; s_v_web_id=verify_lqehktvc_OILF8jxv_lOko_4fzw_Bj6i_tOc8XqtvtaFu; passport_csrf_token=e8f57958402c9f254c102828fe1e2efb; passport_csrf_token_default=e8f57958402c9f254c102828fe1e2efb; bd_ticket_guard_client_web_domain=2; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20231221%2F1%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; n_mh=Ld_2sVp0ll_u6mp6b_LurZQyiDFye8Ekksyi0O0RcOo; passport_auth_status=9de3935ced0b493f12bbd223522a5d61%2C; passport_auth_status_ss=9de3935ced0b493f12bbd223522a5d61%2C; publish_badge_show_info=%220%2C0%2C0%2C1703831076774%22; _bd_ticket_crypt_doamin=2; store-region=cn-bj; store-region-src=uid; __security_server_data_status=1; passport_assist_user=CjwPz7rPkyDLe-vL7ERFGU-0sQDYCF9_rFKpVpQf0q33WT4O5WIrMFHDYe9c3FQq14xeTSXv4jAlqA9_C-waSgo86_VTn-yXs1VOWGM_-B0s_N7-CzNgYBuVT8bmvS2GAp74-iMWFjf99wixo_EXXZ6k-JZfBR5Adm4SgDtiELObxQ0Yia_WVCABIgEDE4Hv3w%3D%3D; sso_uid_tt=6165c5a4b5393ec547012f7c19828c71; sso_uid_tt_ss=6165c5a4b5393ec547012f7c19828c71; toutiao_sso_user=3e0d874dd585c91429edcd6e376f19ce; toutiao_sso_user_ss=3e0d874dd585c91429edcd6e376f19ce; sid_ucp_sso_v1=1.0.0-KGJmOGQzY2RkNjljM2Q0MmFiMjliMDFmMThmMjg2ZjNjZDRiZWFjYTIKHwj74b6ujAIQw-u5rAYY7zEgDDC27__OBTgFQPsHSAMaAmxxIiAzZTBkODc0ZGQ1ODVjOTE0MjllZGNkNmUzNzZmMTljZQ; ssid_ucp_sso_v1=1.0.0-KGJmOGQzY2RkNjljM2Q0MmFiMjliMDFmMThmMjg2ZjNjZDRiZWFjYTIKHwj74b6ujAIQw-u5rAYY7zEgDDC27__OBTgFQPsHSAMaAmxxIiAzZTBkODc0ZGQ1ODVjOTE0MjllZGNkNmUzNzZmMTljZQ; uid_tt=e16bc823cecd572bc58c362027664947; uid_tt_ss=e16bc823cecd572bc58c362027664947; sid_tt=25f728ccada64c912281607a3ac576d7; sessionid=25f728ccada64c912281607a3ac576d7; sessionid_ss=25f728ccada64c912281607a3ac576d7; _bd_ticket_crypt_cookie=76c90f9795b51364094d6383440024a6; LOGIN_STATUS=1; sid_guard=25f728ccada64c912281607a3ac576d7%7C1703835081%7C5183997%7CTue%2C+27-Feb-2024+07%3A31%3A18+GMT; sid_ucp_v1=1.0.0-KDZlODdlNWMwNjA0ZDljNTM0YzgwNzg2MWUxZmRhNjgwMGY2MTUwOTgKGQj74b6ujAIQyeu5rAYY7zEgDDgFQPsHSAQaAmhsIiAyNWY3MjhjY2FkYTY0YzkxMjI4MTYwN2EzYWM1NzZkNw; ssid_ucp_v1=1.0.0-KDZlODdlNWMwNjA0ZDljNTM0YzgwNzg2MWUxZmRhNjgwMGY2MTUwOTgKGQj74b6ujAIQyeu5rAYY7zEgDDgFQPsHSAQaAmhsIiAyNWY3MjhjY2FkYTY0YzkxMjI4MTYwN2EzYWM1NzZkNw; pwa2=%220%7C0%7C3%7C1%22; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; csrf_session_id=e59364c87926c1d1eb74f48f3d27adb0; strategyABtestKey=%221703900104.699%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.6%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; xg_device_score=7.379650438414911; __ac_nonce=0658f934d00a3d4932650; __ac_signature=_02B4Z6wo00f01UwBeLgAAIDCcahiJUEA60lMIXwAADaTrBhHjH2A1PBXbQ9sVE3y54RQrmAxToTNXis28imuKx-RW7WpFQbg2o5wgetHekVNmi4MQZJQrfxfJay8pyAJmN0q6ckwgeOBKLowc4; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAnOVhWteHlcX1uMzCR3Q1JMzgMINKPzSEmdOiJJ6zDCM%2F1703952000000%2F0%2F0%2F1703909806909%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAnOVhWteHlcX1uMzCR3Q1JMzgMINKPzSEmdOiJJ6zDCM%2F1703952000000%2F0%2F0%2F1703910406911%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1440%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSTUrV3gwajZGZFJyNFAzR245ZUNYSVhYS1NRWUtIaHc5UzdJQmVuUDZCTXFDR3RaSTJ5RG1nMzVqbHFTakJvTjlQOFRYTW9EU0NyQTRUL3dHak9Fcm89IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; home_can_add_dy_2_desktop=%221%22; msToken=GryhMW5EcxcbxP1j8LJe062fI-6pcsldJpDT3vdIhXBiM69HKXjaveMNueyoReA_zc2MwDy0c0IYv1AaJzJo30bPa9RmxbiWmqrGt5hRhhMM5wInKMsRFl3N69eNJyc=; msToken=C9X4qdg6qFRX0VKHkkHl9hmY-OLmKALx8w6fJIZoCpqLMxWgqjrmQko2XF_PuLmSi1wR6yv9oRG0OYYxJucVxo3vvvIqieXKBZBK3vGZjsM6fw28UPHi5PFBqTwz0ps=; odin_tt=6c43061f21aedf78c87cc7b133aaa19322607607611fdc6dc1e9cfb45f3ae6fce983536d2670619eb70d6da69f8799d5; tt_scid=8AzI7.ZNFNYV0K.kGUD8SpcJZ6lZBIxe0gAPRXMnXSL-uSU.gP5kNii9qQeZBo2r5544; IsDouyinActive=false; passport_fe_beating_status=false'
    params_ = {
        'aid': '6383',
        'sec_user_id': sec_user_id,
        'max_cursor': str(int(round(time() * 1000))),
    }
    video_list = []
    video_ad_list = []
    aweme_id = []
    comment = []
    num_0 = 0
    url_api = 'https://www.douyin.com/aweme/v1/web/comment/list/?'
    url = f'https://www.douyin.com/aweme/v1/web/aweme/post/?'
    api_url_reply = 'https://www.douyin.com/aweme/v1/web/comment/list/reply/?'

    headers = {
        'referer': f'https://www.douyin.com/user/{sec_user_id}',
        'cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    with open(f'../{ad}/视频链接.csv', 'w', encoding='utf-8') as f:
        f.write('名称,aweme_id,发布时间,点赞数,评论数,收藏数,转发量,时长,视频地址\n')
    with open(f'../{ad}/评论信息.csv', 'w', encoding='utf-8') as f:
        f.write('名称,评论内容,aweme_id,cid,发布时间,点赞数,ip地址\n')
    has_more = True
    while has_more:
        try:
            num_1 = 0
            params = params_.copy()
            XB = get('http://xb.tom14.top/?', params={'form': urlencode(params)}).json()
            xb = XB['data']["X_Bogus"]
            params['X-Bogus'] = xb
            try:
                data = get(url, headers=headers, params=params).json()
            except:
                sleep(5)
                continue
            with open(f'../{ad}/视频信息/{params_["max_cursor"]}.json', 'w') as f:
                json.dump(data, f)
            for post in data['aweme_list']:
                params_comment = {
                    'aid': '6383',
                    'aweme_id': post['aweme_id'],
                    'count': 50,
                    'cursor': num_1*20
                }

                data_comment = get_post(params_comment, url_api, headers)
                if data_comment:
                    data_comment = data_comment.json()
                with open(f'../{ad}/评论信息/{num_0}{num_1}.json', 'a+', encoding='utf-8') as f:
                    f.write(str(data_comment))
                if data_comment['comments']:
                    for i in data_comment['comments']:
                        try:
                            ip = i['ip_label']
                        except:
                            ip = None

                        comment.append(f"{i['user']['nickname']},{i['text']},{i['aweme_id']},{i['cid']},{i['create_time']},{i['digg_count']},{ip}")

                print(post['desc'].encode().decode('utf-8'))
                video_list.append(f"{post['desc'].encode().decode('utf-8')},{post['aweme_id']}, {post['create_time']},{post['statistics']['digg_count']},{post['statistics']['comment_count']},{post['statistics']['collect_count']},{post['statistics']['share_count']},{int(post['duration'])/1000}秒")
                video_ad_list.append(f"{post['video']['play_addr']['url_list'][0]}")
                file_comment = open(f'../{ad}/评论信息.csv', 'a+', encoding='utf-8')
                for i in comment:
                    file_comment.write(i)
                    file_comment.write('\n')
                file_comment.write('\n')
                file_comment.close()
                aweme_id.append(f"?{post['aweme_id']}")
                num_1 += 1
                comment = []
                print(1)

            params_['max_cursor'] = data['max_cursor']
            has_more = data['has_more']

            num_0 += 1
            sleep(1)
            if num_0 > 1000:
                break
        except:
            break
    print(len(video_list) == len(video_ad_list))
    print(aweme_id)
    print(comment)
    for i in range(len(video_list)):
        file = open(f'../{ad}/视频链接.csv', 'a+', encoding='utf-8')
        file.write(f"{video_list[i]}, {video_ad_list[i]}")
        file.write('\n')
        file.close()



# get_situation()
get_video()



