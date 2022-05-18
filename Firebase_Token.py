import pyrebase

class Token():
    config = {  "apiKey": "AIzaSyBTGrklWDyt2cWXL3XVgV7AvJLeQXX60iQ",            "authDomain": "smart-doorlock-c9e00.firebaseapp.com",
        "databaseURL": "https://smart-doorlock-c9e00-default-rtdb.firebaseio.com",
        "projectId": "smart-doorlock-c9e00",
        "storageBucket": "smart-doorlock-c9e00.appspot.com",
        "messagingSenderId": "404335392148",
        "appId": "1:404335392148:web:75c6d6f8572fea4dbf4b81",
        "measurementId": "G-7TB1L2YDF4",
        "serviceAccount": "smart-doorlock-c9e00-firebase-adminsdk-qge67-165a3f65b6.json"}


    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    storage = firebase.storage()
