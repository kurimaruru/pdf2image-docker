FROM public.ecr.aws/lambda/python:3.9

RUN yum -y install poppler-utils 
#     yum -y install ghostscript && \
#     yum -y install tesseract-ocr-jpn* && \
#     yum -y install jbig2enc 
#     # yum -y install pngguant && \
#     # yum -y install unpaper

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip3 install -r requirements.txt --target ${LAMBDA_TASK_ROOT}

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}  
COPY dummy.pdf ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]