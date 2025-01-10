from flask import Blueprint, render_template, jsonify
import boto3

main = Blueprint('main', __name__)

# AWS Athena'dan veri çekme
@main.route('/api/athena_data')
def get_athena_data():
    client = boto3.client('athena', region_name='eu-north-1')
    query = "SELECT date, latitude, longitude, magnitude, location FROM deprem_afad LIMIT 10;"
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={'Database': 'direct_db'},
        ResultConfiguration={'OutputLocation': 's3://deprem-verileri-new-bucket/results/'}
    )
    query_id = response['QueryExecutionId']
    result = client.get_query_results(QueryExecutionId=query_id)
    rows = result['ResultSet']['Rows']
    data = [dict(zip([col['VarCharValue'] for col in rows[0]['Data']], [col.get('VarCharValue') for col in row['Data']])) for row in rows[1:]]
    return jsonify(data)

# S3'teki dosyaları listeleme
@main.route('/api/s3_files')
def list_s3_files():
    s3_client = boto3.client('s3', region_name='eu-north-1')
    response = s3_client.list_objects_v2(Bucket='deprem-verileri-new-bucket')
    files = [obj['Key'] for obj in response.get('Contents', [])]
    return jsonify(files)

# Lambda loglarını alma
@main.route('/api/lambda_status')
def get_lambda_logs():
    cloudwatch_client = boto3.client('logs', region_name='eu-north-1')
    response = cloudwatch_client.filter_log_events(
        logGroupName='/aws/lambda/aks_demo_lambda',
        limit=10
    )
    logs = [event['message'] for event in response['events']]
    return jsonify(logs)

# Ana sayfa
@main.route('/')
def home():
    return render_template('index.html')
