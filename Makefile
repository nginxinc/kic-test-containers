

build-docker-tcp:
	docker build -t tcp-server -f tcp/Dockerfile .

build-docker-udp:
	docker build -t udp-server -f udp/Dockerfile .

build-docker-grpc:
	docker build -t grpc-server -f grpc/Dockerfile .

run-docker-tcp:
	docker run -p 3333:3333 -it tcp-server

run-docker-udp:
	docker run -p 3334:3334 -it udp-server

run-docker-grpc:
	docker run -p 50051:50051 -it grpc-server
