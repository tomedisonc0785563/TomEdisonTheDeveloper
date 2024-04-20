import boto3

# Initialize the AWS services clients
s3 = boto3.client('s3')
textract = boto3.client('textract')
dynamodb = boto3.resource('dynamodb')

# Specify your S3 bucket and file name
bucket_name = "data-extract-paperless-logistics"
file_name = "commercial-invoice-template test sample.png"

# DynamoDB table to store extracted text
table_name = "data-extract-paperless-logistics-data"
table = dynamodb.Table(table_name)

def extract_text_from_s3_document():
    # Using AWS Textract to extract text from the document stored in S3
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': file_name
            }
        }
    )

    # Extracted text
    extracted_text = ""

    # Iterate over the detected items to collect extracted text
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print(item["Text"] + "\n")
            extracted_text += item["Text"] + "\n"

    # Storing extracted text in DynamoDB
    table.put_item(
        Item={
            'document_name': file_name,
            'extracted_text': extracted_text
        }
    )

    print(f"Successfully extracted and stored text for {file_name}")

# Execute the function
if __name__ == "__main__":
    extract_text_from_s3_document()
