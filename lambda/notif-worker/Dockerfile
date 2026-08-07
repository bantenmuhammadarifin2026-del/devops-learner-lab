FROM public.ecr.aws/lambda/python:3.11

# Copy requirements dan install (jika ada)
COPY app.py ${LAMBDA_TASK_ROOT}

# Set command handler
CMD [ "app.handler" ]
