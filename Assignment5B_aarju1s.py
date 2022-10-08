#Function that calculates how many gigabytes in total storage.
def storage_calculator(apps, photos, songs, movies):
    mb_apps = apps * 256
    mb_photos = photos * 2
    mb_songs = songs * 4
    mb_movies = movies * 1500
    mb_total = mb_apps + mb_photos + mb_songs + mb_movies
    gb_total = mb_total/1000
    return gb_total

#Main code
#Variables that define Jemma
jemma_apps = 12
jemma_photos = 65
jemma_songs = 11
jemma_movies = 2
storage = storage_calculator(jemma_apps, jemma_photos, jemma_songs, jemma_movies)
print("Jemma has %s gigabytes in total storage" %str(storage))

#Variables that define Sonny
sonny_apps = 7
sonny_photos = 125
sonny_songs = 21
sonny_movies = 3
storage = storage_calculator(sonny_apps, sonny_photos, sonny_songs, sonny_movies)
print("Sonny has %s gigabytes in total storage" %str(storage))

#Variables that define user input
question = "How many %s do you have in your device?\n"
input_apps = int(input(question %"apps"))
input_photos = int(input(question %"photos"))
input_songs = int(input(question %"songs"))
input_movies = int(input(question %"movies"))
storage = storage_calculator(input_apps, input_photos, input_songs, input_movies)
print("You have %s gigabytes in total storage" %str(storage))

      
