# syntax=docker/dockerfile:1.10
FROM golang:1.23-alpine AS builder

WORKDIR /go/src/github.com/nginxinc/kic-test-containers/
COPY udp/main.go ./udp/
COPY go.mod utils.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /main ./udp/

FROM scratch AS goreleaser
ARG TARGETARCH

COPY dist/udp_linux_${TARGETARCH}*/main /app/main

ENTRYPOINT ["/app/main"]

FROM scratch

COPY --from=builder /main /app/

ENTRYPOINT ["/app/main"]
