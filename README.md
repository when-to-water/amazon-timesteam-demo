# amazon-timestream-demo
Repo for testing the connection to AWS Timestream using a predefinied demo database by AWS.
Code is based on [this tutorial by aws-dojo.com](https://aws-dojo.com/excercises/excercise24/).
## Prerequisites
- Demo Database created
- AWS User with access to AWS Timestream (e.g. with the AWS managed "AmazonTimestreamFullAccess" policy)
- AWS CLI [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

## Installation

```Shell
pipenv install
```

## Run

```Shell
pipenv shell
python main.py
```

## See also
[AWS Sample App](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/sample_apps/python)

[AWS Timesteam Tutorial](https://www.youtube.com/watch?v=39ijv_pfWSQ&feature=emb_logo)
