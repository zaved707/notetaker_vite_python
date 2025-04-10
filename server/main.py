import files,os
from flask import Flask, jsonify,request

app = Flask(__name__)
route=os.path.join(os.getcwd(),'notes')
if not os.path.exists(route):
    os.makedirs(route)
@app.route('/api/items', methods=['GET'])
def get_items():
    filesList=files.list_files_only(route)
    items = ['item1', 'item2']
    return jsonify({"items": filesList})

@app.route('/api/fetchFile')
def add_item():
    filename = request.args.get('filename')  # Get the filename from the URL
    if not filename:
        return jsonify({"error": "Please send a filename"}), 400
    # Add it to our list
    filePath=os.path.join(route,filename)
    fileContent=files.read_file_content(filePath)
    return jsonify({"message": f"{fileContent}"})
@app.route('/api/saveFile')
def save_file():
    fileContent = request.args.get('fileContent')  # Get the filename from the URL
    fileName=request.args.get('fileName')
    if not fileContent:
        return jsonify({"error": "Please send a filecontent"}), 400
    # Add it to our list
    files.saveFile(fileContent, os.path.join(route,fileName))
    return jsonify('True')                              #TODO: not very tidy



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

