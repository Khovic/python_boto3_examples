import boto3

iam_client = boto3.client('iam')

for i in range(0, len(iam_client.list_users()['Users'])):
    user_name = iam_client.list_users()['Users'][i]['UserName']
    print(user_name)
    try:
        user_last_logged = iam_client.list_users()['Users'][i]['PasswordLastUsed']
        print(user_last_logged)
    except:
        print("error, user never logged?")
