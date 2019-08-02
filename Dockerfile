FROM  nvidia/cuda:9.0-base

RUN apt-get -y update && apt-get install -y \
     wget \
     python3 \
     python3-pip \
     curl \
     git \
     build-essential \
     python-setuptools

COPY . /FuseNet
WORKDIR /FuseNet
ENV PATH="/FuseNet:${PATH}"

RUN pip3 install --upgrade pip

#RUN wget -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
#RUN bash miniconda.sh -b
#RUN rm miniconda.sh
#ENV PATH="/root/miniconda3/bin:${PATH}"
#RUN conda update -y conda

WORKDIR /FuseNet/FuseNet_PyTorch
RUN pip install -r requirements.txt
#RUN python3 fusenet_train.py --dataroot ./FuseNet_PyTorch/datasets/nyu_class_10_db.h5 --#batch_size 8 --lr 0.005"

ENTRYPOINT ["/FuseNet/entrypoint.py"]


