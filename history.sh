ssh ssh-keygen -t ed25519 -C "shivam.pant@hcltech.com"
ssh-keygen -t ed25519 -C "shivam.pant@hcltech.com"
cat /home/azureuser/.ssh/id_ed25519.pub
clear
sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc podman-docker containerd runc | cut -f1)
 # Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl status docker
clear
   27  cat /home/azureuser/.ssh/id_ed25519.pub
   28  git clone git@github.com:Shiazy18/azure-advisor.git
   29  clear
   30  ls
   31  cd azure-advisor/
   32  ls
   33  cat README.md 
   34  clear
   35  vi README.md 
   36  git add .
   37  git commit -m "chekcing if ssh in vm is wokring"
   38  git push
   39  git branch 
   40  git branch checkout docker
   41  git pull
   42  git branch checkout docker
   43  git branch  docker
   44  git branch
   45  git branch docker
   46  git switch docker
   47  cleaer
   48  clear
   49  vi .env
   50  cat .env
   51  clear
   52  docker pull
   53  clear
   54  git pull
   55  ls
   56  git branch
   57  ls
   58  git fetch
   59  ls
   60  git branches
   61  git branch
   62  clear
   63  ls
   64  git pull
   65  clear
   66  ls
   67  docker build -t azure-advisor .
   68  sudo groupadd docker
   69  sudo usermod -aG docker $USER
   70  clear
   71  docker build -t azure-advisor .
   72  sudo usermod -aG docker $USER
   73  clear
   74  sudo docker build -t azure-advisor .
   75  docker ps
   76  sudo docker ps
   77  sudo docker images
   78  sudo docker run -p 8501:8501 --env-file .env azure-advisor
   79  cd azure-advisor/
   80  cat .env 
   81  vi .env
   82  rm -f .env
   83  ls
   84  vi .env
   85  cat .env 
   86  clear
   87  sudo docker run -p 8501:8501 --env-file .env azure-advisor
   88  clear
   89  docker login azureadvisor.azurecr.io
   90  docker images
   91  docker tag azure-advisor azureadvisor.azurecr.io/azure-advisor
   92  docker images
   93  docker rm 098c40d5cdc5
   94  docker rmi 098c40d5cdc5
   95  docker rmi -f 098c40d5cdc5
   96  docker images
   97  cls
   98  clear
   99  docker build -t azureadvisor.azurecr.io/azure-advisor .
  100  docker images
  101  docker run -it -p 8501:8501 azureadvisor.azurecr.io/azure-advisor
  102  docker run -it -d -p 8501:8501 azureadvisor.azurecr.io/azure-advisor
  103  clear
  104  docker push azureadvisor.azurecr.io/azure-advisor
  105  helm create azure-advisor-helm
  106  curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-4
  107  chmod 700 get_helm.sh
  108  ./get_helm.sh
  109  clear
  110  helm create azure-advisor-helm
  111  ls
  112  cd azure-advisor-helm/
  113  ls
  114  cd templates/
  115  cd ..
  116  ls
  117  git push
  118  git add .
  119  git commit -m "added helm chart"
  120  git push
  121  ls
  122  cd azure-advisor/
  123  ls
  124  git pull
  125  cls
  126  clear
  127  ls
  128  git branch
  129  git pull
  130  git fetch
  131  ls
  132  cd azure-advisor-helm/
  133  ls
  134  docker run -it -d -p 8501:8501 azureadvisor.azurecr.io/azure-advisor
  135  docker rm -f azure-advisor
  136  docker ps
  137  docker rm -f dc88933c9661
  138  docker images
  139  clear
  140  ls
  141  cd ..
  142  ls
  143  cat .env 
  144  vi .env
  145  clear
  146  vi gpt.py 
  147  docker images
  148  docker build -t azureadvisor.azurecr.io/azure-advisor .
  149  docker images
  150  docker run -it -d -p 8501:8501 azureadvisor.azurecr.io/azure-advisor
  151  docker push azureadvisor.azurecr.io/azure-advisor
  152  docker build -t azureadvisor.azurecr.io/azure-advisor:v1.0.0 .
  153  docker push azureadvisor.azurecr.io/azure-advisor:v1.0.0

