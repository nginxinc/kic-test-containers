# syntax=docker/dockerfile:1.5
FROM golang:1.19 as builder

RUN git clone https://github.com/grpc/grpc-go.git

WORKDIR /go/grpc-go/examples/route_guide/server

RUN sed -i -e 's/localhost//g' server.go
RUN CGO_ENABLED=0 go build -o /grpc_server server.go

FROM scratch
COPY --from=builder /grpc_server /
CMD ["/grpc_server"]
