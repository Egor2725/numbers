# numbers
sudo docker-compose up
sudo docker-compose run web migrate
sudo docker-compose run web createsuperuser

# tests
sudo dockercompose run web pytest

