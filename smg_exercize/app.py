from flask import Flask, request
from flask_restx import Resource, Api, fields
from lib.dataencryption.DataEncryptor import DataEncryptor
from lib.storage.FakeStorageManager import FakeStorageManager
from lib.cipher.Rot13Cipher import Rot13Cipher


app = Flask(__name__)

api = Api()
api.init_app(
    app,
    title = 'SMG GM Data Team - Data Engineer Python API Exercise',
    description = 'This is a simple REST API containing two endpoints. This API allows you to get a sentence with the encrypted version of it (with rot13), but also add new sentences in the existing store.',
    version = '1.0.0',
    validate=False
)

data_encryptor = DataEncryptor(
        storage_manager = FakeStorageManager(),
        cipher = Rot13Cipher()
    )

# TODO: trigger 400 error message
@api.route('/sentences/<int:sentenceId>')
class SentenceReader(Resource):
    @api.doc(
            params={'sentenceId': 'ID of sentence to return'},
            summary = 'Get a sentence and its encrypted version',
            description = 'Get a sentence by Id and the rot13 encryption of it',
            responses={
                200: 'successful operation',
                400: 'Invalid ID supplied',
                404: 'Sentence not found'
            }
    )
    def get(self,sentenceId):
        if not isinstance(sentenceId, int):
            return 400, 'Invalid ID supplied'
        res = data_encryptor.read_sentence(sentence_id = sentenceId)
        if not res:
            return 404, 'Sentence not found'
        return res






post_request = api.model('post_request', {
    'id': fields.Integer(required=True, example=10),
    'text': fields.String(required=True, example='super movie title', description='text contained in the sentence')
})


@api.route('/sentences/')
class SentenceWriter(Resource):

    @api.doc(
            summary = 'Add a new sentence to the store',
            description = 'Create a new sentence in the store and return it with its encrypted version',
            responses={
                200: 'successful operation',
                405: 'Invalid input'
            }
    )
    @api.expect(post_request)
    def post(self):
        result = data_encryptor.write_sentence(sentence_id = api.payload['id'], sentence = api.payload['text'])
        if not result:
            return 405, 'Invalid input'
        return result


if __name__ == "__main__":
    app.run(debug=True)