import boto3
from operator import itemgetter

ecr_client = boto3.client('ecr')
described_repos = ecr_client.describe_repositories()

#name of the repo we want
specified_repo_name = 'java-mysql-app'

for repo in described_repos['repositories']:
    print(repo['repositoryName'])
    if repo['repositoryName'] == specified_repo_name:

        described_images = ecr_client.describe_images(repositoryName=repo['repositoryName'],)
        sorted_images = sorted(described_images['imageDetails'], key=itemgetter('imagePushedAt'), reverse=True)

        for image in sorted_images[:3]:
            try:
               print(f'image {image["repositoryName"]}:{image["imageTags"][0]} pushed at {image["imagePushedAt"]}')
            except:
                print(f'image {image["repositoryName"]} has a tag error')
