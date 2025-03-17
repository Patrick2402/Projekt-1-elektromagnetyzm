FROM golang:1.24-alpine AS builder

RUN apk add --no-cache git

WORKDIR /app

COPY . .

RUN go mod download

RUN CGO_ENABLED=0 go build -a -ldflags "-s -w" -o bin/kics cmd/console/main.go

RUN mkdir -p assets/queries assets/cwe_csv assets/libraries

FROM alpine:3.19

RUN apk add --no-cache ca-certificates

WORKDIR /app

COPY --from=builder /app/bin/kics /app/bin/kic

ENV PATH $PATH:/app/bin

ENTRYPOINT ["/app/bin/kics"]
