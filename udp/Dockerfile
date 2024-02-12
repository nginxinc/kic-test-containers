# syntax=docker/dockerfile:1.5
FROM golang:1.22-alpine as builder

WORKDIR /go/src/github.com/nginxinc/kic-test-containers/
COPY udp/main.go ./udp/
COPY go.mod utils.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /main ./udp/

FROM scratch as goreleaser
ARG TARGETARCH

COPY dist/udp_linux_${TARGETARCH}*/main /app/main

ENTRYPOINT ["/app/main"]

FROM scratch

COPY --from=builder /main /app/

ENTRYPOINT ["/app/main"]
