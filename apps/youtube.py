from googleapiclient.discovery import build
from colored import bg, attr, fg


highlight = bg(16) + fg('white')
reset = attr('reset')
border_color = fg('pale_green_1a')
error = fg('red_3a')

def youtube_search(keyword, total_results=25, managed=True):

    if managed:
        with open('data/api-key.txt', 'r') as api_file:
            api_key = api_file.read()
    else:
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
    print(youtube_search('rick and morty', managed=False))


