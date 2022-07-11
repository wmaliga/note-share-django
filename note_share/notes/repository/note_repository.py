import boto3

from ..models import Note

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('notes')


def save(note: Note):
    table.put_item(Item={
        "id": note.id,
        "type": note.type,
        "password": note.password,
        "title": note.title,
        "expirationDate": note.expirationDate,
        "data": note.data
    })
