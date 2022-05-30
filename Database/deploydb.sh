dnf update -y
dnf install -y epel-release
dnf update -y
dnf install -y podman-compose
mkdir mysql
cd mysql
echo "services:
  db:
    image: mysql:latest
    restart: always
    environment:
      MYSQL_DATABASE: 'progexdb'
      # So you don't have to use root, but you can if you like
      MYSQL_USER: 'programuser'
      # You can use whatever password you like
      MYSQL_PASSWORD: 'b#oGkx*vnp78P8us'
      # Password for root access
      MYSQL_ROOT_PASSWORD: 'b#oGkx*vnp78P8us'
    ports:
      # <Port exposed> : < MySQL Port running inside container>
      - '3306:3306'
    expose:
      # Opens port 3306 on the container
      - '3306'
      # Where our data will be persisted
    volumes:
      - my-db:/var/lib/mysql
# Names our volume
volumes:
  my-db:./" >> docker-compose.yml
  docker compose up -d

  
  