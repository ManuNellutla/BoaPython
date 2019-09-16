# Pymongo driver to access mongodb
from pymongo import MongoClient
client = MongoClient()

# installed mongodb and connecting on local 27017
client = MongoClient('mongodb://localhost:27017')

#creating Test DB
db = client['pymongo_test']

# creating collection called posts
posts = db.posts
"""""
# JSON post data

post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}

#single insert into db
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))


post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

#multi insert into DB
new_result = posts.insert_many([post_1, post_2, post_3])
print('Multiple posts: {0}'.format(new_result.inserted_ids))
"""
bills_post = posts.find_one({'author': 'Bill'})
print(bills_post)