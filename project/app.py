from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# AWS Config
s3_client = boto3.client('s3')
athena_client = boto3.client('athena', region_name='eu-central-1')
sns_client = boto3.client('sns')

# Bucket ve Athena ayarları
S3_BUCKET = 'deprem-verileri-new-bucket'
ATHENA_OUTPUT = 's3://bucket-adiniz/athena-output/'
TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:DepremBildirim'

@app.route('/query', methods=['GET'])
def query_data():
    region = request.args.get('region')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    query = f"""
        SELECT * FROM deprem_verisi
        WHERE bolge = '{region}' 
        AND zaman BETWEEN '{start_time}' AND '{end_time}'
    """

    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': 'depremler'},
        ResultConfiguration={'OutputLocation': ATHENA_OUTPUT}
    )

    query_id = response['QueryExecutionId']
    result = athena_client.get_query_results(QueryExecutionId=query_id)
    return jsonify(result)

@app.route('/notify', methods=['POST'])
def send_notification():
    data = request.json
    magnitude = data.get('magnitude')
    region = data.get('region')
    phone_number = data.get('phone_number')

    if magnitude >= 4.0:  # Eşik değer
        message = f"{region} bölgesinde {magnitude} büyüklüğünde deprem oldu!"
        sns_client.publish(PhoneNumber=phone_number, Message=message)

    return jsonify({'status': 'Notification sent'})

if __name__ == '__main__':
    app.run(debug=True)
