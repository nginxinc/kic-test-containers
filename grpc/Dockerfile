# syntax=docker/dockerfile:1.5
FROM golang:1.22 as builder

RUN git clone -b v1.63.0 --depth 1 https://github.com/grpc/grpc-go
WORKDIR /go/grpc-go/examples
RUN CGO_ENABLED=0 go build -C helloworld/greeter_server -o /greeter_server

FROM scratch
COPY --from=builder /greeter_server /
CMD ["/greeter_server"]
