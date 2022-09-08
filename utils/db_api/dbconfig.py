import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from data.config import dp_api

cred = credentials.Certificate(dp_api)
firebase_admin.initialize_app(cred)

db = firestore.client()


async def add_statistics():
    statistics = db.collection(u'statistics').document(u"launches")
    launches = statistics.get().to_dict()['number_of_launches']
    launches += 1;
    statistics.set({
        u'number_of_launches': launches,
    })


async def chek(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        name = user_name.to_dict()['name']
    except:
        name = 'No name'
    return name != "No name"


async def get_name(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        name = user_name.to_dict()['name']
    except:
        name = 'No name'
    return name


async def get(collection, document, field):
    bot_ref = db.collection(str(collection)).document(str(document))
    data = bot_ref.get()
    try:
        current_field = data.to_dict()[str(field)]
    except:
        current_field = '🚫'
    return current_field


async def get_field(collection, document, field, field_name):
    bot_ref = db.collection(str(collection)).document(str(document))
    data = bot_ref.get()
    try:
        current_field = data.to_dict()[str(field)][str(field_name)]
    except:
        current_field = '🚫'
    return current_field

async def get_button(bot_id, button_number):
    bot_ref = db.collection('bots').document(bot_id)
    data = bot_ref.get()
    try:
        current_field = data.to_dict()[f"button{button_number}"]["about"]
    except:
        current_field = '🚫'
    return current_field

async def get_main(bot_id):
    bot_ref = db.collection('bots').document(bot_id)
    data = bot_ref.get()
    try:
        current_field = data.to_dict()[f"main"]
    except:
        current_field = '🚫'
    return current_field

async def get_button_ref(bot_id, button_number):
    bot_ref = db.collection('bots').document(bot_id)
    data = bot_ref.get()
    try:
        current_field = data.to_dict()[f"button{button_number}"]["ref"]
    except:
        current_field = '🚫'
    return current_field


async def get_bot_id(user_id):
    bot_ref = db.collection("users").document(str(user_id))
    data = bot_ref.get()
    try:
        current_field = data.to_dict()['bots']['id']
    except:
        current_field = 'No data'
    return current_field


async def get_phone(user_id):
    user = str(user_id)
    users_ref = db.collection(u'users').document(user)
    user_name = users_ref.get()
    try:
        phone = user_name.to_dict()['user']['phone']
    except:
        phone = '🚫'
    return phone


async def create_users_for_db(id, username, phone, bot_id, bot_name, bot_token):
    doc_ref = db.collection(u'users').document(str(id))
    doc_ref.set({
        u'bots': {'id': str(bot_id), 'bot_name': str(bot_name), 'bot_token': str(bot_token)},
        u'user': {'name': str(username), 'phone': str(phone)},
    })


async def get_all_users():
    docs = db.collection(u'users').stream()
    all_users = []

    for user in docs:
        all_users.append(user.id)
    return all_users


async def chek_user(user_id):
    docs = db.collection(u'users').stream()
    flag = True

    for user in docs:
        if user.id == str(user_id):
            flag = False
            break
    return flag


async def get_all_bots():
    users_ref = db.collection('users')
    docs = users_ref.stream()
    all_bots = []
    for doc in docs:
        bots = u'{}'.format(doc.to_dict()['bots']['id'])
        all_bots.append(bots)
    return all_bots


async def edit_bot(bot_id, main_text, b1_d, b1_r, b2_d, b2_r, b3_d, b3_r, b4_d, b4_r, b5_d, b5_r):
    doc_ref = db.collection(u'bots').document(str(bot_id))
    doc_ref.set({
        u'main': main_text,
        u'button1': {'about': b1_d, 'ref': b1_r},
        u'button2': {'about': b2_d, 'ref': b2_r},
        u'button3': {'about': b3_d, 'ref': b3_r},
        u'button4': {'about': b4_d, 'ref': b4_r},
        u'button5': {'about': b5_d, 'ref': b5_r},
    })



async def delete_bot(bot_id):
    db.collection(u'bots').document(bot_id).delete()