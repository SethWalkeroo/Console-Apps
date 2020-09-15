from googleapiclient.discovery import build
from colored import bg, attr, fg


highlight = bg(16) + fg('white')
reset = attr('reset')
border_color = fg('pale_green_1a')
error = fg('red_3a')

def youtube_search(keyword, total_results=151):

    with open('../data/api-key.txt', 'r') as api_file:
        api_key = api_file.read()

    video_lookup = {}

    youtube = build('youtube', 'v3', developerKey=api_key)

    vid_search_request = youtube.search().list(
    part='snippet',
    q=keyword,
    videoDefinition='any',
    relevanceLanguage='en',
    maxResults=total_results,
    )

    video_response = vid_search_request.execute()

    for count in range(total_results):
        try:
            video_info = video_response['items'][count]['snippet']
            video_id = video_response['items'][count]['id']['videoId']
            video_title = video_info['title']
            channel_title = video_info['channelTitle']
            description = video_info['description']
            video_lookup.update({count:video_id})

            print()
            print('=' * 150)
            print(highlight + str(count + 1) + reset)
            print()
            print(highlight + video_title + reset)
            print()
            print(channel_title)
            print()
            print(description)
            print()
            print('=' * 150)
            print()
            print()
        except KeyError:
            print()
            print(error + f'{count + 1}: No information provided...' + reset)
            print()
            print()

    return video_lookup


if __name__ == '__main__':
    print(youtube_search('rick and morty'))





# print(response)

# for key, value in response.items():
#      print(f'{key}: --> {value}')

# regionCode:
# pageInfo: --> results



# for key, value in video_info.items():
#     print(f'{key}: --> {value}')


# channel_id = response['items'][0]['snippet']['channelId']


# playlist_request = youtube.playlists().list(
#     part='snippet,contentDetails',
#     channelId=channel_id,
#     maxResults=1
# )

# response2 = playlist_request.execute()
# playlist_id = response2['items'][0]['id']
# print(playlist_id)

# for i in range(len(response2['items'])):

#     playlist_info = response2['items'][i]['snippet']

#     print()
#     print('-' * 100)
#     for key, value in playlist_info.items():
#         print(f'{key}: {value}')
#     print('-' * 100)
#     print()

#publishedAt:
#channelId:
#title:
#description:
#thumbnails: is dictionary with first param 'default':
#channelTitle
#liveBroadcastContent: none
#publishTime:


# playlist_item_request = youtube.playlistItems().list(
#     part='contentDetails',
#     playlistId=playlist_id
# )

# response3 = playlist_item_request.execute()

# #print(response3['items'][0])

# video_id = response3['items'][0]['contentDetails']['videoId']



# DELETE LINE - ctrl shift k

# DUPLICATE LINES - ctrl shift d

# HIDE FILE MENU - ctrl

# COMMENT OUT - ctrl /

# SELECT SAME WORD - ctrl d
# UNDO SELECTION - ctrl u
# SELECT SAME WORD ALL - alt F3

# SHOW FUNCTIONS - ctrl r
