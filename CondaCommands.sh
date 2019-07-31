conda create --name fusenet python=3.6
conda activate fusenet
conda install -c anaconda cudatoolkit
conda install -c anaconda cudnn
mkdir fusenet && cd fusenet
git clone https://github.com/zanilzanzan/FuseNet_PyTorch.git
cd FuseNet_PyTorch
pip install -r requirements.txt
mkdir datasets && cd datasets
wget https://vision.in.tum.de/webarchive/hazirbas/fusenet-pytorch/nyu/nyu_class_10_db.h5
cd ..
python fusenet_train.py --dataroot ./datasets/nyu_class_10_db.h5 --batch_size 8 --lr 0.005
