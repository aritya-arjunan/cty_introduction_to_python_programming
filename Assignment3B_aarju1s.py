# There were 110 cookies and there were twice as many kids as the cookies.
# The kids were equally distributed into 4 groups.
# How many kids are there in each group?
cookies = 110
kids = cookies * 2
groups = 4
kids_in_each_group = kids / groups
print(kids_in_each_group)



# There were 72859 kids and thrice as many kids as cookies.
# THere were also 72 bottles which contain cookies that are equally distributed into the bottles.
# How many cookies in each bottle?
kids = 72792
cookies = kids / 3
bottles = 72
number_of_cookies_in_each_bottle = cookies / bottles
print(number_of_cookies_in_each_bottle)



# Mathew wants to put 7 snowflake stickers on each of his 19 story books.
# If the snowflake stickers are sold in packs of 8.
# What is the minimum number of packs of stickers he must buy?
stickers = 7
story_books = 19
stickers_in_each_pack = 8
stickers_required = stickers * story_books
import math
packs_required = math.ceil(stickers_required / stickers_in_each_pack)
print(packs_required)
