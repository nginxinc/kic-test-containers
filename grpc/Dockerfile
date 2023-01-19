# syntax=docker/dockerfile:1.5
FROM golang:1.19 as builder

RUN GO111MODULE=off go get google.golang.org/grpc/examples/helloworld/greeter_server
WORKDIR /go/src/google.golang.org/grpc/examples/helloworld/greeter_server
RUN CGO_ENABLED=0 go build -o /greeter_server

FROM scratch
COPY --from=builder /greeter_server /
CMD ["/greeter_server"]
