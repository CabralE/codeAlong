
# Docker
- from the root directory run `docker-compose build`
- then to run the application `docker-compose up -d`
- if you make a change that required rebuilding the container i.e. adding a python library to requirements.txt:
  - `docker-compose down`
  - `docker-compose build`
  - `docker-compose up -d`
- if you run into permission issues when trying to run docker-compose build, delete the /data directory (`rm -rf data/`), you may need to use sudo `sudo rm -rf data/`
