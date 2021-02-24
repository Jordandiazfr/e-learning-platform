# container api 
docker stop apiflask
docker rm apiflask
docker run -itd --name apiflask --mount type=bind,src=${PWD}/api,dst=/api -w //api -p 5000:5000 python
docker exec -it apiflask python -m pip install -r requirements.txt
docker exec -it apiflask python app.py
