FROM  nvidia/cuda:9.0-base

RUN apt-get -y update && apt-get install -y --no-install-recommends \
     wget \
     python3 \
     python3-pip \
     curl \
     git \
     build-essential \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PATH="/app:${PATH}"

# # Copy the current directory contents into the container at /app
# COPY .. /app

RUN pip3 install --upgrade pip

RUN wget -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash miniconda.sh -b
RUN rm miniconda.sh
ENV PATH="/root/miniconda3/bin:${PATH}"
RUN conda update -y conda

COPY docker/requirements.txt requirements.txt
COPY docker/conda-requirements.txt conda-requirements.txt
COPY docker/Python-requirements.sh Python-requirements.sh
RUN /app/Python-requirements.sh
RUN rm -rf /root/.cache

COPY docker /app
WORKDIR /app

ENTRYPOINT ["/app/entrypoint.py"]


