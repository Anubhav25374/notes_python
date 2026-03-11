import json


def load_data():
    try:
        #file = open("example.txt", "r")
        #content = file.read()
        #print(content)
        #file.close()                                 <----OR---->
        with open ('Youtube.txt', 'r') as file:
            test =  json.load(file)
            return test
    except FileNotFoundError:
        return []    

def save_data_helper(Videos):
    with open ('Youtube.txt', "w") as file:
        json.dump(Videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 100)
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ") 

    print("\n")
    print("*" * 100)       

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name":name, "time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter number of video you want to update! "))
    if 1 <= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video duration: ")
        videos[index-1] = {'name': name, 'time':time}
        save_data_helper(videos)
    else:
        print("Error: This index does not exits!! ")    

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter number of video you want to delete ! "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Error: This index does not exits!!")    

def main():
    videos = load_data()
    while True:
        print("\n Youtube manager App")
        print("1. show videos list")
        print("2. add videos list")
        print("3. update videos list")
        print("4. delete videos list")
        print("5.  Exit app")

        choice = input("\n Plz enter your choice: ")
        

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos) 
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalide Input!")           
        

if __name__ == "__main__":
    main()