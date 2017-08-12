# -*- coding: utf-8 -*-

import pymongo

def get_db():
    from pymongo import MongoClient
    client = MongoClient('192.168.2.207:30000')
    db = client.get_database("near")
    return db


mongodb = get_db()

imgs = mongodb.imgs



def insert(pin):
    db = get_db()
    db.imgs.insert({"pin": str(pin)})


def get_img(pin):
    return mongodb.imgs.find_one({"pin": pin})


def find():
    return mongodb.imgs.find()


def findstr(str):
    return mongodb.imgs.find(str)