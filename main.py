from flask import Flask, request, jsonify
from pydantic import BaseModel
import spacy
app = Flask(__name__)

class InputData(BaseModel):
    heading: str
    description: str

class OutputData(BaseModel):
    tags: list

@app.route('/generate_tags', methods=['POST'])
def generate_tags():
    try:
        # Get JSON data from the request
        json_data = request.get_json()
        # Validate JSON against the Pydantic model
        # input_data = InputData(**json_data)
        # print(input_data)
        # load_model()
        # result = predict()
        # Process the data and create the result
        new_text1 = json_data['heading']
        new_text2 = json_data['description']
        # Combine both text fields
        combined_text = new_text1 + ' ' + new_text2

        # Make predictions using the fine-tuned model
        doc = nlp_fine_tuned(combined_text)

        # Print entities found in the text
        tags =[]
        for ent in doc.ents:
            if ent.label_ == 'tech_stack':
                tags.append(ent.text)
            print(f"Entity: {ent.text}, Label: {ent.label_}, Start: {ent.start_char}, End: {ent.end_char}")
        tuned_model = spacy.load('tuned_spacy_ner')
        # result = {"tags": tags}
        result = {"tags": ["bla", "foo"]}
        # Validate the result against the output model
        output_data = OutputData(**result)
        # Return the result as JSON
        return jsonify(result)
    except Exception as e:
        # Handle validation errors or other exceptions
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)