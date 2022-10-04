from flask import Blueprint, request, jsonify, url_for, render_template
from api.validation import validate_inputs
from api.config import get_logger
import pickle

_logger = get_logger(logger_name=__name__)
## Load the model
#regmodel = pickle.load(open('regmodel.pkl','rb'))
#scalar = pickle.load(open('scaling.pkl','rb'))

prediction_app = Blueprint('prediction_app', __name__)
TEST = 'test'


@prediction_app.route("/", methods=['GET', 'POST'])
def home():
    _logger.info('Home page')
    return render_template('home.html')


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'health status OK'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': TEST,
                        'api_version': TEST})


@prediction_app.route('/predict_api', methods=['POST'])
def predict_api():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        return jsonify(
            {'predictions': json_data,
            'version': TEST,
            'errors': TEST})


@prediction_app.route('/predict', methods=['POST'])
def predict():
    # Step 1: Extract POST data from request body as JSON
    json_data = request.get_json()
    _logger.info(f'Inputs: {json_data}')
    print('Call Endpoint', json_data)
    # Step 2: Validate the input using marshmallow schema
    #input_data, errors = validate_inputs(input_data=json_data)

    # DATA TRANSFORMATION - load trasnformers

    # Step 3: Model prediction
    # NOT NEEDED MAYBE  print(np.array(list(json_data.values())).reshape(1,-1))
    #result = make_prediction(input_data=input_data)
    #_logger.debug(f'Outputs: {result}')

    # Step 4: Convert numpy ndarray to list
    #predictions = result.get('predictions').tolist()
    #version = result.get('version')

    # Step 5: Return the response as JSON
    #return jsonify({'predictions': json_data,
    #                'version': TEST,
    #                'errors': TEST})
    return json_data
        

