# syntax=docker/dockerfile:1.5
FROM golang:1.19-alpine as builder

WORKDIR /go/src/github.com/nginxinc/kic-test-containers/
COPY tcp/main.go ./tcp/
COPY go.mod utils.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /main ./tcp/

FROM scratch as goreleaser
ARG TARGETARCH

COPY dist/tcp_linux_${TARGETARCH}*/main /app/main

ENTRYPOINT ["/app/main"]

FROM scratch

COPY --from=builder /main /app/

ENTRYPOINT ["/app/main"]
