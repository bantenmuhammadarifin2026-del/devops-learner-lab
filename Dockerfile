FROM public.ecr.aws/lambda/python:3.11
COPY lambda/notif-worker/app.py ${LAMBDA_TASK_ROOT}
CMD [ "app.handler" ]
