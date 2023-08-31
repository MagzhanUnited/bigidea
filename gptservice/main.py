from app import app
from flask import request
from gpt import BotHelper
import json
import login
from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user
@app.route("/", methods=['GET'])
def hello():
    return "Hello, World!", 200

@app.route('/ask', methods=['POST'])
@jwt_required()
def ask():
    conv_id = request.args.get('conv_id')
    print("CONV_ID:", conv_id)
    data = request.data.decode('utf-8')
    data = json.loads(data)
    # access_token = data.get('access_token')
    if current_user.access_token is None:
        return "Access token is missing", 400
    question = data.get('prompt')
    if question is None:
        return "Prompt is missing", 400
    try:
        bot_instance = BotHelper(access_token=current_user.access_token, conv_id=conv_id)
        answer = bot_instance.start_chat(question)
    except Exception as e:
        print(e)
        return e.message, 429
    if conv_id is None or conv_id == '':
        conv_id = bot_instance.get_conversations(0, 1)[0]['id']
        bot_instance.conv_id = conv_id
        bot_instance.setup_title(question)
    print(answer)
    return {"answer":answer, "conv_id":conv_id}, 200

@app.route('/conversations', methods=['GET'])
@jwt_required()
def conversations():
    access_token = current_user.access_token
    if access_token is None:
        return "Access token is missing", 400
    return BotHelper(access_token=access_token).get_conversations()

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
