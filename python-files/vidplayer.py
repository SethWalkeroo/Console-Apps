from vlc import MediaPlayer
from pafy import new
from colored import fg, bg, attr
from time import sleep, perf_counter
from welcome import title_card, loading_animation
from os import system, rename, remove
from youtube import youtube_search


movie_ptrn = ['*', '^', '-', '=']
highlight = bg('pale_green_1a')
txt_color = fg(16)
success = fg('green')
delete = fg('red_3a')
reset = attr('reset')

def video_player_main():
    welcome_message = 'WELCOME TO THE VIDEO PLAYER!'
    title_card(welcome_message)

    local = False

    while True:
        command = input('Would you like to search for a video, enter a link, or play one locally? (search/link/local/exit): ')
        loading_animation(time=1)
        if command == 'link':
            link = input('Enter the video link: ')
            video_name = link[31:]

        elif command == 'search':

            new_search = ''
            while new_search != 'no':
                keyword = input('What would you like to search?: ')
                loading_animation('Generating results...', time=1)
                search_start = perf_counter()
                
                videos = youtube_search(keyword)

                search_finish = perf_counter()
                print()
                print(f'Finished in {round(search_finish - search_start, 2)} second(s)')
                print()
                new_search = input('Would you like to search something else? (yes/no): ')
                if new_search == 'yes':
                    loading_animation(time=1)
                print()

            video_name = int(input('Which video would you like to watch? (enter the number): '))
            loading_animation('starting media player...', time=1)
            video_choice = videos[video_name - 1]
            link = f'https://www.youtube.com/watch?v={video_choice}'
            print()
        elif command == 'local':
            local = True
            video_name = input('What is the name of the video?: ')
            loading_animation('starting media...', time=1)
        elif command == 'exit':
            break
        else:
            system('clear')
            print('ERROR: either enter "search", "link", "local", or "exit"')
            print()
        

        if not local:
            video = new(link)
            best = video.getbest()
            media = MediaPlayer(best.url)
        else:
            video_path = f'../videos/{video_name}'
            media = MediaPlayer(video_path)

        while True:
            playback_choice = input('type "play", "pause", or "stop": ')
            if playback_choice.lower() == "play":
                media.play()
                loading_animation('playing... ', time=2)
            elif playback_choice.lower() == "pause":
                media.pause()
                loading_animation('paused... ', time=1)
            elif playback_choice.lower() == "stop":
                media.stop()
                loading_animation('stopping... ', time=1)
                break
            else:
                loading_animation('please enter a valid command... ', time=2)
        
        system('clear')
        if not local:
            keep = input('Would you like to download that video? (yes/no): ')
            loading_animation(time=1)
            if keep == 'yes':
                video_path = f'../videos/{video_name}'
                # gets the best quality for the download
                best.download(filepath=video_path, quiet=False)
                loading_animation(time=1)
                new_name = input('What would you like to name this video?: ')
                print()
                rename(f'../videos/{video_name}', f'../videos/{new_name}')
                video_path = f'../videos/{new_name}'
                print(success + f'File "{new_name}" has been successfully saved at {video_path}' + reset)
                sleep(2)
                loading_animation(time=1)
            else:
                loading_animation(time=1)

    exit_message = 'LEAVING THE VIDEO PLAYER!'
    title_card(exit_message)
    sleep(1.5)
    loading_animation('goodbye!', time=1)


if __name__ == '__main__':
    video_player_main()
