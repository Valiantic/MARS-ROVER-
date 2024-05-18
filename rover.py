# import requests, os, webbrowser

# api_key = 'Pa41EKygcE2L3n3DImI43fXEc445gGyKqwYQO2k4'
# api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'

# def get_rover_data():
#     r = requests.get(api_url + '?api_key=' + api_key)
#     data = r.json()
#     return data

# def get_photos(rover, sol, camera):
#     sol_pic = False
#     retry_count = 0
#     while not sol_pic:
#         r = requests.get(api_url + rover + '/photos?sol=' + str(sol) + '&camera=' + camera + '&api_key=' + api_key)
#         if r.status_code != 200:
#             print(f"Error {r.status_code} while fetching photos for rover {rover} on Sol {sol} with camera {camera}")
#             return []
#         data = r.json()
        
#         if data['photos'] or retry_count > 2:
#             sol_pic = True
#         else:
#             sol -= 1
#             retry_count += 1
#     return data['photos']

# def download_and_open_photos(camera_data, camera_name, path):
#     img_data = requests.get(camera_data[len(camera_data) - 1]['img_src']).content
#     with open(path + camera_name + '.jpg', 'wb') as handler:
#         handler.write(img_data)
#     webbrowser.open('file://' + os.path.realpath(path + camera_name + '.jpg'))

# def main():
#     rover_data = get_rover_data()
#     path = 'frontend/images/'
#     if not os.path.exists(path):
#         os.makedirs(path)
    
#     for rover in rover_data['rovers']:
#         path = 'frontend/images/' + rover['name'] + '/'
#         if not os.path.exists(path):
#             os.makedirs(path)

#         if (rover['status'] == 'complete'):
#             print(f"Skipping rover {rover['name']} (rover status: {rover['status']})")
#             continue
#         print(f"Scraping rover {rover['name']}, starting with Sol {rover['max_sol']} (rover status: {rover['status']})")
#         for camera in rover['cameras']:
#             print(f"Scraping camera {rover['name']}@{camera['name']} ({camera['full_name']})")
#             camera_data = get_photos(rover['name'], rover['max_sol'], camera['name'])
#             if not camera_data:
#                 continue
#             download_and_open_photos(camera_data, camera['name'], path)

# if __name__ == '__main__':
#     main()


# import requests, os, webbrowser

# api_key = 'Pa41EKygcE2L3n3DImI43fXEc445gGyKqwYQO2k4'
# api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/'

# def get_rover_data():
#     r = requests.get(api_url + '?api_key=' + api_key)
#     data = r.json()
#     return data

# def get_photos(rover, sol, camera):
#     sol_pic = False
#     retry_count = 0
#     while not sol_pic:
#         r = requests.get(api_url + rover + '/photos?sol=' + str(sol) + '&camera=' + camera + '&api_key=' + api_key)
#         if r.status_code != 200:
#             print(f"Error {r.status_code} while fetching photos for rover {rover} on Sol {sol} with camera {camera}")
#             return []
#         data = r.json()
        
#         if data['photos'] or retry_count > 2:
#             sol_pic = True
#         else:
#             sol -= 1
#             retry_count += 1
#     return data['photos']

# def describe_photo(camera_name):
#     # This is a very basic example. In a real-world application, you would use a machine learning model here.
#     return f"This photo was taken by the {camera_name} camera."

# def download_and_open_photos(camera_data, camera_name, path):
#     img_data = requests.get(camera_data[len(camera_data) - 1]['img_src']).content
#     with open(path + camera_name + '.jpg', 'wb') as handler:
#         handler.write(img_data)
#     print(describe_photo(camera_name))
#     webbrowser.open('file://' + os.path.realpath(path + camera_name + '.jpg'))

# def main():
#     rover_data = get_rover_data()
#     path = 'frontend/images/'
#     if not os.path.exists(path):
#         os.makedirs(path)
    
#     for rover in rover_data['rovers']:
#         path = 'frontend/images/' + rover['name'] + '/'
#         if not os.path.exists(path):
#             os.makedirs(path)

#         if (rover['status'] == 'complete'):
#             print(f"Skipping rover {rover['name']} (rover status: {rover['status']})")
#             continue
#         print(f"Scraping rover {rover['name']}, starting with Sol {rover['max_sol']} (rover status: {rover['status']})")
#         for camera in rover['cameras']:
#             print(f"Scraping camera {rover['name']}@{camera['name']} ({camera['full_name']})")
#             camera_data = get_photos(rover['name'], rover['max_sol'], camera['name'])
#             if not camera_data:
#                 continue
#             download_and_open_photos(camera_data, camera['name'], path)

# if __name__ == '__main__':
#     main()



import requests
import random
import webbrowser

api_key = 'Pa41EKygcE2L3n3DImI43fXEc445gGyKqwYQO2k4'
api_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def get_random_photo():
    params = {
        'api_key': api_key,
        'sol': random.randint(0, 1000),  # choose a random Martian sol between 0 and 1000
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # ensure we got a successful response
    photos = response.json()['photos']

    if not photos:
        print("No photos found for the chosen Martian sol. Try again.")
        return None

    photo = random.choice(photos)  # choose a random photo
    return photo

def main():
    photo = get_random_photo()
    if photo is not None:
        print(f"Displaying a random photo taken by the {photo['rover']['name']} rover on Martian sol {photo['sol']} using the {photo['camera']['full_name']} ({photo['camera']['name']}).")
        webbrowser.open(photo['img_src'])

if __name__ == '__main__':
    main()
